import socket
import time
import datetime
import logging
import os

# --- Configuración de Logging ---
LOG_DIR = 'logs'
CLIENT_LOG_FILE = os.path.join(LOG_DIR, 'client.log')

# Asegurarse de que el directorio de logs exista
os.makedirs(LOG_DIR, exist_ok=True)

# Configurar el logger del cliente
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CLIENT_LOG_FILE),
        logging.StreamHandler() # También imprime en la consola
    ]
)
logger = logging.getLogger('client_logger')

# --- Configuración del Cliente ---
SERVER_HOST = '127.0.0.1'  # La dirección IP del servidor
SERVER_PORT = 65432        # El puerto del servidor
GROUP_NAME = 'GRUPO_XYZ'   # Nombre identificatorio del grupo
SEND_INTERVAL_SECONDS = 2  # Intervalo de tiempo entre envíos en segundos
NUM_PACKETS_TO_SEND = 10   # Número de paquetes a enviar

def start_client():
    """Inicia el cliente TCP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Intentando conectar a {SERVER_HOST}:{SERVER_PORT}...")
            s.connect((SERVER_HOST, SERVER_PORT))
            logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectado al servidor.")

            for i in range(1, NUM_PACKETS_TO_SEND + 1):
                unique_id = f"{GROUP_NAME}-{i:03d}"  # Formato: GRUPO_XYZ-001, GRUPO_XYZ-002, etc.
                message = f"Hola, soy el paquete {unique_id}"
                
                s.sendall(message.encode('utf-8'))
                timestamp_sent = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
                logger.info(f"[{timestamp_sent}] Enviando: {message}")

                # Esperar la confirmación del servidor
                s.settimeout(5) # Establece un timeout para recv para evitar bloqueo indefinido
                try:
                    data = s.recv(1024)
                    if data:
                        response = data.decode('utf-8')
                        timestamp_received = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
                        logger.info(f"[{timestamp_received}] Recibido del servidor: {response}")
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

if __name__ == '__main__':
    start_client()