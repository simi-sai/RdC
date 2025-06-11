import socket
import time
import datetime

SERVER_HOST = '192.168.1.5'         # La dirección IP del servidor
SERVER_PORT = 65432                 # El puerto del servidor
GROUP_NAME = 'Lenox Legends v2.0'   # Nombre identificatorio del grupo
SEND_INTERVAL_SECONDS = 1           # Intervalo de tiempo entre envíos en segundos
NUM_PACKETS_TO_SEND = 10            # Número de paquetes a enviar

def start_client():
    """Inicia el cliente TCP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Intentando conectar a {SERVER_HOST}:{SERVER_PORT}...")
            s.connect((SERVER_HOST, SERVER_PORT))
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectado al servidor.")

            for i in range(1, NUM_PACKETS_TO_SEND + 1):
                unique_id = f"{GROUP_NAME}-{i:03d}"  # Formato: GROUP_NAME-001, GROUP_NAME-002, etc.
                message = f"Hola, soy el paquete {unique_id}"
                print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Enviando: {message}")
                s.sendall(message.encode('utf-8'))

                # Esperar la confirmación del servidor
                data = s.recv(1024)
                if data:
                    response = data.decode('utf-8')
                    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Recibido del servidor: {response}")
                else:
                    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] El servidor cerró la conexión inesperadamente.")
                    break

                if i < NUM_PACKETS_TO_SEND:
                    time.sleep(SEND_INTERVAL_SECONDS) # Esperar el intervalo configurado

    except ConnectionRefusedError:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: La conexión fue rechazada. Asegúrate de que el servidor esté corriendo en {SERVER_HOST}:{SERVER_PORT}.")
    except Exception as e:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ocurrió un error: {e}")
    finally:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cliente finalizado.")

if __name__ == '__main__':
    start_client()