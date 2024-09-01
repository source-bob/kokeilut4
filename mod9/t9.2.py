class Auto:

    def __init__(self, rektun, nopeus):
        self.rektun = rektun
        self.nopeus = nopeus
        self.nopeus_h = 0
        self.matka = 0

    def __str__(self):
        return f'rekisteritunnus: {self.rektun}\nhuippunopeus on {self.nopeus} km/h\nnopeus nyt: {self.nopeus_h} km/h'

    def kiihdittya(self, maara:int):
        if maara > 0:
            if self.nopeus_h + maara < self.nopeus:
                self.nopeus_h += maara
            else:
                self.nopeus_h = self.nopeus
                print('max speed laitettu')
        elif maara < 0:
            if self.nopeus_h + maara > 0:
                self.nopeus_h += maara
            else:
                self.nopeus_h = 0
                print('pysähty')

    def hatajarru(self):
        self.kiihdittya(-200)
        print(f'hätäjarru! nopeus nyt: {self.nopeus_h} km/h')

if __name__ == '__main__':
    car = Auto('ABC-123', 142)
    car2 = Auto('ZXC-987', 195)
    car.kiihdittya(60)
    car.kiihdittya(-17)
    print(car)
    print(car2)
    car2.kiihdittya(150)
    print(car2)
    car2.hatajarru()