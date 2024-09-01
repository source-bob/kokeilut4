while True:
    luku = int(input('anna luku: '))
    if luku < 2:
        print('luku ei ole alkuluku')
        continue

    is_prime = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            is_prime = False
            break

    if is_prime:
        print('luku on alkuluku')
    else:
        print('luku ei ole alkuluku')