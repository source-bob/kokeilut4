'''
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
'''

class Vehicle:
    def __init__(self, rektun, huippunopeus, consuption, nope=0, matka=0, tankki=0, fuel=0, nopeudet=[], tunnit_matkalla=0):
        self.rektun = rektun
        self.huippunopeus = huippunopeus
        self.tankki = tankki
        self.consuption = consuption
        self.nopeus_nyt = nope
        self.matka = matka
        self.fuel = fuel
        self.tunnit_matkalla = tunnit_matkalla

    @property
    def keskinopeus(self):
        return self.matka / self.tunnit_matkalla if self.tunnit_matkalla > 0 else 0

    def tulosta_tiedot(self):
        print(
            f'''auto: {self.rektun}
huippunopeus: {self.huippunopeus} km/h
keskinopeus koko matkalla: {self.keskinopeus:.2f} km/h
yhteensä ajettu: {self.matka:.2f} km
tunnit matkalla: {self.tunnit_matkalla:.2f} h'''
        )

    def kiihdittya(self, num):
        if num > 0:
            self.nopeus_nyt = min(self.nopeus_nyt + num, self.huippunopeus)
        elif num < 0:
            self.nopeus_nyt = max(self.nopeus_nyt + num, 0)

    def kulje(self, hours):
        heti_matka = self.nopeus_nyt * hours
        poltettu = (heti_matka / 100) * self.consuption
        if self.tankki - poltettu > 0:
            self.tunnit_matkalla += hours
            self.tankki -= poltettu
            self.matka += heti_matka
            self.fuel += poltettu
        elif self.tankki - poltettu < 0:
            heti_matka = (100 / self.consuption) * self.tankki
            self.matka += heti_matka
            time = heti_matka / self.nopeus_nyt
            self.tunnit_matkalla += time
            self.fuel += self.tankki
            self.tankki = 0



    def hatajarru(self):
        self.kiihdittya(-200)



class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tankki=150)
        self.type = 'poltto'

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(
            f'''class: {self.type}
bensaa jäi {self.tankki:.2f} l
poltettu matkalla {self.fuel:.2f} l'''
        )

    def kulje(self, num):
        super().kulje(num)
        if self.tankki == 0:
            print('tarvi bensaa')
            self.hatajarru()


class Ecar(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tankki=250)
        self.type = 'e'

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(
            f'''class: {self.type}
{self.tankki:.2f} kWh sähköä jäi
{self.fuel:.2f} kW sähköä käytetty matkalla'''
        )

    def kulje(self, num):
        super().kulje(num)

        if self.tankki == 0:
            print('tarvi sähköä')
            self.hatajarru()

if __name__ == '__main__':
    car = Ecar('ABC-15', 180, 52.5, 40)
    car2 = Car('ACD-123', 165, 32.3, 50)
    for i in range(3):
        car.kulje(1)
        car2.kulje(1)
    car.kiihdittya(15)
    car2.kiihdittya(-10)

    for i in range(3):
        car.kulje(1)
        car2.kulje(1)

    car.tulosta_tiedot()
    print('_________')
    car2.tulosta_tiedot()