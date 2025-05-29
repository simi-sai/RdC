# Trabajo Practico N°4: Ruteo Externo Dinámico (BGP) y Sistemas Autónomos (AS)

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
