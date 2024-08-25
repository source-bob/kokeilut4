
def change(gal):
    return gal * 3.785

while True:
    gals = float(input('Kuinka paljon gal?: '))
    if gals < 0:
        print('moika')
        break
    print(f'{gals} gall on {change(gals):.3f} litraa')
