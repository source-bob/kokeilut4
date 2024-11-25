def ohje():
    print('1 - uusi lento')
    print('2 - hae talennettu lento')
    print('0 - exit')

airports = []

while True:
    ohje()
    choice = input('Anna numero: ')

    if choice == '1':
        koodi = input('anna koodi: ')
        nimi = input('anna nimi: ')
        airports.append((koodi, nimi))
        print('tiedot talennettu')
    elif choice == '2':
        koodi = input('anna koodi: ')
        for item in airports:
            if item[0] == koodi:
                print(f'koodi: {item[0]} airport nimi: {item[1]}')
    elif choice == '0':
        print('kiitos käynnistä')
        break
    else:
        print('väärin numero, kokeile vielä')