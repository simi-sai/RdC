# Trabajo Practico N°1

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

**{FECHA}**

## Parte I - Configuración y Análisis de tráfico IPv4/IPv6

### 1. Marco Teórico Resumido

### Protocolos IPv4 e IPv6
El protocolo IPv4 ha sido la base de las redes durante decadas, utilizando direcciones de 32 bits (como 192.168.1.10) para identificar dispositivos. Sin embargo, su limitado espacio de direcciones la dependencia de tecnologias como NAT han impulsado la adopcion de IPv6, que emplea direcciones de 128 bits (por ejemplo, 2001:aaaa:bbbb:1::10). Esta notacion hexadecimal no solo resuelve agotamiento de direcciones, sino que tambien introduce mejoras en seguridad, autoconfiguracion y eficiencia en el enrutamiento.

### Mecanismos de Reloucion de Direcciones
En IPv4, el protocolo ARP(Adress Resolution Protocol) se encarga de traducir direcciones IP a direcciones MAC. Por ejemplo, cuando un host necesita comunicarse con otro en la misma red, envia una solicitud ARP para obtener la direccion fisica de destino. En cambio, IPv6 utiliza NDP (Neighbor Discovery Protocol), que no solo reemplaza a ARP, sino que tambien incorpora funciones avanzadas como la deteccion de routers vecinos y la autoconfiguracion de direcciones. NDP opera mediante mensajes como Neighbot Solicitation y Neighbot Advertisement, que se transmiten de manera mas eficiente usando multicast en lugar de broadcast.

### ICMP y Diagnostico de Red
Tanto IPv4 como IPv6 emplean versiones del protocolo ICMP para tareas de diagnostico y manejo de errores. En IPv4, el comando ping utiliza ICMPv4 para verificar la conectividad entre hosts. mientras que en IPv6 se usa ping6 con ICMPv6. Estos protocolos son escenciales para identificar problemas de red, como paquetes perdidos o rutas inaccesibles.

### Dual Stack y Asignacion Dinamica de Direcciones
La tecnologia dual stack permite que los dispositivos soporten ambos protocolos en paralelo, asignando una direccion IPv4 y otra IPv6 a cada interfaz de red. Esto facilita la transmision gradual hacia IPv6 sin interrumpir servicios existentes. Ademas, la asignacion dinamica de direcciones puede realizarse mediante DHCP en IPv4 o combinando DHCPv6 y SLAAC(Stateless Autoconfiguration) eb IPv6 lo que simplifica la administracion de redes grandes.

### 2. Construcción de Simulación de Red propuesta

### 3. Diferencias entre Simulador y Emulador

### 4. Evaluar conectividad entre 3 host IPv4

### 5. Evaluar conectividad entre 3 host IPv6

### 6. Analisis de trafico ICMP entre 2 redes

### 7. Analisis de trafico ICMPv3 entre 2 redes

## Parte II - Manejo de equipamiento físico, recuperación de contraseñas de equipos de red y establecimiento de red y análisis de tráfico.

### 1. Caracteristicas principales del Switch

### 2. Checklist de procedimientos

### 3. Experiencia presencial
