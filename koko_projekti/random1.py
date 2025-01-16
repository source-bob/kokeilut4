import random
#random1
dictionary_A = {
    'key1': 10,
    'key2': 20,
    'key3': 40,
    'key4': 50,
    'key5': 80,
    'key6': 100,
}


def random_A():
    random_key = random.choice(list(dictionary_A.keys()))
    value = dictionary_A[random_key]

    if isinstance(value, (int, float)):
        return int(value)

#random2

dictionary_B = {
    'key1': 200,
    'key2': 300,
    'key3': 500,
    'key4': 100,
    'key5': 150,
    'key6': 250,
}


def random_B():
    random_key = random.choice(list(dictionary_B.keys()))
    value = dictionary_B[random_key]

    if isinstance(value, (int, float)):
        return int(value)
#random3

dictionary_C = {
    'key1': 'thief',
    'key2': 'time',
    'key3': 'mail',
    'key4': 'code',
    'key5': 'mail'
}

def random_C():
    random_key = random.choice(list(dictionary_C.keys()))
    return dictionary_C[random_key]


#random4

r_text = {
    'key1': 'KEEP GOING IF YOU ARE ON THE RIGHT TRACK!',
    'key2': 'IT APPARENTLY HAS SEEN THE EVIL-DOER AT THIS AIRPORT',
    'key3': 'YOU ARE VERY CLOSE TO THE THIEF',

}

def random_T():
    random_key = random.choice(list(r_text.keys()))
    return r_text[random_key]





