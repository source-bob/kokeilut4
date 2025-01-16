import random

numerot = list(range(1, 11))

while True:
    print('new game')
    print('0 lopeta')
    numero = random.choice(numerot)

    while True:
        suoritus = int(input('anna numero (1-10): '))
        if suoritus == 0:
            print('peli loppu')
            break
        elif suoritus == numero:
            print('good')
            print(f'numero oli {suoritus}')
            break
        elif suoritus < numero:
            print('lian pieni, try again')
        elif suoritus > numero:
            print('lian suuri, try again')
    if suoritus == 0:
        break