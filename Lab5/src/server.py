import socket
import threading
import datetime

HOST = '0.0.0.0'  # Escucha en todas las interfaces disponibles
PORT = 65432      # Puerto arbitrario

def handle_client(conn, addr):
    """Maneja la comunicación con un cliente individual."""
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectado por {addr}")
    try:
        while True:
            data = conn.recv(1024)  # Recibe hasta 1024 bytes
            if not data:
                break  # El cliente cerró la conexión
            message = data.decode('utf-8')
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Recibido de {addr}: {message}")

            try:
                group_name, seq_num_str = message.rsplit('-', 1)
                print(f"    Nombre de grupo: {group_name}, Número secuencial: {seq_num_str}")
            except ValueError:
                print("    Formato de mensaje no reconocido.")

            response = f"ACK: {message}"
            conn.sendall(response.encode('utf-8'))
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Enviado a {addr}: {response}")
    except ConnectionResetError:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conexión con {addr} reseteada por el cliente.")
    finally:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Desconectado de {addr}")
        conn.close()

def start_server():
    """Inicia el servidor TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reusar la dirección
        s.bind((HOST, PORT))
        s.listen()
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Servidor escuchando en {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            # Inicia un nuevo hilo para manejar cada conexión de cliente
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == '__main__':
    start_server()