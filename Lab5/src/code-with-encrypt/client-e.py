import socket
import time
import logging
import os
import statistics
import argparse
from crypto_utils import encrypt_message, decrypt_message

# --- Configuración de Logging ---
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Configuración base del logger (se complementará con el nombre del protocolo)
def setup_client_logger(protocol):
    client_log_file = os.path.join(LOG_DIR, f'{protocol}_client.log')
    latency_log_file = os.path.join(LOG_DIR, f'{protocol}_latency.log')

    logger = logging.getLogger(f'{protocol}_client_logger')
    logger.setLevel(logging.INFO)
    
    latency_logger = logging.getLogger(f'{protocol}_latency_logger')
    latency_logger.setLevel(logging.INFO)

    # Evitar añadir handlers múltiples veces
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        file_handler = logging.FileHandler(client_log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        latency_handler = logging.FileHandler(latency_log_file)
        latency_handler.setFormatter(logging.Formatter('%(message)s'))
        latency_logger.addHandler(latency_handler)
    
    return logger, latency_logger

# --- Configuración del Cliente ---
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
GROUP_NAME = 'Lenox Legends v2.0'
SEND_INTERVAL_SECONDS = 1
NUM_PACKETS_TO_SEND = 100
RECEIVE_TIMEOUT_SECONDS = 2

def start_client():
    parser = argparse.ArgumentParser(description="Cliente TCP/UDP unificado.")
    parser.add_argument('--protocol', type=str, default='tcp', choices=['tcp', 'udp'],
                        help="Protocolo a usar: 'tcp' o 'udp'. Por defecto: tcp")
    args = parser.parse_args()

    protocol = args.protocol.upper()
    logger, latency_logger = setup_client_logger(args.protocol)
    
    latencies = []

    if protocol == 'TCP':
        sock_type = socket.SOCK_STREAM
    elif protocol == 'UDP':
        sock_type = socket.SOCK_DGRAM
    else:
        logger.critical("Protocolo no válido. Use 'tcp' o 'udp'.")
        return

    with socket.socket(socket.AF_INET, sock_type) as s:
        try:
            if protocol == 'TCP':
                logger.info(f"Intentando conectar a {SERVER_HOST}:{SERVER_PORT} usando {protocol}...")
                s.connect((SERVER_HOST, SERVER_PORT))
                logger.info(f"Conectado al servidor.")
            elif protocol == 'UDP':
                logger.info(f"Cliente {protocol} v4 listo para enviar a {SERVER_HOST}:{SERVER_PORT}...")

            for i in range(1, NUM_PACKETS_TO_SEND + 1):
                unique_id = f"{GROUP_NAME}-{i:03d}"
                message = f"Hola, soy el paquete {unique_id}"
                
                start_time = time.perf_counter()
                
                if protocol == 'TCP':
                    message = encrypt_message(message)  # Encriptar el mensaje antes de enviarlo
                    logger.debug(f"Mensaje encriptado: {message}")
                    s.sendall(message.encode('utf-8'))
                elif protocol == 'UDP':
                    s.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
                
                logger.info(f"Enviando: {message}")

                s.settimeout(RECEIVE_TIMEOUT_SECONDS)
                response = None
                try:
                    if protocol == 'TCP':
                        data = s.recv(1024)
                        if not data: # TCP closed
                            logger.warning(f"El servidor cerró la conexión inesperadamente.")
                            break
                        response = decrypt_message(data.decode('utf-8'))  # Decriptar el mensaje recibido

                    elif protocol == 'UDP':
                        data, addr = s.recvfrom(1024)
                        response = data.decode('utf-8')
                        # En UDP, el ACK no tiene una dirección asociada fija como en TCP
                        # pero `addr` contiene la dirección del remitente del ACK.
                    
                    end_time = time.perf_counter()
                    latency_ms = (end_time - start_time) * 1000
                    latencies.append(latency_ms)
                    
                    logger.info(f"Recibido ACK: {response} | Latencia: {latency_ms:.3f} ms")
                    latency_logger.info(f"{latency_ms:.3f}")
                    
                except socket.timeout:
                    logger.error(f"Timeout: No se recibió ACK del servidor para el paquete {unique_id}.")
                    # En UDP, un timeout significa pérdida; en TCP, es un problema serio.
                    if protocol == 'TCP':
                        break # En TCP, un timeout de recv suele indicar un problema grave, mejor salir.
                except Exception as e:
                    logger.error(f"Error al recibir ACK: {e}")
                    if protocol == 'TCP':
                        break # En TCP, cualquier error de recepción suele indicar un problema grave.

                if i < NUM_PACKETS_TO_SEND:
                    time.sleep(SEND_INTERVAL_SECONDS)

        except ConnectionRefusedError:
            logger.error(f"Error: La conexión fue rechazada. Asegúrate de que el servidor esté corriendo en {SERVER_HOST}:{SERVER_PORT}.")
        except Exception as e:
            logger.error(f"Ocurrió un error en el cliente {protocol}: {e}")
        finally:
            logger.info(f"Cliente {protocol} finalizado.")
            
            if latencies:
                min_latency = min(latencies)
                max_latency = max(latencies)
                avg_latency = sum(latencies) / len(latencies)
                
                jitter = 0.0
                if len(latencies) > 1:
                    jitter = statistics.stdev(latencies)
                else:
                    logger.warning("No hay suficientes muestras de latencia para calcular el jitter (se requiere al menos 2).")

                logger.info(f"--- Estadísticas de Latencia y Jitter para {len(latencies)} paquetes ({protocol}) ---")
                logger.info(f"Latencia Mínima: {min_latency:.3f} ms")
                logger.info(f"Latencia Máxima: {max_latency:.3f} ms")
                logger.info(f"Latencia Promedio: {avg_latency:.3f} ms")
                logger.info(f"Jitter (Desviación Estándar): {jitter:.3f} ms")
                logger.info(f"--------------------------------------------------")
                
                latency_logger.info(f"--- Estadísticas de Latencia y Jitter para {len(latencies)} paquetes ({protocol}) ---")
                latency_logger.info(f"Min: {min_latency:.3f} ms")
                latency_logger.info(f"Max: {max_latency:.3f} ms")
                latency_logger.info(f"Avg: {avg_latency:.3f} ms")
                latency_logger.info(f"Jitter (StdDev): {jitter:.3f} ms")
            else:
                logger.warning(f"No se recibieron ACKs válidos para calcular latencias/jitter.")

if __name__ == '__main__':
    start_client()