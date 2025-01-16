lista = []
while True:
    luku = input('anna luku: ')
    if luku == '':
        break
    else:
        lista.append(float(luku))

lista = sorted(lista, reverse=True)
if len(lista) >= 5:
    print(lista[:5])
else:
    print(lista)