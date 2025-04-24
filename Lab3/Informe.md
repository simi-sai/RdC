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


## INTRODUCCION TEORICA
### OSPF
El protocolo del primer camino mas corto posible (OSPF, Open Shortest Path First) se usa de forma generalizada como protocolo de enrutamiento interior en redes TPC/IP. OSPF calcula una ruta a traves de una interconexión de redes que suponga el menor coste de a cuerdo a una métrica de coste configurable por usuario. El usuario puede configurar el coste para que exprese una función del retardo, velocidad de transmisión, el coste económico u otros factores. OSFP es capaz de equilibrar las cargas entre múltiples caminos de igual coste.

#### Resumen de Caracteristicas de OSPF

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
### Clases de Red
La direccion IP esta codigicada para permitir una asignación variable de bits para especificar la red y el computador, como se muestra en la siguiente imagen: 

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
### Algoritmos de Shortest Path
Los algoritmos de camino mas corto son técnicas que permiten encontrar el camino más corto entre un nodo de inicio y uno de destino dentro de un grafo. Algunos algoritmos son:

#### 1. Algoritmo de Dijkstra
Uno de los algoritmos mas conocidos y utilizados par aencontrar el camino mas corto en grafos con pesos NO negativos. Funciona para grafos dirigidos y no dirigidos y puede ser implementado usando una cola de prioridad para optimizar el rendimiento. Es **Greedy**, es decir, toma la desicion óptima en cada paso basándose en la información local.

- Ventaja: Muy eficiente para grafos dispersos (pocos nodos y aristas).
- Desventaja: No puede manejar grafos con Pesos negativos.

#### 2. Algoritmo de Bellman-Ford
Este algoritmo es util cuando el grafo tiene pesos negativos en las aristas. Es mas lento que Dijkstra, especialmente en grafos grandes.

#### 3. Algoritmo de Floyd-Warshall
A diferencia de Dijkstra y Bellman-Ford, calcula las distancias mas cortas entre los pares nodos en el grafo. Es muy util cuando se necesitan todas las rutas mas cortas de un grafo completo. Es muy lento para grafos grandes

#### 4. Algoritmo A* (A-star)
Este algoritmo es una modificacion del algoritmo de Dijkstra que incorpora heurísticas para mejorar el rendimiento en ciertos escenarios, como la navegacion de mapas.

#### Comparacion de los Algoritmos:
| Algoritmo      | Mejor para                                           | Limitaciones                                 | Complejidad Temporal       |
|----------------|------------------------------------------------------|----------------------------------------------|----------------------------|
| Dijkstra       | Grafos sin pesos negativos, rutas más rápidas        | No funciona con pesos negativos              | O((V + E) * log(V))        |
| Bellman-Ford   | Grafos con pesos negativos, detecta ciclos negativos | Más lento que Dijkstra                       | O(V * E)                   |
| Floyd-Warshall | Todos los pares de nodos, grafos completos           | Muy lento para grafos grandes                | O(V³)                      |
| A*             | Búsqueda eficiente en mapas o rutas (con heurísticas) | Depende de una heurística precisa            | Depende de la heurística   |
----

### Aplicación de grafos en OSPF
Una red de computadoras puede modelarse naturalmente como un grafo:
- **Nodos**: Representan dispositivos como routers, switches o hosts.
- **Aristas**: Representan las conexiones fisicas o logicas entre los dispositivos.
- **Pesos en las aristas**: Representan costos de transmision, como ancho de banda, latencia, carga de enlace o costo arbitrario asignado por el administrador de Red.

OSPF es un protocolo que utiliza la teoria de grafos para encontrar los caminos mas cortos desde un router hasta todos los destinos posibles en la red. 

#### Construccion del grafo

Cada router OSPF recopila informacion sobre todos los enlaces a los que esta conectado y distribuye esa informacion a traves de Link-State Advertisements (LSAs). Con esto:

- Todos los routers construyen un mapa identico de la red, que es un grafo completo de todos los routers y enlaces.
- Cada nodo tiene una copia del grafo, donde conoce la topologia completa.

#### Aplicacion del algoritmo de Dijkstra
Una vez que el router tiene el grafo de la red, utiliza el algoritmo de Dijkstra para calcular la mejor ruta a cada destino. Esto construye la tabla de enrutamiento, que indica el mejor siguiente salgo (next-hop) hacia cada red. 

Cuando cambia el estado de un enlace, se envia un nuevo LSA y Todos los routers actualizan su grafo y recalculan sus rutas usando este algoritmo.

## Esquema de direccionamiento IP
Red propuesta:
![Red](/Lab3/Imagenes/Red.PNG)

Vamos a dividir la red en subredes logicas.
#### Asignacion de Subredes
| Enlace   | Red asignada     | Router A IP         | Router B IP         |
|----------|------------------|---------------------|---------------------|
| R1 - R2  | 192.168.1.0/30   | R1: 192.168.1.1     | R2: 192.168.1.2     |
| R1 - R3  | 192.168.1.4/30   | R1: 192.168.1.5     | R3: 192.168.1.6     |
| R2 - R3  | 192.168.1.8/30   | R2: 192.168.1.9     | R3: 192.168.1.10    |
| R3 - R4  | 192.168.1.12/30  | R3: 192.168.1.13    | R4: 192.168.1.14    |
| R3 - R5  | 192.168.1.16/30  | R3: 192.168.1.17    | R5: 192.168.1.18    |
| R4 - R5  | 192.168.1.20/30  | R4: 192.168.1.21    | R5: 192.168.1.22    |

#### Subred del Switch S1 con los hosts 1,2,3
Vamos a usar una red clase B para esta LAN:
| Red            | Dispositivo | IP            |
|----------------|-------------|---------------|
| 172.16.0.0/24  | H1          | 172.16.0.101  |
|                | H2          | 172.16.0.102  |
|                | H3          | 172.16.0.103  |
|                | R2 (gateway)| 172.16.0.1    |

----
#### Host h4 conectado directo a R4 - Clase B
| Red            | Dispositivo | IP            |
|----------------|-------------|---------------|
| 172.16.1.0/30  | H4          | 172.16.1.2    |
|                | R4          | 172.16.1.1    |

----
#### Host h5 conectado directo a R5 - Clase B
| Red            | Dispositivo | IP            |
|----------------|-------------|---------------|
| 172.16.2.0/30  | H5          | 172.16.2.2    |
|                | R5          | 172.16.2.1    |

#### Tabla de direccionamiento completa
| Dispositivo | Interfaz               | Dirección IP     | Máscara de Subred   | Descripción                                   |
|--------------|------------------------|------------------|---------------------|-----------------------------------------------|
| R1           | Loopback               | 192.168.1.1      | 255.255.255.255     | Loopback (Dirección de loopback)              |
| R1           | Interfaz R1-R2         | 192.168.1.1      | 255.255.255.252     | Enlace con R2                                 |
| R1           | Interfaz R1-R3         | 192.168.1.5      | 255.255.255.252     | Enlace con R3                                 |
| R2           | Interfaz R1-R2         | 192.168.1.2      | 255.255.255.252     | Enlace con R1                                 |
| R2           | Interfaz R2-R3         | 192.168.1.9      | 255.255.255.252     | Enlace con R3                                 |
| R3           | Interfaz R1-R3         | 192.168.1.6      | 255.255.255.252     | Enlace con R1                                 |
| R3           | Interfaz R2-R3         | 192.168.1.10     | 255.255.255.252     | Enlace con R2                                 |
| R3           | Interfaz R3-R4         | 192.168.1.13     | 255.255.255.252     | Enlace con R4                                 |
| R3           | Interfaz R3-R5         | 192.168.1.17     | 255.255.255.252     | Enlace con R5                                 |
| R4           | Interfaz R3-R4         | 192.168.1.14     | 255.255.255.252     | Enlace con R3                                 |
| R4           | Interfaz R4-R5         | 192.168.1.21     | 255.255.255.252     | Enlace con R5                                 |
| R5           | Interfaz R3-R5         | 192.168.1.18     | 255.255.255.252     | Enlace con R3                                 |
| R5           | Interfaz R4-R5         | 192.168.1.22     | 255.255.255.252     | Enlace con R4                                 |
| S1           | Interfaz de Switch     | 172.16.0.1       | 255.255.255.0       | Gateway para los hosts (H1, H2, H3)          |
| H1           | Interfaz de Host       | 172.16.0.101     | 255.255.255.0       | Host 1, conectado a S1                       |
| H2           | Interfaz de Host       | 172.16.0.102     | 255.255.255.0       | Host 2, conectado a S1                       |
| H3           | Interfaz de Host       | 172.16.0.103     | 255.255.255.0       | Host 3, conectado a S1                       |
| H4           | Interfaz de Host       | 172.16.1.2       | 255.255.255.252     | Host 4, conectado a R4                       |
| R4           | Interfaz de Host       | 172.16.1.1       | 255.255.255.252     | Gateway para H4                              |
| H5           | Interfaz de Host       | 172.16.2.2       | 255.255.255.252     | Host 5, conectado a R5                       |
| R5           | Interfaz de Host       | 172.16.2.1       | 255.255.255.252     | Gateway para H5                              |

Se usan distintas redes para cada par de routers ya que los protocolos como OSPF necesitan saber que redes estan disponibles y por donde se llega a cada una. Si todo esta en la misma red, no hay forma de diferenciarlas, y el protocolo no puede calcular rutas correctas.