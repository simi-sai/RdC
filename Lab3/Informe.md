# Trabajo Practico N°3 - Práctico

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

### 1. Introducción Teórica

#### OSPF

El protocolo del primer camino mas corto posible (OSPF, Open Shortest Path First) se usa de forma generalizada como protocolo de enrutamiento interior en redes TPC/IP. OSPF calcula una ruta a traves de una interconexión de redes que suponga el menor coste de a cuerdo a una métrica de coste configurable por usuario. El usuario puede configurar el coste para que exprese una función del retardo, velocidad de transmisión, el coste económico u otros factores. OSPF es capaz de equilibrar las cargas entre múltiples caminos de igual coste.

##### Resumen de Caracteristicas de OSPF

| Característica       | Detalle                                                                 |
|----------------------|-------------------------------------------------------------------------|
| Tipo              | Protocolo IGP de estado de enlace                                       |
| Algoritmo         | Dijkstra (SPF - Shortest Path First)                                    |
| Métrica           | Cost (costo basado en el ancho de banda)                                |
| Convergencia      | Rápida (actualiza cambios de red muy rápido)                            |
| Jerarquía         | Soporta jerarquía de áreas (área backbone y otras)                      |
| Autenticación     | Soporta autenticación para mayor seguridad                              |
| Multicast         | Usa multicast para actualizaciones (224.0.0.5 y 224.0.0.6)              |
| Estándar abierto  | No propietario, definido por el RFC 2328                                |
----

#### Clases de Red

La direccion IP esta codificada para permitir una asignación variable de bits para especificar la red y el computador, como se muestra en la siguiente imagen: 

![Formatos de direcciones IP](/Lab3/Imagenes/ClasesRedes.PNG)

Este esquema de codificación proporciona flexibilidad al asignar las direcciones a los computadores y permite una mezcla de tamaños de red en un conjunto de redes. Existen tres clases principales de redes que se pueden asociar a las siguientes condiciones:

* **Clase A:** pocas redes, cada una con muchos computadores.
* **Clase B:** un número medio de redes, cada una con un número medio de computadores.
* **Clase C:** muchas redes, cada una con pocos computadores.

| Clase | Primer octeto (rango) | Bits de red | Bits de host | Número de redes     | Hosts por red (sin contar 0 y 255) | Ejemplo       |
|-------|------------------------|-------------|---------------|----------------------|-------------------------------------|----------------|
| A     | 0 - 127                | 8           | 24            | 128 (solo 1-126)     | ~16 millones                        | 10.0.0.1       |
| B     | 128 - 191              | 16          | 16            | ~16,000              | ~65,000                             | 172.16.0.1     |
| C     | 192 - 223              | 24          | 8             | ~2 millones          | 254                                 | 192.168.1.1    |
| D     | 224 - 239              | -           | -             | Multicast            | No para host                        | 224.0.0.1      |
| E     | 240 - 255              | -           | -             | Reservada (experimentos) | -                               | 240.0.0.1      |
----

#### Algoritmos de Shortest Path

Los algoritmos de camino mas corto son técnicas que permiten encontrar el camino más corto entre un nodo de inicio y uno de destino dentro de un grafo. Algunos de estos algoritmos son:

##### 1. Algoritmo de Dijkstra

Uno de los algoritmos mas conocidos y utilizados para encontrar el camino mas corto en grafos con pesos NO negativos. Funciona para grafos dirigidos y no dirigidos y puede ser implementado usando una cola de prioridad para optimizar el rendimiento. Es **Greedy**, es decir, toma la desicion óptima en cada paso basándose en la información local.

- Ventaja: Muy eficiente para grafos dispersos (pocos nodos y aristas).
- Desventaja: No puede manejar grafos con pesos negativos.

##### 2. Algoritmo de Bellman-Ford

Este algoritmo es util cuando el grafo tiene pesos negativos en las aristas. Es mas lento que Dijkstra, especialmente en grafos grandes.

##### 3. Algoritmo de Floyd-Warshall

A diferencia de Dijkstra y Bellman-Ford, calcula las distancias mas cortas entre los pares nodos en el grafo. Es muy util cuando se necesitan todas las rutas mas cortas de un grafo completo. Es muy lento para grafos grandes.

##### 4. Algoritmo A* (A-star)

Este algoritmo es una modificacion del algoritmo de Dijkstra que incorpora heurísticas para mejorar el rendimiento en ciertos escenarios, como la navegacion de mapas.

#### Comparacion de los Algoritmos:

| Algoritmo      | Mejor para                                           | Limitaciones                                 | Complejidad Temporal       |
|----------------|------------------------------------------------------|----------------------------------------------|----------------------------|
| Dijkstra       | Grafos sin pesos negativos, rutas más rápidas        | No funciona con pesos negativos              | O((V + E) * log(V))        |
| Bellman-Ford   | Grafos con pesos negativos, detecta ciclos negativos | Más lento que Dijkstra                       | O(V * E)                   |
| Floyd-Warshall | Todos los pares de nodos, grafos completos           | Muy lento para grafos grandes                | O(V³)                      |
| A*             | Búsqueda eficiente en mapas o rutas (con heurísticas) | Depende de una heurística precisa            | Depende de la heurística   |
----

#### Aplicación de grafos en OSPF

Una red de computadoras puede modelarse naturalmente como un grafo:

- **Nodos**: Representan dispositivos como routers, switches o hosts.
- **Aristas**: Representan las conexiones fisicas o logicas entre los dispositivos.
- **Pesos en las aristas**: Representan costos de transmision, como ancho de banda, latencia, carga de enlace o costo arbitrario asignado por el administrador de Red.

OSPF es un protocolo que utiliza la teoria de grafos para encontrar los caminos mas cortos desde un router hasta todos los destinos posibles en la red. 

##### Construccion del Grafo

Cada router OSPF recopila informacion sobre todos los enlaces a los que esta conectado y distribuye esa informacion a traves de Link-State Advertisements (LSAs). 

Con esto:

- Todos los routers construyen un mapa identico de la red, que es un grafo completo de todos los routers y enlaces.
- Cada nodo tiene una copia del grafo, donde conoce la topologia completa.

##### Aplicacion del Algoritmo de Dijkstra

Una vez que el router tiene el grafo de la red, utiliza el algoritmo de Dijkstra para calcular la mejor ruta a cada destino. Esto construye la tabla de enrutamiento, que indica el mejor siguiente salto (next-hop) hacia cada red. 

Cuando cambia el estado de un enlace, se envia un nuevo LSA y todos los routers actualizan su grafo y recalculan sus rutas usando este algoritmo.

### 2. Esquema de Direccionamiento IP

Red propuesta:

![Red](/Lab3/Imagenes/Red.PNG)

Vamos a dividir la red en subredes logicas.

#### 1. Segmentación de redes clase B para hosts

- **Red principal:** `172.16.0.0/16` (clase B).
- **Subredes /24 para hosts:**
  - **Subred S1 (H1, H2, H3):** `172.16.0.0/24`.
  - **Subred H4 (R4):** `172.16.1.0/24`.
  - **Subred H5 (R5):** `172.16.2.0/24`.

---

#### 2. Redes clase C para enlaces entre routers
| **Enlace**  | **Red asignada**   | **Router A (IP)**  | **Router B (IP)**  |
|-------------|---------------------|--------------------|--------------------|
| **R1-R2**   | 192.168.1.0/24     | R1: 192.168.1.1   | R2: 192.168.1.2   |
| **R1-R3**   | 192.168.2.0/24     | R1: 192.168.2.1   | R3: 192.168.2.2   |
| **R2-R3**   | 192.168.3.0/24     | R2: 192.168.3.1   | R3: 192.168.3.2   |
| **R3-R4**   | 192.168.4.0/24     | R3: 192.168.4.1   | R4: 192.168.4.2   |
| **R3-R5**   | 192.168.5.0/24     | R3: 192.168.5.1   | R5: 192.168.5.2   |
| **R4-R5**   | 192.168.6.0/24     | R4: 192.168.6.1   | R5: 192.168.6.2   |

---

#### 3. Tabla de direccionamiento completa

| **Dispositivo** | **Interfaz**         | **Dirección IP**   | **Máscara**         | **Descripción**                    |
|-----------------|----------------------|--------------------|---------------------|------------------------------------|
| **R1**          | Loopback             | 10.0.0.1           | 255.255.255.255     | Loopback (administración)          |
| R1              | Enlace R1-R2         | 192.168.1.1        | 255.255.255.0       | Conexión a R2                      |
| R1              | Enlace R1-R3         | 192.168.2.1        | 255.255.255.0       | Conexión a R3                      |
| **R2**          | Enlace R1-R2         | 192.168.1.2        | 255.255.255.0       | Conexión a R1                      |
| R2              | Enlace R2-R3         | 192.168.3.1        | 255.255.255.0       | Conexión a R3                      |
| R2              | Interfaz LAN (S1)    | 172.16.0.1         | 255.255.255.0       | Gateway para H1, H2, H3            |
| **R3**          | Enlace R1-R3         | 192.168.2.2        | 255.255.255.0       | Conexión a R1                      |
| R3              | Enlace R2-R3         | 192.168.3.2        | 255.255.255.0       | Conexión a R2                      |
| R3              | Enlace R3-R4         | 192.168.4.1        | 255.255.255.0       | Conexión a R4                      |
| R3              | Enlace R3-R5         | 192.168.5.1        | 255.255.255.0       | Conexión a R5                      |
| **R4**          | Enlace R3-R4         | 192.168.4.2        | 255.255.255.0       | Conexión a R3                      |
| R4              | Enlace R4-R5         | 192.168.6.1        | 255.255.255.0       | Conexión a R5                      |
| R4              | Interfaz LAN (H4)    | 172.16.1.1         | 255.255.255.0       | Gateway para H4                    |
| **R5**          | Enlace R3-R5         | 192.168.5.2        | 255.255.255.0       | Conexión a R3                      |
| R5              | Enlace R4-R5         | 192.168.6.2        | 255.255.255.0       | Conexión a R4                      |
| R5              | Interfaz LAN (H5)    | 172.16.2.1         | 255.255.255.0       | Gateway para H5                    |
| **S1**          | VLAN 1               | 172.16.0.254       | 255.255.255.0       | Switch S1 (gestión)                |
| **H1**          | eth0                 | 172.16.0.101       | 255.255.255.0       | Host 1 (gateway: 172.16.0.1)       |
| **H2**          | eth0                 | 172.16.0.102       | 255.255.255.0       | Host 2 (gateway: 172.16.0.1)       |
| **H3**          | eth0                 | 172.16.0.103       | 255.255.255.0       | Host 3 (gateway: 172.16.0.1)       |
| **H4**          | eth0                 | 172.16.1.2         | 255.255.255.0       | Host 4 (gateway: 172.16.1.1)       |
| **H5**          | eth0                 | 172.16.2.2         | 255.255.255.0       | Host 5 (gateway: 172.16.2.1)       |

---

### 3. Configuracion de routers para que utilice el protocolo OSPF
Luego de configurar los routers para utilizar protocolo OSPF verificamos la conexion punto a punto entre los dispositivos enlazados:

#### 1- Comprobar conectividad IP básica
De R1 a R2:

![alt text](/Lab3/Imagenes/PingR1-R2.png)

De R1 a R3:

![alt text](/Lab3/Imagenes/PingR1-R3.png)

De H1 a H5:

![alt text](/Lab3/Imagenes/PingH1-H5.png)

Si hacemos esto con todos los routers con sus respectivos vecinos deberia dar el mismo resultado
#### 2- Verificar la vecindad OSPF
Verificamos la vecindad de R3:

![alt text](/Lab3/Imagenes/VecinosR3.png)

Si hacemos esto para todos los routers nos dara la misma informacion pero con sus respectivos vecinos de ese router
#### 3- Revisar la tabla de enrutamiento
 Las rutas OSPF aparecen con la letra O:
![alt text](/Lab3/Imagenes/TablaEnrutamientoR3.png)

Con el mismo codigo en los distintos routers apareceran las rutas OSPF

### 4. Identificamos y analizamos los mensajes de OSPF
#### 1. Panel de Simulación
![alt text](/Lab3/Imagenes/Simulacion.png)

**Explicación**  
- La ventana muestra la **lista de eventos** capturados en modo “Simulation”.  
- Se ha filtrado para ver sólo mensajes **OSPF**.  
- Cada línea indica:
  - **Vis. Time(sec)**: instante de la simulación en segundos.
  - **Last Device**: emisor del paquete (p. ej. `Router3`).
  - **At Device**: receptor del paquete (p. ej. `Router4`, `H4`, etc.).
  - **Type**: tipo de PDU (aquí todos son OSPF Hello, DBD, LSR, etc.).
- En este fragmento vemos varios **OSPF Hello** intercambiados entre `Router3` → `Router4`, luego `Router4` → `H4`, etc.

---

#### 2.Detalle OSI del PDU recibido
![alt text](/Lab3/Imagenes/PDUInformation-OSIModel.png)

**Explicación por capas**  
- **Layer 1**: el paquete llega a la interfaz `Serial0/0/0` de `Router4`.  
- **Layer 2**: tramas HDLC (encapsulación serial).  
- **Layer 3**: cabecera IP con:
  - **Src IP**: `192.168.4.1` (interfaz de `Router3`).
  - **Dest IP**: `224.0.0.5` (dirección multicast de vecinos OSPF).  
- No hay capas superiores mostradas en esta vista OSI; el contenido OSPF se examina en “Inbound PDU Details”.

---

#### 3.Campos del OSPF Hello
![alt text](/Lab3/Imagenes/OSPF-Hello.png)

| Campo                     | Valor ejemplo      | Significado / Impacto                                          |
|---------------------------|--------------------|----------------------------------------------------------------|
| **VERSION NUM**           | 2                  | Versión OSPF para IPv4.                                        |
| **TYPE**                  | 1                  | Tipo de paquete (1 = Hello).                                   |
| **PACKET LENGTH**         | 48                 | Longitud total en bytes.                                       |
| **ROUTER ID**             | 192.168.5.1        | Identificador único del emisor.                                |
| **AREA ID**               | 0.0.0.0            | Área OSPF (aquí, área 0).                                      |
| **CHECKSUM**              | 0                  | Suma de verificación (calculará un valor en redes reales).     |
| **AUTH TYPE**             | 0                  | Tipo de autenticación (0 = sin auth).                          |
| **NETWORK MASK**          | 255.255.255.0      | Máscara de la subred del enlace punto-a-punto.                 |
| **HELLO INTERVAL**        | 10                 | Frecuencia de envío de Hellos (debe coincidir en ambos extremos). |
| **ROUTER DEAD INTERVAL**  | 40                 | Tiempo tras el cual se considera muerto al vecino (4× Hello).  |
| **OPTIONS**               | 0                  | Bits de capacidades (p.ej. soporte de redes stub/NSSA).        |
| **DESIGNATED ROUTER**     | 0.0.0.0            | En multiacceso, DR (aquí 0.0.0.0 porque es punto-a-punto).      |
| **BACKUP DESIGNATED ROUTER** | 0.0.0.0         | BDR en multiacceso (no aplica en punto-a-punto).               |
| **NEIGHBOR**              | 192.168.4.2        | Lista de Router IDs con los que ya se vio Hello (vecindad).    |

**Comentarios**  
- Los temporizadores **Hello** y **Dead** deben coincidir en ambos routers para formar adyacencia.  
- El **Router ID** no puede duplicarse en la misma área.  
- El **Neighbor** listado confirma que `Router4` vio un Hello previo de `Router3` (ID `192.168.4.2`).

Con estas capturas explicadas demuestras:
1. Cómo se generan y envían los **HS** (Hello) en OSPF.  
2. Qué información crítica transportan y cómo afecta a la formación de adyacencias.  
3. Qué buscar (coherencia de temporizadores, área, IDs, máscara) para diagnosticar fallos de convergencia.  
4. La ventaja de usar el modo **Simulation** de Packet Tracer para desglosar paso a paso cada PDU.  