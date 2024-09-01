
import random
import pandas as pd

class Auto:

    def __init__(self, rektun, nopeus):
        self.rektun = rektun
        self.nopeus = nopeus
        self.nopeus_h = 100
        self.matka = 0
        self.matkan_aika = 0

    def __str__(self):
        return (
            f'rekisteritunnus: {self.rektun}\n'
            f'huippunopeus (km/h): {self.nopeus}\n'
            f'nopeus nyt (km/h): {self.nopeus_h}\n'
            f'ajettu matka(km): {self.matka}\n'
            f'matkan kesto (h): {self.matkan_aika}'
        )

    def kiihdittya(self, maara:int):
        if maara > 0:
            if self.nopeus_h + maara < self.nopeus:
                self.nopeus_h += maara
            else:
                self.nopeus_h = self.nopeus
        elif maara < 0:
            if self.nopeus_h + maara > 0:
                self.nopeus_h += maara
            else:
                self.nopeus_h = 0

    def hatajarru(self):
        self.kiihdittya(-200)
        print(f'hätäjarru! nopeus nyt: {self.nopeus_h} km/h')

    def kulje(self, tunnit:float):
        matka = self.nopeus_h * tunnit
        self.matka += matka
        self.matkan_aika += tunnit

class Kilpailu:
    def __init__(self, kilp_nimi, pituus, auton_lista):
        self.kilp_nimi = kilp_nimi
        self.pituus = pituus
        self.auton_lista = auton_lista
        self.voitajat = []

    def tunti_kuulu(self):
        for car in self.auton_lista:
            if car.matka < self.pituus:
                if car.nopeus_h < 100:
                    car.kiihdittya(random.choice(list(range(5, 15, 5))))
                elif car.nopeus_h >= 100:
                    car.kiihdittya(random.choice(list(range(-10, 15, 5))))
                car.kulje(1)
            elif car.matka >= self.pituus and car not in self.voitajat:
                car.hatajarru()
                self.voitajat.append(car)
        if self.kilpailu_ohi():
            self.end()



    def tulosta_tilanne(self):
        for car in self.auton_lista:
            print(car)
            print('____________')

    def kilpailu_ohi(self):
        return len(self.voitajat) >= 4

    def end(self):
        self.tulosta_tilanne()
        data = [dict(item2.split(': ') for item2 in str(winner).split('\n')) for winner in self.voitajat]

        scores = pd.DataFrame(data)
        ind = ['scores a first place knock-out!', 'finishes second!', 'takes a weak third!', 'is in another time zone!']
        scores.index = [f'{row['rekisteritunnus']} {indx}' for row, indx in zip(scores.to_dict('records'), ind)]
        scores = scores.drop(scores.columns[[0, 2, 3]], axis=1)
        print(scores)

if __name__ == '__main__':
    list_of_cars = []
    list_of_speeds = list(range(100, 200, 10))
    for i in range(1, int(input('how much cars?: ')) + 1):
        list_of_cars.append(Auto(f'ABC-{i}', random.choice(list_of_speeds)))

    distance = int(input('how long? (km): '))

    challenge = Kilpailu('Romuralli', distance, list_of_cars)
    while True:
        challenge.tunti_kuulu()
        if challenge.kilpailu_ohi():
            break
