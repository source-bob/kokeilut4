vuosi = int(input('anna vuosi: '))
print(vuosi // 4 == 0)
if vuosi // 4 == 0:
    print('moi')
    if vuosi // 100 == 0:
        if vuosi // 400 == 0:
            print('karkausvuosi')
        else:
            print('ei karkausvuosi')
    else:
        print('karkausvuosi')
