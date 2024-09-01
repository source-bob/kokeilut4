import requests

pyyntö = 'https://api.chucknorris.io/jokes/random'


while True:
    print('1 - new joke, 2 - exit')
    choice = input('Your choice: ')
    if choice == '2':
        print('kiitos käynnistä')
        break
    elif choice == '1':
        vastaus = requests.get(pyyntö).json()
        print(vastaus['value'])