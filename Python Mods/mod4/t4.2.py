while True:
    tuuma = input('anna tuuma: ')
    if float(tuuma) < 0:
        break
    else:
        cm = float(tuuma) * 2.54
        print(f'{tuuma} tuuma on {cm:.2f} cm')