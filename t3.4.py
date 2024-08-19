vuosi = int(input('anna vuosi: '))
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print('karkausvuosi')
        else:
            print('ei karkausvuosi')
    else:
        print('karkausvuosi')
else:
    print('ei karkausvuosi')
