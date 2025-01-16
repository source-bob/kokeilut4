luokka = input('anna hyttiluokan (LUX, A, B, C): ')
if luokka == 'LUX':
    print(f'{luokka} on parvekkeellinen hytti yläkannella')
elif luokka == 'A':
    print(f'{luokka} on ikkunallinen hytti autokannen yläpuolella')
elif luokka == 'B':
    print(f'{luokka} on ikkunaton hytti autokannen yläpuolella')
elif luokka == 'C':
    print(f'{luokka} on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')