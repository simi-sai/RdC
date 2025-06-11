import socket
import time
import datetime
import logging
import os
import statistics

# --- Configuración de Logging ---
LOG_DIR = 'logs'
CLIENT_LOG_FILE = os.path.join(LOG_DIR, 'client.log')
LATENCY_LOG_FILE = os.path.join(LOG_DIR, 'latency.log')

# Asegurarse de que el directorio de logs exista
os.makedirs(LOG_DIR, exist_ok=True)

# Configurar el logger principal del cliente
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CLIENT_LOG_FILE),
        logging.StreamHandler() # También imprime en la consola
    ]
)
logger = logging.getLogger('client_logger')

# Configurar un logger específico para las latencias
latency_logger = logging.getLogger('latency_logger')
latency_logger.setLevel(logging.INFO)
latency_logger_handler = logging.FileHandler(LATENCY_LOG_FILE)
latency_logger_handler.setFormatter(logging.Formatter('%(message)s'))
latency_logger.addHandler(latency_logger_handler)

# --- Configuración del Cliente ---
SERVER_HOST = '192.168.1.5'         # La dirección IP del servidor
SERVER_PORT = 65432                 # El puerto del servidor
GROUP_NAME = 'Lenox Legends v2.0'   # Nombre identificatorio del grupo
SEND_INTERVAL_SECONDS = 1           # Intervalo de tiempo entre envíos en segundos
NUM_PACKETS_TO_SEND = 100           # Número de paquetes a enviar

def start_client():
    """Inicia el cliente TCP y calcula la latencia y el jitter."""
    latencies = [] # Lista para almacenar todas las latencias medidas

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Intentando conectar a {SERVER_HOST}:{SERVER_PORT}...")
            s.connect((SERVER_HOST, SERVER_PORT))
            logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectado al servidor.")

            for i in range(1, NUM_PACKETS_TO_SEND + 1):
                unique_id = f"{GROUP_NAME}-{i:03d}"  # Formato: GROUP_NAME-001, GROUP_NAME-002, etc.
                message = f"Hola, soy el paquete {unique_id}"
                
                start_time = time.perf_counter() # Marca de tiempo antes de enviar
                
                s.sendall(message.encode('utf-8'))
                timestamp_sent = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
                logger.info(f"[{timestamp_sent}] Enviando: {message}")

                # Esperar la confirmación del servidor
                s.settimeout(5) # Establece un timeout para recv para evitar bloqueo indefinido
                try:
                    data = s.recv(1024)
                    if data:
                        response = data.decode('utf-8')
                        end_time = time.perf_counter() # Marca de tiempo después de recibir ACK
                        
                        latency_ms = (end_time - start_time) * 1000 # Latencia en milisegundos
                        latencies.append(latency_ms)
                        
                        timestamp_received = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
                        logger.info(f"[{timestamp_received}] Recibido del servidor: {response} | Latencia: {latency_ms:.3f} ms")
                        latency_logger.info(f"{latency_ms:.3f}") # Registra solo la latencia en el archivo específico
                    else:
                        logger.warning(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] El servidor cerró la conexión inesperadamente.")
                        break
                except socket.timeout:
                    logger.error(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Timeout esperando respuesta del servidor para el paquete {unique_id}.")
                    break # Salir si no hay respuesta
                except Exception as recv_e:
                    logger.error(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error al recibir respuesta: {recv_e}")
                    break

                if i < NUM_PACKETS_TO_SEND:
                    time.sleep(SEND_INTERVAL_SECONDS) # Esperar el intervalo configurado

    except ConnectionRefusedError:
        logger.error(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: La conexión fue rechazada. Asegúrate de que el servidor esté corriendo en {SERVER_HOST}:{SERVER_PORT}.")
    except Exception as e:
        logger.error(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ocurrió un error: {e}")
    finally:
        logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cliente finalizado.")
        
        # --- Cálculo y Log de Estadísticas de Latencia y Jitter ---
        if latencies:
            min_latency = min(latencies)
            max_latency = max(latencies)
            avg_latency = sum(latencies) / len(latencies)
            
            # Calcular Jitter (Desviación Estándar de las latencias)
            # Solo si hay suficientes muestras (al menos 2)
            jitter = 0.0
            if len(latencies) > 1:
                jitter = statistics.stdev(latencies)
            else:
                logger.warning("No hay suficientes muestras de latencia para calcular el jitter (se requiere al menos 2).")

            logger.info(f"--- Estadísticas de Latencia y Jitter para {len(latencies)} paquetes ---")
            logger.info(f"Latencia Mínima: {min_latency:.3f} ms")
            logger.info(f"Latencia Máxima: {max_latency:.3f} ms")
            logger.info(f"Latencia Promedio: {avg_latency:.3f} ms")
            logger.info(f"Jitter (Desviación Estándar): {jitter:.3f} ms")
            logger.info(f"--------------------------------------------------")
            
            # También loguear en el archivo de latencias
            latency_logger.info(f"--- Estadísticas de Latencia y Jitter para {len(latencies)} paquetes ---")
            latency_logger.info(f"Min: {min_latency:.3f} ms")
            latency_logger.info(f"Max: {max_latency:.3f} ms")
            latency_logger.info(f"Avg: {avg_latency:.3f} ms")
            latency_logger.info(f"Jitter (StdDev): {jitter:.3f} ms")

if __name__ == '__main__':
    start_client()