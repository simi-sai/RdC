import socket
import threading
import datetime
import logging
import os

# --- Configuración de Logging ---
LOG_DIR = 'logs'
SERVER_LOG_FILE = os.path.join(LOG_DIR, 'server.log')

# Asegurarse de que el directorio de logs exista
os.makedirs(LOG_DIR, exist_ok=True)

# Configurar el logger del servidor
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(SERVER_LOG_FILE),
        logging.StreamHandler() # También imprime en la consola
    ]
)
logger = logging.getLogger('server_logger')

# --- Configuración del Servidor ---
HOST = '0.0.0.0'  # Escucha en todas las interfaces disponibles
PORT = 65432      # Puerto arbitrario

def handle_client(conn, addr):
    """Maneja la comunicación con un cliente individual."""
    client_id = f"{addr[0]}:{addr[1]}"
    logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectado por {client_id}")
    try:
        while True:
            data = conn.recv(1024)  # Recibe hasta 1024 bytes
            if not data:
                logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cliente {client_id} cerró la conexión.")
                break  # El cliente cerró la conexión
            
            message = data.decode('utf-8')
            timestamp_received = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
            logger.info(f"[{timestamp_received}] Recibido de {client_id}: {message}")

            # Extraer el contenido identificatorio (por ejemplo, "GRUPO_XYZ-001")
            try:
                group_name, seq_num_str = message.rsplit('-', 1)
                logger.debug(f"    Nombre de grupo: {group_name}, Número secuencial: {seq_num_str}")
            except ValueError:
                logger.warning(f"    Formato de mensaje no reconocido de {client_id}: {message}")

            response = f"ACK: {message}"
            conn.sendall(response.encode('utf-8'))
            timestamp_sent = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # ms
            logger.info(f"[{timestamp_sent}] Enviado a {client_id}: {response}")

    except ConnectionResetError:
        logger.warning(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conexión con {client_id} reseteada por el cliente.")
    except Exception as e:
        logger.error(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error manejando cliente {client_id}: {e}")
    finally:
        logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Desconectado de {client_id}")
        conn.close()

def start_server():
    """Inicia el servidor TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reusar la dirección
        try:
            s.bind((HOST, PORT))
            s.listen()
            logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Servidor escuchando en {HOST}:{PORT}...")
            while True:
                conn, addr = s.accept()
                # Inicia un nuevo hilo para manejar cada conexión de cliente
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.start()
        except Exception as e:
            logger.critical(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Falló el inicio del servidor: {e}")

if __name__ == '__main__':
    start_server()