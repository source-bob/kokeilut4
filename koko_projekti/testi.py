

import random

# Diccionario
dictionary_A = {
    'key1': -40,
    'key2': 50,
    'key3': 20,
    'key4': 100,
    'key5': 500,
    'key6': 1000,
}


# Función que devuelve el valor de una clave aleatoria como un número entero
def get_random_value_as_int():
    # Seleccionar una clave aleatoria
    random_key = random.choice(list(dictionary_A.keys()))

    # Obtener el valor correspondiente
    value = dictionary_A[random_key]

    # Verificar si el valor es numérico y devolverlo como entero
    if isinstance(value, (int, float)):
        return int(value)
    else:
        return "El valor no es numérico, no se puede devolver como entero."