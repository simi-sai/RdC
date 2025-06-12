from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

#Clave de 32 bytes para AES-256 
SECRET_KEY = b'EstaEsUnaKeyDeLenoxLegends2025!!'  # 32 bytes

def encrypt_message(message):
    iv=os.urandom(16)  # Generar un IV aleatorio de 16 bytes
    padder = padding.PKCS7(128).padder() # AES usa bloques de 128 bits (16 bytes)
    padded=padder.update(message.encode()) + padder.finalize() 
    cipher= Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cyphertext = encryptor.update(padded) + encryptor.finalize()
    return base64.b64encode(iv + cyphertext).decode('utf-8')

def decrypt_message(b64_encoded_data):
    raw= base64.b64decode(b64_encoded_data)
    iv = raw[:16]  # Extraer el IV de los primeros 16 bytes
    ciphertext = raw[16:]  # El resto es el ciphertext
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode('utf-8')