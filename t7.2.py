
nimi_arr = []
while True:
    nimi = input('anna nimesi: ')

    if nimi == '':
        print('kaikki nimet:')
        for item in nimi_arr:
            print(item)
        break

    if nimi in nimi_arr:
        print('aiemmin syötetty nimi')
    elif nimi not in nimi_arr:
        print('uusi nimi')

    nimi_arr.append(nimi)