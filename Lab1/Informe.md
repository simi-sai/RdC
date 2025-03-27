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

**Basado en datasheet oficial**
* **Arquitectura:**
    - 24 puertos Ethernet 10/100BASE-TX.
    - 2 puertos Gigabit Ethernet uplink.
    - Backplane de 8.8 Gbps.
    - Memoria Flash: 8MB (para IOS).
    - RAM: 32 MB
* **Protocolos soportados:**
    - Spanning Tree Protocol (802.1D).
    - VLANs (802.1Q).
    - SNMP v2c/v3.
    - CDP (Cisco Discovery Protocol).
* **Consola:**
    - Puerto RJ-45 (9600 Baudios, 8N1, flujo de datos none).
    - Acceso mediante cable serie rollover (Cisco PINOUT: RJ-45 a DB-9).

### 2. Checklist de procedimientos
**a. Conexion por consula con PUTTY**
1. Hardware
    - Conectar el puerto de consola con un puerto usb a la PC1 usando un cable serie RJ-45 y un adaptador USB-Serie.

2. Configuracion de PUTTY
    - Tipo de conexion: Serial
    - puerto COM: Identificar en Administrador de dispositivos(windows).
    - Velocidad: **9600 baudios**.
    - Parámetros: 8bits de datos, 1 bit de parada, sin paridad, control de flujo: None.

3. Acceso:
    - Encender el switch y presionar Enter en PC1 para obtener prompt `Switch>`

**b. Modificacion de contraseñas.**
1. cambiar contraseña de modo privilegiado.
~~~
Switch> enable
Switch# configure terminal
Switch(config)# enable secret [clave_nueva]
Switch(config)# exit
~~~
2. Configurar contraseña para acceso por consola
~~~
Switch(config)# line console 0
Switch(config-line)# password ClaveConsola456
Switch(config-line)# login
Switch(config-line)# exit
~~~
3. Guardar la configuración
~~~
Switch(config)# copy running-config startup-config
~~~
**c. Configuracion y conexion de red basica.**
1. Conexion de PCs al Switch
    - **PC1**: Puerto FastEthernet0/1.
    - **PC2**: Puerto FastEthernet0/2.
    - **PC3 (para monitoreo)**: Puerto FastEthernet0/3.
2. Configuracion de las IPs en las PCs
    - En windows:
    ~~~
    #PC1:
    netsh interface ip set adress name="Ethernet" static 192.168.1.10 255.255.255.0

    #PC2:
    netsh interface ip set adress name="Ethernet" static 192.168.1.11 255.255.255.0
    ~~~
    - En linux:
    ~~~
    #PC1:
    sudo ip addr add 192.168.1.10/24 dev eth0

    #PC2:
    sudo ip addr add 192.168.1.11/24 dev eth0
    ~~~
3. Prueba de conectividad
~~~
#Desde PC1:
ping 192.168.1.11 

#PC2:
ping 192.168.1.10
~~~
**d. Configuracion de Port Mirroring (SPAN) con capturas de trafico**
1. Habilitar SPAN en el Switch
~~~
Switch# configure terminal
Switch(config)# monitor session 1 source interface FastEthernet0/1 both
Switch(config)# monitor session 1 destination interface FastEthernet0/3
Switch(config)# end
~~~
2. Configurar Wireshark en PC3
1. Abrir Wireshark y seleccionar interfaz de red.
2. Aplicar filtros:
    - `arp` para ver solicitudes/respuestas ARP.
    - `icmp` para trafico de ping
3. Ejecutar el comando `ping` en PC1 o PC2 para observar la captura del trafico.
### 3. Experiencia presencial
