luvut = []

while True:
    luku = input('anna luku: ')
    if luku == '':
        break
    luvut.append(float(luku))



print(min(luvut), max(luvut))