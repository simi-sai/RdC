# Trabajo Practico N°5

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

### 1. Desarrollo de Scripts

### 2.

### 3.

### 4. Encriptacion
#### ENCRIPTADO SIMETRICO
El cifrado simétrico es un tipo de cifrado en el que se utiliza la misma clave para cifrar y descifrar los datos. 

Al utilizar una única clave, el proceso es sencillo por lo que se consigue un buen rendimiento con un bajo consumo de recursos. Pero esto tambien hace que sea menos seguro que el encriptado asimetrico.

Algunos ejemplos de cifrado simetrico son:

* **AES (Advanced Encryption Standard):** Es uno de los algoritmos de cifrado mas utilizados en el mundo. FUe adoptado como estándar de cifrado por el gobierno de los Estados UNidos y es conocido por su eficiencia y seguridad. Se usa comunmente para protección de datos en disco, conexiones seguras en la web (HTTPS), y aplicaciones de cifrado de archivos.

* **DES(Data Encryption Standard):** FUe uno de los primeros algoritmos de cifrado ampliamente adoptados. Utiliza una clave de 56 bits, lo que hoy en dia se considera inseguro debido a su vulnerabilidad a ataques de fuerza bruta,

* **3DES(Triple DES):** Mejora la seguridad de DES al aplicar el algoritmo tres veces con diferentes claves. Es mas seguro que DES pero tambien es mas lento.

#### ENCRIPTADO ASIMETRICO
A diferencia de la encriptación simétrica, la encriptación de clave asimétrica utiliza una clave pública y una clave privada para encriptar y desencriptar datos. Este metodo elimina la necesidad de compartir la misma clave, ya que una clave(la pública) se utiliza para cifrar, y la otra (la privada) para descifrar. 

Este cifrado, tambien conocido como **criptografia de clave publica**, se utiliza habitualmente para comunicaciones seguras en línea, firmas digitales, y protocolos SSL/TLS para establecer conexiones seguras entre navegadores web y servidores.

Algunos algoritmos de encriptacion asimétrica muy utilizados son:

* **RSA (Rivest-Shamir-Adleman):** RSA es uno de los sistemas de encriptación de clave pública más comunes, conocido por su seguridad y versatilidad.

* **ECC (Criptografia de Curva Elíptica):** La ECC proporciona alta seguridad con longitudes de clave mas cortas, lo que hace mas rapida y eficaz para los dispositivos moviles.

* **DSA (Algoritmo de Firma Digital):** Utilizado principalmente para firmas digitales, el DSA garantiza la autenticidad e integridad de los datos.

#### COMPARACION ENTRE CIFRADO SIMETRICO Y ASIMETRICO.

|                        | **Cifrado simétrico**                                   | **Cifrado asimétrico**                                 |
|------------------------|----------------------------------------------------------|----------------------------------------------------------|
| **Claves de uso**      | Misma clave para encriptar y desencriptar               | Par de claves pública y privada                         |
| **Distribución de llaves** | Requiere un intercambio de claves seguro entre las partes | La clave pública puede compartirse abiertamente         |
| **Velocidad**          | Generalmente más rápido, más eficaz para grandes volúmenes de datos | Más lento, más intensivo computacionalmente     |
| **Casos prácticos**    | Cifrado masivo de datos, almacenamiento de archivos, bases de datos | Intercambio seguro de datos, autenticación, firmas digitales |
| **Seguridad**          | Fuerte para entornos privados y controlados             | Mayor seguridad para redes abiertas en las que es posible compartir públicamente |
| **Escalabilidad**      | Gestión de claves menos escalable y compleja para múltiples usuarios | Más escalable, ya que la clave pública puede compartirse con varios usuarios |
| **Algoritmos**         | AES, DES, 3DES                                      | RSA, ECC, DSA                                            |

#### APLICACION EN LOS SCRIPTS DESARROLLADOS

Para nuestro desarrollo, usamos la libreria de Python `cryptography`, que es la mas moderna y mantenida. Encripta con AES(simetrica) y RSA(asimetrica).

Para nuestro caso, elegimos la encriptacion simetrica AES.

#### Caracteristicas de **AES**:
Elegimos AES porque destaca en muchas metricas clave de rendimiento. Sus principales caracteristicas son:



