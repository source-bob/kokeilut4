import random
import string

def agenti_tunus():
    caracteres = string.digits  # Solo números
    codigo = ''.join(random.choice(caracteres) for _ in range(4))  # Genera una secuencia de 4 números
    return codigo

# Ejemplo de uso
#print(generar_codigo())