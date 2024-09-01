import requests





while True:
    choice = input('1 - show weather, 2 - exit: ')
    if choice == '2':
        print('kiitos käynnistä')
        break
    elif choice == '1':
        kaupunki = input('kaupunki: ')
        response = requests.get(f'https://wttr.in/{kaupunki}?format=j1')
        data = response.json()

        aste = data['current_condition'][0]['temp_C']
        sää = data['current_condition'][0]['weatherDesc'][0]['value']
        print(f'{kaupunki}: {aste}°C')
        print(f'weather condition: {sää}')