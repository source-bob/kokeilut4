m = [134, 195]
n = [117, 175]

suku = int(input('suku 1 - m, 2 - n: '))
hemo = int(input('anna hemoglobiiniarvon: '))
check = []

if suku == 1:
    check = m
elif suku == 2:
    check = n

if hemo < check[0]:
    print('alhainen')
elif hemo > check[0] and hemo < check[1]:
    print('normaali')
elif hemo > check[1]:
    print('korkea')