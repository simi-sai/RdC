import socket
import threading
import logging
import os
import argparse
from crypto_utils import encrypt_message, decrypt_message

# --- Configuración de Logging ---
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Configuración base del logger (se complementará con el nombre del protocolo)
def setup_server_logger(protocol):
    log_file = os.path.join(LOG_DIR, f'{protocol}_server.log')
    logger = logging.getLogger(f'{protocol}_server_logger')
    logger.setLevel(logging.INFO)
    
    # Evitar añadir handlers múltiples veces si la función se llama más de una vez
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    
    return logger

# --- Configuración del Servidor ---
HOST = '0.0.0.0'
PORT = 65432

def handle_tcp_client(conn, addr, logger):
    client_id = f"{addr[0]}:{addr[1]}"
    logger.info(f"Conectado por {client_id}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                logger.info(f"Cliente {client_id} cerró la conexión.")
                break
            
            message = decrypt_message(data.decode('utf-8'))
            logger.info(f"Recibido de {client_id}: {message}")

            try:
                group_name, seq_num_str = message.rsplit('-', 1)
                logger.debug(f"    Nombre de grupo: {group_name}, Número secuencial: {seq_num_str}")
            except ValueError:
                logger.warning(f"    Formato de mensaje no reconocido de {client_id}: {message}")

            response = encrypt_message(f"ACK: {message}")
            logger.debug(f"    Respuesta cifrada: {response}")
            conn.sendall(response.encode('utf-8'))
            logger.info(f"Enviado a {client_id}: {response}")

    except ConnectionResetError:
        logger.warning(f"Conexión con {client_id} reseteada por el cliente.")
    except Exception as e:
        logger.error(f"Error manejando cliente {client_id}: {e}")
    finally:
        logger.info(f"Desconectado de {client_id}")
        conn.close()

def start_server():
    parser = argparse.ArgumentParser(description="Servidor TCP/UDP unificado.")
    parser.add_argument('--protocol', type=str, default='tcp', choices=['tcp', 'udp'],
                        help="Protocolo a usar: 'tcp' o 'udp'. Por defecto: tcp")
    args = parser.parse_args()

    protocol = args.protocol.upper()
    logger = setup_server_logger(args.protocol)
    
    if protocol == 'TCP':
        sock_type = socket.SOCK_STREAM
    elif protocol == 'UDP':
        sock_type = socket.SOCK_DGRAM
    else:
        logger.critical("Protocolo no válido. Use 'tcp' o 'udp'.")
        return

    with socket.socket(socket.AF_INET, sock_type) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((HOST, PORT))
            
            if protocol == 'TCP':
                s.listen()
                logger.info(f"Servidor {protocol} escuchando en {HOST}:{PORT}...")
                while True:
                    conn, addr = s.accept()
                    client_thread = threading.Thread(target=handle_tcp_client, args=(conn, addr, logger))
                    client_thread.start()
            elif protocol == 'UDP':
                logger.info(f"Servidor {protocol} escuchando en {HOST}:{PORT}...")
                while True:
                    data, addr = s.recvfrom(1024)
                    message = data.decode('utf-8')
                    logger.info(f"Recibido de {addr[0]}:{addr[1]}: {message}")

                    try:
                        group_name, seq_num_str = message.rsplit('-', 1)
                        logger.debug(f"    Nombre de grupo: {group_name}, Número secuencial: {seq_num_str}")
                    except ValueError:
                        logger.warning(f"    Formato de mensaje no reconocido de {addr[0]}:{addr[1]}: {message}")

                    response = f"ACK: {message}"
                    s.sendto(response.encode('utf-8'), addr)
                    logger.info(f"Enviado ACK a {addr[0]}:{addr[1]}: {response}")

        except Exception as e:
            logger.critical(f"Falló el inicio o la operación del servidor {protocol}: {e}")

if __name__ == '__main__':
    start_server()