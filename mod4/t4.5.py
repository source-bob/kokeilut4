oik_tunnus = 'python'
oik_salasana = 'rules'
check = 0
while True:
    tunnus = input('anna tunnus: ')
    salasana = input('anna salasana: ')
    if tunnus == oik_tunnus and salasana == oik_salasana:
        print('Tervetuloa')
        break
    else:
        print('pääsy evätty, try again')
        check += 1
        if check == 5:
            print('bye')
            break