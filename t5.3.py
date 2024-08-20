check = list(range(1, 9))

while True:
    luku = float(input('anna luku: '))
    counter = 0
    for point in check:
        if luku % point == 0 and luku != 1 and point != 1 and luku != point:
            counter += 1
    if counter == 0 or luku == 1:
        print('luku on alkuluku')
    elif counter != 0:
        print('luku ei ole alkuluku')