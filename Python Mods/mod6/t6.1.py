import random

def heito():
    sides = list(range(1, 7))
    return random.choice(sides)

while True:
    noppa = heito()
    if noppa == 6:
        print(f'{noppa}!')
        print('voito')
        break
    print(f'sorry, {noppa}, kokeile vielä')