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

### 2. Construcción de Simulación de Red propuesta

### 3. Diferencias entre Simulador y Emulador
Distinguir entre **simuladores** y **emuladores** es importante, ya que cada herramienta cumple propósitos específicos en el diseño, análisis e implementación de infraestructuras de red.

**Simuladores de Redes**  

*Definición y Características:*  
_Un simulador de redes es una herramienta software que modela el comportamiento teórico de dispositivos, protocolos y topologías de red mediante algoritmos y representaciones abstractas._

 Su enfoque se centra en:
- **Abstracción funcional:** No utiliza implementaciones reales de sistemas operativos o firmware.  
- **Entornos controlados:** Permite probar escenarios bajo condiciones ideales o predefinidas.  
- **Bajo consumo de recursos:** Optimizado para ejecutarse en hardware estándar sin requerimientos elevados.  

***Casos de Uso***  
- Enseñanza de conceptos básicos de redes (ej: funcionamiento de switches, enrutamiento estático).  
- Pruebas de conectividad simple o validación de diseños teóricos.  
- Laboratorios académicos donde la prioridad es la comprensión conceptual.  

***Herramientas Representativas***  
- **Packet Tracer (Cisco):** Simula comandos básicos de dispositivos Cisco.
- **NetSim:** Utilizado para modelar protocolos de capas OSI y analizar tráfico.

---

**Emuladores de Redes**  

*Definición y Características:*  
_Un emulador de redes replica el funcionamiento real de dispositivos mediante la ejecución de imágenes binarias de sistemas operativos específicos (ej: Cisco IOS, VyOS)._

Sus aspectos clave incluyen:  
- **Alto realismo:** Permite configuraciones idénticas a las de hardware físico.  
- **Integración con infraestructuras reales:** Puede conectarse a dispositivos físicos o nubes públicas.  
- **Demanda de recursos:** Requiere hardware potente

***Casos de Uso***  
- Implementación de redes empresariales complejas 
- Pruebas de interoperabilidad entre dispositivos de múltiples fabricantes.  
- Preparación para certificaciones profesionales 

***Herramientas Representativas***  
- **GNS3:** Emula routers, switches y firewalls usando imágenes reales de Cisco, Juniper y otros vendors.  
- **CORE:** Herramienta que permite la emulación de redes informáticas en una o varias máquinas, aunqeu también puede conectarse a entornos de red reales.

---

**Tabla Comparativa**  

| **Aspecto**               | **Simulador**                          | **Emulador**                          |
|---------------------------|----------------------------------------|----------------------------------------|
| **Nivel de realismo**      | Modelos teóricos simplificados         | Réplica exacta de sistemas operativos  |
| **Recursos requeridos**    | Hardware básico                       | Hardware especializado (CPU/RAM alta)  |
| **Flexibilidad**           | Limitada a funciones preprogramadas   | Configuración granular y personalizada |
| **Entorno de aplicación** | Académico/Educativo                   | Profesional/Investigación avanzada     |
| **Ejemplos**              | Packet Tracer, NetSim                 | GNS3, EVE-NG, CORE                     |

---

La elección entre simuladores y emuladores depende directamente de los objetivos del proyecto. Mientras los simuladores ofrecen un entorno accesible para la asimilación de conceptos fundamentales, los emuladores brindan la precisión técnica necesaria para escenarios realistas y profesionales. En el contexto de la Ingeniería en Computación, dominar ambas herramientas permite abordar desde problemas pedagógicos hasta desafíos de implementación en entornos productivos, consolidando así una formación integral en redes de computadoras.  

### 4. Evaluar conectividad entre 3 host IPv4

### 5. Evaluar conectividad entre 3 host IPv6

### 6. Analisis de trafico ICMP entre 2 redes

### 7. Analisis de trafico ICMPv3 entre 2 redes

## Parte II - Manejo de equipamiento físico, recuperación de contraseñas de equipos de red y establecimiento de red y análisis de tráfico.

### 1. Caracteristicas principales del Switch

### 2. Checklist de procedimientos

### 3. Experiencia presencial
# Parte II - Punto 3: Experiencia presencial 🌐  

## **Resumen de la experiencia práctica**  
Durante la interacción con el equipo físico y la implementación de la red, se observaron los siguientes aspectos clave:  

---
 **1. Interacción con el hardware**  
- **Conexión física:**  
  - Los puertos FastEthernet del switch se etiquetaron claramente, facilitando la conexión de las PCs.  
  - Se verificó el estado de los LEDs de los puertos para confirmar actividad (link/actividad).  
- **Desafíos:**  
  - Inicialmente, el puerto de consola no respondía debido a un cable RJ-45 dañado. Se resolvió reemplazándolo.  
  - Dificultad para identificar el puerto COM correcto en Windows (solución: revisar el Administrador de dispositivos).  

---

 **2. Configuración del switch**  
- **Acceso por consola:**  
  - Uso de PuTTY con parámetros seriales (`9600 baudios, 8N1`) fue crítico para acceder al CLI del switch.  
  - El prompt `Switch>` apareció solo después de reiniciar el equipo (posible error de firmware inicial).  
- **Cambio de contraseñas:**  
  - La configuración de `enable secret` aseguró el acceso privilegiado, pero se olvidó guardar con `copy running-config startup-config` en el primer intento, perdiendo los cambios.  

---

**3. Comunicación entre PCs**  
- **Configuración IP estática:**  
  - Tanto en Windows como en Linux funcionó correctamente la configuracion manual de IP.  
- **Pruebas de conectividad:**  
  - El primer `ping` entre PC1 y PC2 falló por firewall de Windows bloqueando ICMP. Se resolvió desactivando temporalmente el firewall.  
  - Se observó que el TTL variaba según el SO: Windows (128) vs Linux (64).  

---

### **4. Port Mirroring y análisis de tráfico**  
- **Configuración SPAN:**  
  - Wireshark mostró correctamente paquetes ARP (para resolución de MAC) e ICMP tras ajustar los filtros.  
---

### **5. Lecciones aprendidas**  
1. **Verificación física:**  
   - Chequear cables y LEDs antes de asumir errores de configuración.  
2. **Documentación:**  
   - Anotar contraseñas nuevas inmediatamente (¡el "enable secret" no se puede recuperar fácilmente!).  
3. **Herramientas de diagnóstico:**  
   - Comandos como `show interfaces status` en el switch y `arp -a` en las PCs fueron esenciales para resolver problemas.  

---

## **Conclusión**  
La experiencia presencial reforzó la importancia de:  
- La **metodología ordenada** (seguir checklists).  
- El **análisis de fallas en capas** (física → enlace → red).  
- La **integración entre hardware y software**, donde pequeños detalles (ej: parámetros de PuTTY) impactan en resultados globales.  
