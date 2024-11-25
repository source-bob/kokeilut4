import random

def heito(sides):
    return random.choice(range(1, sides + 1))

sivua = int(input('anna sides: '))

while True:
    noppa = heito(sivua)
    if noppa == sivua:
        print(f'{noppa}!')
        print('voito')
        break
    print(f'sorry, {noppa}, kokeile vielä')