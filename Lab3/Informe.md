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

| Característica   | Detalle                                                    |
| ---------------- | ---------------------------------------------------------- |
| Tipo             | Protocolo IGP de estado de enlace                          |
| Algoritmo        | Dijkstra (SPF - Shortest Path First)                       |
| Métrica          | Cost (costo basado en el ancho de banda)                   |
| Convergencia     | Rápida (actualiza cambios de red muy rápido)               |
| Jerarquía        | Soporta jerarquía de áreas (área backbone y otras)         |
| Autenticación    | Soporta autenticación para mayor seguridad                 |
| Multicast        | Usa multicast para actualizaciones (224.0.0.5 y 224.0.0.6) |
| Estándar abierto | No propietario, definido por el RFC 2328                   |

---

#### Clases de Red

La direccion IP esta codificada para permitir una asignación variable de bits para especificar la red y el computador, como se muestra en la siguiente imagen:

![Formatos de direcciones IP](/Lab3/Imagenes/ClasesRedes.PNG)

Este esquema de codificación proporciona flexibilidad al asignar las direcciones a los computadores y permite una mezcla de tamaños de red en un conjunto de redes. Existen tres clases principales de redes que se pueden asociar a las siguientes condiciones:

- **Clase A:** pocas redes, cada una con muchos computadores.
- **Clase B:** un número medio de redes, cada una con un número medio de computadores.
- **Clase C:** muchas redes, cada una con pocos computadores.

| Clase | Primer octeto (rango) | Bits de red | Bits de host | Número de redes          | Hosts por red (sin contar 0 y 255) | Ejemplo     |
| ----- | --------------------- | ----------- | ------------ | ------------------------ | ---------------------------------- | ----------- |
| A     | 0 - 127               | 8           | 24           | 128 (solo 1-126)         | ~16 millones                       | 10.0.0.1    |
| B     | 128 - 191             | 16          | 16           | ~16,000                  | ~65,000                            | 172.16.0.1  |
| C     | 192 - 223             | 24          | 8            | ~2 millones              | 254                                | 192.168.1.1 |
| D     | 224 - 239             | -           | -            | Multicast                | No para host                       | 224.0.0.1   |
| E     | 240 - 255             | -           | -            | Reservada (experimentos) | -                                  | 240.0.0.1   |

---

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

##### 4. Algoritmo A\* (A-star)

Este algoritmo es una modificacion del algoritmo de Dijkstra que incorpora heurísticas para mejorar el rendimiento en ciertos escenarios, como la navegacion de mapas.

#### Comparacion de los Algoritmos:

| Algoritmo      | Mejor para                                            | Limitaciones                      | Complejidad Temporal     |
| -------------- | ----------------------------------------------------- | --------------------------------- | ------------------------ |
| Dijkstra       | Grafos sin pesos negativos, rutas más rápidas         | No funciona con pesos negativos   | O((V + E) \* log(V))     |
| Bellman-Ford   | Grafos con pesos negativos, detecta ciclos negativos  | Más lento que Dijkstra            | O(V \* E)                |
| Floyd-Warshall | Todos los pares de nodos, grafos completos            | Muy lento para grafos grandes     | O(V³)                    |
| A\*            | Búsqueda eficiente en mapas o rutas (con heurísticas) | Depende de una heurística precisa | Depende de la heurística |

---

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

#### Segmentación de redes clase B para hosts

- **Red principal:** `172.16.0.0/16` (clase B).
- **Subredes /24 para hosts:**
  - **Subred S1 (H1, H2, H3):** `172.16.0.0/24`.
  - **Subred H4 (R4):** `172.16.1.0/24`.
  - **Subred H5 (R5):** `172.16.2.0/24`.

---

#### Redes clase C para enlaces entre routers

| **Enlace** | **Red asignada** | **Router A (IP)** | **Router B (IP)** |
| ---------- | ---------------- | ----------------- | ----------------- |
| **R1-R2**  | 192.168.1.0/24   | R1: 192.168.1.1   | R2: 192.168.1.2   |
| **R1-R3**  | 192.168.2.0/24   | R1: 192.168.2.1   | R3: 192.168.2.2   |
| **R2-R3**  | 192.168.3.0/24   | R2: 192.168.3.1   | R3: 192.168.3.2   |
| **R3-R4**  | 192.168.4.0/24   | R3: 192.168.4.1   | R4: 192.168.4.2   |
| **R3-R5**  | 192.168.5.0/24   | R3: 192.168.5.1   | R5: 192.168.5.2   |
| **R4-R5**  | 192.168.6.0/24   | R4: 192.168.6.1   | R5: 192.168.6.2   |

---

#### Tabla de direccionamiento completa

| **Dispositivo** | **Interfaz**      | **Dirección IP** | **Máscara**     | **Descripción**              |
| --------------- | ----------------- | ---------------- | --------------- | ---------------------------- |
| **R1**          | Loopback          | 10.0.0.1         | 255.255.255.255 | Loopback (administración)    |
| R1              | Enlace R1-R2      | 192.168.1.1      | 255.255.255.0   | Conexión a R2                |
| R1              | Enlace R1-R3      | 192.168.2.1      | 255.255.255.0   | Conexión a R3                |
| **R2**          | Enlace R1-R2      | 192.168.1.2      | 255.255.255.0   | Conexión a R1                |
| R2              | Enlace R2-R3      | 192.168.3.1      | 255.255.255.0   | Conexión a R3                |
| R2              | Interfaz LAN (S1) | 172.16.0.1       | 255.255.255.0   | Gateway para H1, H2, H3      |
| **R3**          | Enlace R1-R3      | 192.168.2.2      | 255.255.255.0   | Conexión a R1                |
| R3              | Enlace R2-R3      | 192.168.3.2      | 255.255.255.0   | Conexión a R2                |
| R3              | Enlace R3-R4      | 192.168.4.1      | 255.255.255.0   | Conexión a R4                |
| R3              | Enlace R3-R5      | 192.168.5.1      | 255.255.255.0   | Conexión a R5                |
| **R4**          | Enlace R3-R4      | 192.168.4.2      | 255.255.255.0   | Conexión a R3                |
| R4              | Enlace R4-R5      | 192.168.6.1      | 255.255.255.0   | Conexión a R5                |
| R4              | Interfaz LAN (H4) | 172.16.1.1       | 255.255.255.0   | Gateway para H4              |
| **R5**          | Enlace R3-R5      | 192.168.5.2      | 255.255.255.0   | Conexión a R3                |
| R5              | Enlace R4-R5      | 192.168.6.2      | 255.255.255.0   | Conexión a R4                |
| R5              | Interfaz LAN (H5) | 172.16.2.1       | 255.255.255.0   | Gateway para H5              |
| **S1**          | VLAN 1            | 172.16.0.254     | 255.255.255.0   | Switch S1 (gestión)          |
| **H1**          | eth0              | 172.16.0.101     | 255.255.255.0   | Host 1 (gateway: 172.16.0.1) |
| **H2**          | eth0              | 172.16.0.102     | 255.255.255.0   | Host 2 (gateway: 172.16.0.1) |
| **H3**          | eth0              | 172.16.0.103     | 255.255.255.0   | Host 3 (gateway: 172.16.0.1) |
| **H4**          | eth0              | 172.16.1.2       | 255.255.255.0   | Host 4 (gateway: 172.16.1.1) |
| **H5**          | eth0              | 172.16.2.2       | 255.255.255.0   | Host 5 (gateway: 172.16.2.1) |

---

### 3. Configuracion de routers para que utilice el protocolo OSPF

Luego de configurar los routers para utilizar protocolo OSPF verificamos la conexion punto a punto entre los dispositivos enlazados:

#### Comprobar conectividad IP básica

De R1 a R2:

![alt text](/Lab3/Imagenes/PingR1-R2.png)

De R1 a R3:

![alt text](/Lab3/Imagenes/PingR1-R3.png)

De H1 a H5:

![alt text](/Lab3/Imagenes/PingH1-H5.png)

Si hacemos esto con todos los routers con sus respectivos vecinos deberia dar el mismo resultado

#### Verificar la vecindad OSPF

Verificamos la vecindad de R3:

![alt text](/Lab3/Imagenes/VecinosR3.png)

Si hacemos esto para todos los routers nos dara la misma informacion pero con sus respectivos vecinos de ese router

#### Revisar la tabla de enrutamiento

Las rutas OSPF aparecen con la letra O:
![alt text](/Lab3/Imagenes/TablaEnrutamientoR3.png)

Con el mismo codigo en los distintos routers apareceran las rutas OSPF

### 4. Identificación y Analisis de mensajes OSPF

#### Panel de Simulación

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

#### Detalle OSI del PDU recibido

![alt text](/Lab3/Imagenes/PDUInformation-OSIModel.png)

**Explicación por capas**

- **Layer 1**: el paquete llega a la interfaz `Serial0/0/0` de `Router4`.
- **Layer 2**: tramas HDLC (encapsulación serial).
- **Layer 3**: cabecera IP con:
  - **Src IP**: `192.168.4.1` (interfaz de `Router3`).
  - **Dest IP**: `224.0.0.5` (dirección multicast de vecinos OSPF).
- No hay capas superiores mostradas en esta vista OSI; el contenido OSPF se examina en “Inbound PDU Details”.

---

#### Campos del OSPF Hello

![alt text](/Lab3/Imagenes/OSPF-Hello.png)

| Campo                        | Valor ejemplo | Significado / Impacto                                             |
| ---------------------------- | ------------- | ----------------------------------------------------------------- |
| **VERSION NUM**              | 2             | Versión OSPF para IPv4.                                           |
| **TYPE**                     | 1             | Tipo de paquete (1 = Hello).                                      |
| **PACKET LENGTH**            | 48            | Longitud total en bytes.                                          |
| **ROUTER ID**                | 192.168.5.1   | Identificador único del emisor.                                   |
| **AREA ID**                  | 0.0.0.0       | Área OSPF (aquí, área 0).                                         |
| **CHECKSUM**                 | 0             | Suma de verificación (calculará un valor en redes reales).        |
| **AUTH TYPE**                | 0             | Tipo de autenticación (0 = sin auth).                             |
| **NETWORK MASK**             | 255.255.255.0 | Máscara de la subred del enlace punto-a-punto.                    |
| **HELLO INTERVAL**           | 10            | Frecuencia de envío de Hellos (debe coincidir en ambos extremos). |
| **ROUTER DEAD INTERVAL**     | 40            | Tiempo tras el cual se considera muerto al vecino (4× Hello).     |
| **OPTIONS**                  | 0             | Bits de capacidades (p.ej. soporte de redes stub/NSSA).           |
| **DESIGNATED ROUTER**        | 0.0.0.0       | En multiacceso, DR (aquí 0.0.0.0 porque es punto-a-punto).        |
| **BACKUP DESIGNATED ROUTER** | 0.0.0.0       | BDR en multiacceso (no aplica en punto-a-punto).                  |
| **NEIGHBOR**                 | 192.168.4.2   | Lista de Router IDs con los que ya se vio Hello (vecindad).       |

**Comentarios**

- Los temporizadores **Hello** y **Dead** deben coincidir en ambos routers para formar adyacencia.
- El **Router ID** no puede duplicarse en la misma área.
- El **Neighbor** listado confirma que `Router4` vio un Hello previo de `Router3` (ID `192.168.4.2`).

Con estas capturas explicadas demuestras:

1. Cómo se generan y envían los **HS** (Hello) en OSPF.
2. Qué información crítica transportan y cómo afecta a la formación de adyacencias.
3. Qué buscar (coherencia de temporizadores, área, IDs, máscara) para diagnosticar fallos de convergencia.
4. La ventaja de usar el modo **Simulation** de Packet Tracer para desglosar paso a paso cada PDU.

### 5 y 6.

#### Nota sobre la Configuración de Router IDs

Durante la configuración de OSPF, decidí modificar las Router IDs de los routers, asignándoles valores de acuerdo con su identificación en la red. Esto se realizó con el objetivo de facilitar la lectura y la identificación de los routers al revisar tablas de enrutamiento, bases de datos OSPF y cualquier otro diagnóstico relacionado con OSPF.

**¿Por qué modificar las Router IDs?**
Claridad en el diagnóstico y análisis:

Al utilizar Router IDs como 1.1.1.1, 2.2.2.2, 3.3.3.3, etc., se facilita la comprensión de los resultados al analizar las tablas de enrutamiento o los vecinos OSPF. Es mucho más sencillo identificar a qué router se refiere cada entrada cuando las ID son claras y sistemáticas.

Simplificación en la administración de la red:

Esta asignación lógica permite diferenciar rápidamente entre los distintos routers en los informes, las salidas de los comandos de verificación (show ip ospf neighbor, show ip ospf database, etc.), y en la configuración de áreas.

**Router IDs Asignados**:

- R1: 1.1.1.1
- R2: 2.2.2.2
- R3: 3.3.3.3
- R4: 4.4.4.4
- R5: 5.5.5.5

#### Configuración de Redes Directamente Conectadas

En esta sección se muestra la configuración de las redes conectadas directamente a cada router, que se han configurado para OSPF.

- Router 1 (R1)
  <br>
  ![R1-5a](/Lab3/Imagenes/r1-5a.png)

- Router 2 (R2)
  <br>
  ![R2-5a](/Lab3/Imagenes/r2-5a.png)

- Router 3 (R3)
  <br>
  ![R3-5a](/Lab3/Imagenes/r3-5a.png)

- Router 4 (R4)
  <br>
  ![R4-5a](/Lab3/Imagenes/r4-5a.png)

- Router 5 (R5)
  <br>
  ![R5-5a](/Lab3/Imagenes/r5-5a.png)

#### Base de Datos de Estado de Enlace (LSDB)

Las entradas de la Base de Datos de Estado de Enlace (LSDB) muestran las redes que OSPF ha aprendido y están disponibles en cada router.

- Router 1 (R1)
  <br>
  ![R1-5b](/Lab3/Imagenes/r1-5b.png)

- Router 2 (R2)
  <br>
  ![R2-5a](/Lab3/Imagenes/r2-5b.png)

- Router 3 (R3)
  <br>
  ![R3-5b](/Lab3/Imagenes/r3-5b.png)

- Router 4 (R4)
  <br>
  ![R4-5b](/Lab3/Imagenes/r4-5b.png)

- Router 5 (R5)
  <br>
  ![R5-5b](/Lab3/Imagenes/r5-5b.png)

Las redes conectadas directamente a cada router han sido anunciadas correctamente a través de OSPF.
Las entradas de la LSDB de cada router son consistentes con las configuraciones de red establecidas.
Los routers están correctamente configurados para operar en las áreas adecuadas (Área 0 = A y Área 1 = B).

### 7.

#### a)

Para verificar que R2 tiene una adyacencia con R1 y R3 y que OSPF está funcionando correctamente, debemos utilizar el siguiente comando:

- show ip ospf neighbor

![R2-neighbors](/Lab3/Imagenes/r2-7a.png)

Efectivamente se observa que tanto el R1 como el R3 aparecen en la tabla de vecinos OSPF de R2

- Neighbor ID: Este es el Router ID de los vecinos, que deberían ser 1.1.1.1 (R1) y 3.3.3.3 (R3) en este caso.
- State = FULL: Esto indica que la adyacencia OSPF está completamente establecida.
- Dead Time: El tiempo restante antes de que expire la adyacencia si no hay comunicación.
- Address: La dirección IP de cada vecino.
- Interface: La interfaz local de R2 utilizada para establecer la adyacencia.

#### b)

Para obtener información general sobre las operaciones de OSPF en R2, usamos el comando:

- show ip protocols

![R2-7b](/Lab3/Imagenes/r2-7b.png)

- Routing Protocol is "ospf 1": Confirma que OSPF está configurado con el proceso ID 1.

- Router ID 2.2.2.2: Es el Router ID de R2.

- Routing for Networks: Muestra las redes que R2 está anunciando y las áreas correspondientes previamente configuradas.

- Routing Information Sources: Los vecinos desde los cuales R2 está recibiendo rutas, junto con el tiempo de la última actualización.

### 8. Configuración de Costo

#### Trayectoria por defecto

Primero realizamos un tracert entre **H1** (172.16.0.101) y **H4** (172.16.1.2) para ver la trayectoria que calcula OSPF con los costos por defecto.

!["Tracerert previo a cambiar los costos"](/Lab3/Imagenes/tracerout-default.png)

Como se puede ver (y comparando con la tabla de direccionamiento), el recorrido es:

$$\text{H1} \rightarrowtail \text{R2} \rightarrow \text{R3} \rightarrow \text{R4} \rightarrowtail \text{H4}$$

#### Trayectoria modificada

Aumentando el costo de las conexiones R2-R3.

Cambiando la configuración de R2:

```console
Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface serial0/0/1
Router(config-if)#ip ospf cost 200
Router(config-if)#end
Router#
```

Se obtuvieron los siguientes resultados:

!["tracert-modificado"](/Lab3/Imagenes/tracert-modificado.png)

Como se puede observar, ahora la trayectoria es:

$$\text{H1}\rightarrowtail\text{R2}\rightarrow\text{R1}\rightarrow\text{R3}\rightarrow\text{R4}\rightarrowtail\text{H4}$$

### 9. Redistribuyendo una ruta OSPF predeterminada

#### a. Configuración de Loopback

Se configuró el Router1 para que tenga una dirección IP Loopback para simular un proveedor de internet.

```console
Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#ip route 0.0.0.0 0.0.0.0 Loopback0
%Default route without gateway, if not a point-to-point interface, may impact performance
Router(config)#end
Router#
```

#### b. Ruta estatica R1

Verificando la correcta instalación de la ruta estática con `show ip route static`:

```console
Router#show ip route static
S*   0.0.0.0/0 is directly connected, Loopback0

Router#
```

#### c. Incluyendo ruta predeterminada a actualizaciones OSPF

```console
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#router ospf 1
Router(config-router)#default-information originate
Router(config-router)#end
Router#
```

### 10. Impacto de caida de Interfaz

#### Interfaz R2-R1 (`Serial 0/0/0`)

1.  **Detección:** R2 y R1 detectan la caída del enlace.
2.  **Adyacencia:** R2 deja de recibir mensajes de R1 (y viceversa). La adyacencia OSPF entre ellos se rompe.
3.  **Actualización LSA:** Ambos routers (R1 y R2) originan un nuevo Router LSA (Type 1), indicando que el enlace entre ellos ya no existe o tiene un costo infinito.
4.  **Recálculo SPF:** Todos los routers en Area 1 (R1, R2, y R3 como ABR) reciben los LSAs, actualizan su LSDB y re-ejecutan el algoritmo SPF.
5.  **Nueva Ruta:** R2 pierde su ruta directa hacia R1. Si necesita alcanzar la red Loopback (o cualquier otra red solo alcanzable vía R1 desde R2), deberá enrutar el tráfico a través de su otro vecino OSPF. R1 también redirigirá el tráfico destinado a la LAN de R2 a través de R3.
6.  **ABR:** R3 (ABR) podría actualizar los Summary LSAs (Type 3) si las métricas hacia redes en otras áreas cambian debido a la nueva ruta.
7.  **Impacto:** Pérdida de la conexión directa R1-R2. El tráfico entre ellos y las redes detrás de ellos ahora debe pasar por R3.

#### Interfaz R2-R3 (`Serial 0/0/1`)

1.  **Detección y Adyacencia:** R2 y R3 detectan la caída y la adyacencia OSPF expira.
2.  **Actualización LSA:** R2 y R3 originan nuevos LSAs reflejando la pérdida del enlace R2-R3.
3.  **Recálculo SPF:** Todos los routers afectados re-ejecutan SPF.
4.  **Nueva Ruta:** R2 pierde su conexión directa con R3. Para alcanzar cualquier red LAN h4 o LAN h5, deberá ir a través de R1. R3 también perderá la ruta directa a la LAN de R2 y deberá pasar por R1.
5.  **Impacto:** Pérdida del enlace directo R2-R3. Todo el tráfico entre R2 y el resto de la red ahora debe obligatoriamente transitar por R1.

#### Interfaz R2-S1 (`GigabitEthernet 0/0`)

1.  **Detección:** R2 detecta la caída de su interfaz LAN.
2.  **Actualización LSA:** R2 origina un nuevo Router LSA (Type 1) indicando que la red ya no es alcanzable a través de él.
3.  **Recálculo SPF:** R1 y R3 (ABR) actualizan sus LSDBs y re-ejecutan SPF.
4.  **Nueva Ruta:** R1 y R3 eliminan la ruta hacia los Hosts vía R2.
5.  **Impacto:** Los hosts h1, h2, h3 quedan aislados del resto de la red OSPF, ya que R2 era su único gateway. Tanto R2 como ningún otro router tendrá una ruta válida hacia su red.

### 11.
