# Trabajo Practico N°4: Protocolo de Puerta de Enlace Fronteriza (BGP) y Sistemas Autónomos (AS)

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

### Parte I - Integración de Conceptos, Actividades Online e Investigación

#### Actividad 1:

**a. ¿Qué es un Autonomous System (AS)?**

Un Sistema Autónomo (AS) es un conjunto de redes IP y routers bajo el control de una única entidad administrativa que presenta una política de enrutamiento común al exterior. Cada AS es identificado por un número único conocido como Número de Sistema Autónomo (ASN).

**b. ¿Qué es un Autonomous System Number (ASN) y cómo está conformado?**

Un Autonomous System Number (ASN) es un número único asignado a cada Sistema Autónomo para identificarlo en el contexto del enrutamiento BGP. 

Los ASN pueden ser de `16 bits` o de `32 bits`. Los ASN de `16 bits` están en el rango de 1 a 65534, mientras que los ASN de `32 bits` están en el rango de 131072 a 4294967294. Estos números se presentan en el formato AS(número). Por ejemplo, el ASN de Cloudflare es `AS13335`. Según algunas estimaciones, hay más de 90,000 ASN en uso en todo el mundo.

**c. Buscar 3 ejemplos de ASN de empresas, universidades u organizaciónes**

1. `AS15169` - **Google LLC**: Este ASN es utilizado por Google para sus servicios de búsqueda, publicidad y otros productos en línea.
2. `AS27790` - **Universidad Nacional de Córdoba (UNC)**: Este ASN es utilizado por la universidad para sus redes y servicios académicos.
3. `AS8659` - **United Nations International Computing Centre (UNICC)**: Este ASN es utilizado por el Centro Internacional de Informática de las Naciones Unidas para sus operaciones y servicios tecnológicos.

**d. ASN de mi conexión Actual**

Mi conexión actual utiliza el ASN **AS11664**, que pertenece a **Techtel LMDS Comunicaciones Interactivas S.A.** que corresponde a la empresa de telecomunicaciones **CLARO** en Argentina. Este ASN es utilizado para proporcionar servicios de internet y telecomunicaciones a clientes residenciales y empresariales.

Información adicional sobre el ASN de mi conexión:
- **Niveles de Tráfico**: 1-5 Tbps.
- **Protocolos Soportados**: Unicast IPv4, Multicast, IPv6.
- **Prefijos IPv4**: 3000.
- **Prefijos IPv6**: 600.

>[!NOTE]
>Para mas información sobre el ASN de mi conexión, referirse al archivo `Lab4/Archivos/AS11664.json`.

#### Actividad 2:

**a. ¿Qué es el Border Gateway Protocol (BGP)?**

El Protocolo de Puerta de Enlace Fronteriza (BGP) es el protocolo de enrutamiento utilizado para intercambiar información de enrutamiento entre Sistemas Autónomos (AS) en Internet. BGP es un protocolo de vector de ruta que utiliza políticas de enrutamiento para determinar la mejor ruta para el tráfico entre diferentes AS.

**b. Resumir el funcionamiento del BGP a través de sus procedimientos funcionales: adquisición de vecino, detección de vecino alcanzable, detección de red alcanzable. Explicar tipos de mensajes y formato de paquetes en BGP.**

El funcionamiento de BGP se basa en varios procedimientos funcionales clave:

1. **Adquisición de Vecino**: BGP establece conexiones entre routers vecinos (peers) para intercambiar información de enrutamiento. Esto se realiza a través de la apertura de una sesión TCP en el puerto 179.
2. **Detección de Vecino Alcanzable**: Una vez que se establece la conexión, los routers intercambian mensajes de apertura (OPEN) para negociar parámetros de la sesión, como el ASN del vecino y las capacidades del protocolo.
3. **Detección de Red Alcanzable**: Los routers intercambian mensajes de actualización (UPDATE) que contienen información sobre las rutas disponibles y las políticas de enrutamiento. Estos mensajes incluyen prefijos IP, atributos de ruta y otros datos necesarios para determinar la mejor ruta.

Tipos de Mensajes y Formato de Paquetes en BGP:

Todos los mensajes BGP comparten un encabezado común y tienen una longitud máxima de 4096 bytes.

Formato del Encabezado Común de BGP (19 bytes):

| Campo	| Longitud (octetos) | Descripción |
|---|---|---|
| Marker | 16 | Se utiliza para sincronización y     autenticación. Si no hay autenticación, se llena con todos los bits a 1. |
| Length | 2 | Longitud total del mensaje BGP (incluyendo el encabezado), en octetos. Rango: 19 a 4096. |
| Type| 1 | Tipo de mensaje BGP (1: OPEN, 2: UPDATE, 3: NOTIFICATION, 4: KEEPALIVE, 5: ROUTE-REFRESH). |

Tipos de Mensaje BGP:

- **OPEN**: Establece una sesión BGP entre vecinos y negocia parámetros.
- **UPDATE**: Anuncia nuevas rutas o retira rutas existentes.
- **NOTIFICATION**: Informa sobre errores o condiciones especiales en la sesión BGP.
- **KEEPALIVE**: Mantiene viva la sesión BGP enviando mensajes periódicos para evitar el cierre de la conexión.
- **ROUTE-REFRESH**: Solicita al vecino que reenvíe sus rutas actuales sin cerrar la sesión.

**c. Explicar la diferencia entre BGP Externo (eBGP) y BGP Interno (iBGP) en función de la información que se intercambia dentro de un AS. En el siguiente ejemplo ¿Cuál(es) AS son de tránsito?**

<div class="image", align="center">
    <img src="./Imagenes/Ejemplo2c.png" alt="BGP Example" width="600">
</div>

En funcion de la información que se intercambia dentro de un Sistema Autónomo (AS), la diferencia entre BGP externo e interno es la siguiente:

- **BGP Externo (eBGP)**: Se utiliza para intercambiar información de enrutamiento entre diferentes Sistemas Autónomos. En el ejemplo, los AS1, AS2 y AS3 están intercambiando información de enrutamiento entre ellos a través de eBGP.
- **BGP Interno (iBGP)**: Se utiliza para intercambiar información de enrutamiento dentro de un mismo Sistema Autónomo. En el ejemplo, los routers dentro del AS2 están intercambiando información de enrutamiento a través de iBGP.

En el ejemplo proporcionado, los AS que actúan como tránsito es **AS2**, actúa como tránsito para el tráfico entre **AS1** y **AS3**.

**d. Buscar las conexiones del AS en mi conexión actual. ¿Cuántas conexiones eBGP tiene mi AS?, incluir un gráfico de los AS a uno o dos grados de separación.**

Mi conexión actual utiliza el ASN **AS11664**.

<div class="image", align="center">
    <img src="./Imagenes/AS11664-BGP.png" alt="AS Connections" width="600">
</div>

Al buscar las conexiones eBGP de este AS, encontramos que tiene varias conexiones con otros AS, estas son (separadas por grados de separación):

- 1 grado: `AS19037`, `AS3257`, `AS1299`, `AS6762`, `AS6939`.
- 2 grados: `AS174`, `AS5511`, `AS6830`, `AS2497`, `AS2914`, `AS3356`, `AS6461`, `AS7018`, `AS6453`, `AS5391`.
- 3 grados: `AS3549` y `AS209`.

**e. Buscar las conexiones del AS conectándome a alguna red distinta a la del punto anterior (puede ser 4G/5G de mi teléfono, alguna red en la facultad, etc.). ¿Qué diferencias/similitudes puedo identificar?**

Usando la conexión de mi teléfono móvil (4G/5G), encontramos que el ASN utilizado es **AS7303** (utilizando la página web https://bgp.he.net/), que pertenece a **Telecom Argentina S.A.** empresa que fue comprada por Personal. 

<div class="image", align="center">
    <img src="./Imagenes/AS7303-BGP.png" alt="AS Connections" width="600">
</div>

Conexiones eBGP de **AS11664**:

`AS19037`, `AS3257`, `AS1299`, `AS6762`, `AS6939`, `AS174`, `AS5511`, `AS6830`, `AS2497`, `AS2914`, `AS3356`, `AS6461`, `AS7018`, `AS6453`, `AS5391`, `AS3549`, `AS209`.

Conexiones eBGP de **AS7303**:

`AS1299`, `AS6939`, `AS3356`, `AS3257`, `AS6762`, `AS22927`, `AS12956`, `AS6453`, `AS5511`, `AS2914`, `AS3549`, `AS7018`, `AS6461`, `AS174`, `AS209`, `AS2497`.

| Conexiones Iguales | Conexiones Distintas |
|---------------------|-----------------------|
| `AS5511`, `AS209`, `AS174`, `AS1299`, `AS6762`, `AS7018`, `AS3356`, `AS3257`, `AS6939`, `AS2497`, `AS2914`, `AS3549`, `AS6461`, `AS6453`. | - **AS11664** tiene `AS19037`, `AS6830` y `AS5391`. 
| |- **AS7303** tiene  `AS22927` y `AS12956`. |

Diferencias/Similitudes:

- Ambas conexiones tienen una gran cantidad de conexiones eBGP con otros AS, lo que indica una buena conectividad y redundancia en la red.
- Ambas conexiones comparten varios AS comunes, lo que sugiere que están interconectadas con los mismos proveedores de servicios de Internet y redes.
- Ambas conexiones tienen unas cuantas conexiones únicas, lo que indica que cada AS tiene sus propias relaciones y acuerdos de peering con otros AS.

**f. Investigar algún problema en enrutamiento BGP que haya tenido un impacto en servicios de red a nivel nacional/internacional. Elaborar un resumen de las causas y las consecuencias.**

Noticia: https://www.xataka.com/servicios/que-protocolo-bgp-que-provoco-que-whatsapp-facebook-e-instagram-desaparecieran-internet-durante-horas

El 4 de octubre de 2021, Facebook, WhatsApp e Instagram sufrieron una interrupción masiva que afectó a millones de usuarios en todo el mundo. 

La causa principal del problema fue un error en la configuración del Protocolo de Puerta de Enlace Fronteriza (BGP), que es el protocolo utilizado para enrutar el tráfico de Internet entre diferentes Sistemas Autónomos (AS). El error ocurrió cuando Facebook realizó cambios en su infraestructura de red, lo que provocó que sus servidores BGP anunciaran rutas incorrectas. Esto llevó a que los routers de otros proveedores de servicios de Internet (ISP) eliminaran las rutas hacia los servidores de Facebook, lo que resultó en la inaccesibilidad de sus servicios.

Las consecuencias de este error fueron significativas:

- **Interrupción de Servicios**: Los usuarios de Facebook, WhatsApp e Instagram no pudieron acceder a sus cuentas ni enviar mensajes durante varias horas.
- **Impacto Económico**: Se estima que la interrupción costó a Facebook millones de dólares en ingresos publicitarios y afectó a empresas que dependen de estas plataformas para sus operaciones.
- **Confusión Generalizada**: La interrupción generó confusión y preocupación entre los usuarios, quienes no sabían si el problema era local o global.

### Parte II - Simulaciónes y Análisis