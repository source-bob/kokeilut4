pituus = float(input('anna pituus (cm): '))
if pituus < 37:
    print(f'kuha on alamittainen, ei riitää {37 - pituus} cm')
    print('laske kuhan takaisin järveen, poliisi kohta on tulossa paikkaan rekisteröimään asian')
elif pituus > 37:
    print(f'Hieno, saat ottaa mukaan')