# Trabajo Practico N°5 - Scripts de Comunicación entre Computadoras

**Integrantes**

- Enrique L. Graham.
- Franco I. Mamani.
- Simón Saillen.
- Rodrigo S. Vargas.

**Lenox Legends v2.0**

**Universidad Nacional de Córdoba - FCEFyN**

**Catedra de Redes de Computadoras**

**Profesores**

- Santiago M. Henn.
- Facundo N. 0. Cuneo.

## Desarrollo

### 1. Desarrollo de Scripts y Configuración de Computadoras (TCP)

#### a. Prueba de Script entre dos Computadoras

Para el desarrollo de los scripts y la configuración de las computadoras, se siguieron los siguientes pasos:

1. **Instalación de Dependencias**: Se instalaron las dependencias necesarias en cada computadora, incluyendo Python y las bibliotecas requeridas para la ejecución de los scripts.

2. **Configuración de la Red**: Se configuraron las direcciones IP y las rutas necesarias para asegurar que todas las computadoras pudieran comunicarse entre sí.

Computadora 1 - Cliente (Windows):

Conectada por ethernet al router.

!["Imagen de la configuración de red"](./Imagenes/Windows-IP.png)

Computadora 2 - Servidor (Linux):

Conectada por Wi-Fi al router.

!["Imagen de la configuración de red"](./Imagenes/Linux-IP.png)

3. **Prueba de Conectividad**: Se realizaron pruebas de conectividad entre las computadoras utilizando comandos como `ping` para verificar que la comunicación estaba funcionando correctamente.

Ping Servidor a Cliente:

!["Ping desde el servidor al cliente"](./Imagenes/PING-SC.png)

Ping Cliente a Servidor:

!["Ping desde el cliente al servidor"](./Imagenes/PING-CS.png)

4. **Configuración de Firewall**: Se configuraron las reglas del firewall en ambas computadoras para permitir el tráfico necesario entre ellas.

Configuración del Firewall en el Cliente:

Generalmente Windows no bloquea el tráfico de salida.

Configuración del Firewall en el Servidor:

!["Imagen de la configuración del firewall"](./Imagenes/Firewall-L.png)

1. **Configuración de Scripts**: Se configuraron los scripts en cada computadora para que se ejecutaran correctamente.

Configuración del Script en el Cliente:

```python
# --- Configuración del Cliente ---
SERVER_HOST = '192.168.1.5'         # La dirección IP del servidor
SERVER_PORT = 65432                 # El puerto del servidor
GROUP_NAME = 'Lenox Legends v2.0'   # Nombre identificatorio del grupo
SEND_INTERVAL_SECONDS = 1           # Intervalo de tiempo entre envíos en segundos
NUM_PACKETS_TO_SEND = 5             # Número de paquetes a enviar
```

>[!NOTE]
> Elegimos 5 paquetes porque sinó la impresión en la consola del servidor era muy grande.

6. **Ejecución de Scripts**: Se ejecutaron los scripts en ambas computadoras para iniciar la comunicación.
El script del cliente envía mensajes al servidor, y el servidor los recibe y los imprime en la consola.

Prueba de Comunicación, Cliente a Servidor:

!["Imagen de la prueba de comunicación A"](./Imagenes/Prueba1-C.png)

Prueba de Comunicación, Servidor a Cliente:

!["Imagen de la prueba de comunicación B"](./Imagenes/Prueba1-S.png)

7. **Captura de Paquetes**: Se utilizó Wireshark para capturar los paquetes enviados y recibidos durante la prueba de comunicación.

!["Wireshark Captura de Paquetes"](./Imagenes/Wireshark-L1.png)

Paquete Aleatorio Capturado:

!["Paquete Aleatorio Capturado"](./Imagenes/Wireshark-Packet.png)

#### b. Agregando Logging

Para agregar logging a los scripts, se utilizan las bibliotecas `logging` y `os` de Python. Se configura el logging para registrar eventos importantes, como el inicio y finalización de la comunicación, así como los mensajes enviados y recibidos.

>[!NOTE]
>Dentro de la carpeta `Logs` se encuentran los archivos de log generados por los scripts.

#### c. Calculo de latencia y jitter

Para calcular la latencia, se implementa una secuencia de 100 paquetes enviados con una frecuencia de 1 segundo entre cada envío. Se registra el tiempo de envío y recepción de cada paquete, y se calcula la latencia como la diferencia entre estos tiempos.

Para calcular la latencia (también conocida como Round-Trip Time o RTT) de los paquetes TCP, modificamos el script del cliente para que envíe 100 paquetes y mida el tiempo que tarda en enviar un paquete y recibir su confirmación (ACK) del servidor. Usaremos el módulo time de Python para estas mediciones. Para calcular el jitter, usaremos las latencias individuales que ya estamos midiendo y mediremos la desviación estándar de las latencias. Para esto, se utiliza la biblioteca `statistics` de Python.

Estos valores se almacenan en un archivo de log para su posterior análisis.

Luego de ejecutar el script, se obtienen los siguientes resultados (para ver completo el log, ver carpeta `Logs`):

```plaintext
--- Estad�sticas de Latencia y Jitter para 100 paquetes ---
Min: 3.267 ms
Max: 127.497 ms
Avg: 28.214 ms
Jitter (StdDev): 24.874 ms
```

### 2. Desarrollo de Scripts (UDP)

UDP es un protocolo sin conexión, lo que significa que no establece una conexión persistente como TCP. Cada paquete (datagrama) se envía de forma independiente, y no hay garantías de entrega, orden ni detección de errores incorporadas en el protocolo mismo. Esto lo hace más rápido y con menos sobrecarga, pero requiere que la aplicación maneje la confiabilidad si es necesaria.

Dado que UDP no tiene ACKs incorporados, tendremos que implementar nuestro propio mecanismo de ACK a nivel de aplicación para poder calcular la latencia y el jitter de manera análoga.

Cambios realizados para la implementación de UDP:

1. **Cambio de Protocolo**: Se cambió el protocolo de TCP a UDP en los scripts del cliente y del servidor.

Esto se logra utilizando el socket `SOCK_DGRAM` en lugar de `SOCK_STREAM`.

```python
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```


### 3.

### 4.