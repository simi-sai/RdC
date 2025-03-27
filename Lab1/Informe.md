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
