
import random

class Auto:

    def __init__(self, rektun, nopeus):
        self.rektun = rektun
        self.nopeus = nopeus
        self.nopeus_h = 100
        self.matka = 0
        self.matkan_aika = 0

    def __str__(self):
        return f'rekisteritunnus: {self.rektun}\nhuippunopeus on {self.nopeus} km/h\nnopeus nyt: {self.nopeus_h} km/h\najettu matka: {self.matka} km'

    def kiihdittya(self, maara:int):
        if maara > 0:
            if self.nopeus_h + maara < self.nopeus:
                self.nopeus_h += maara
            else:
                self.nopeus_h = self.nopeus
                print(f'{self.rektun} max speed laitettu')
        elif maara < 0:
            if self.nopeus_h + maara > 0:
                self.nopeus_h += maara
            else:
                self.nopeus_h = 0
                print(f'pysähty {self.rektun}')

    def hatajarru(self):
        self.kiihdittya(-200)
        print(f'hätäjarru! nopeus nyt: {self.nopeus_h} km/h')

    def kulje(self, tunnit:float):
        matka = self.nopeus_h * tunnit
        self.matka += matka
        self.matkan_aika += tunnit



if __name__ == '__main__':
    list_of_cars = []
    list_of_speeds = list(range(100, 200, 10))
    list_of_changes = list(range(-10, 15, 5))
    tunnit_m = 0

    for i in range(1, 11):
        list_of_cars.append(Auto(f'ABC-{i}', random.choice(list_of_speeds)))

    def tick(carlist, changelist):
        for car in carlist:
            car.kiihdittya(random.choice(changelist))
            car.kulje(1)

    while True:
        leader_board = []
        winner_check = False

        tick(list_of_cars, list_of_changes)
        for car in list_of_cars:
            leader_board.append((car.rektun, car.matka))

        leader_board = sorted(leader_board, key=lambda m: m[1], reverse=True)
        for i in range(3):
            print(f'{i + 1} auto {leader_board[i][0]}: {leader_board[i][1]} km ajettu')
            if leader_board[0][1] >= 10000:
                winner_check = True
                break
        if winner_check:
            break

    for car in list_of_cars:
        if car.matka >= 10000:
            print(f'Voitajan rektun: {car.rektun}, ajettu matka: {car.matka}')

    print(f'tunnit matkalla: {list_of_cars[0].matkan_aika} h')