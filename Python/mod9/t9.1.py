class Auto:

    def __init__(self, rektun, nopeus):
        self.rektun = rektun
        self.nopeus = nopeus
        self.nopeus_h = 0
        self.matka = 0

    def __str__(self):
        return f'rekisteritunnus: {self.rektun}\nhuippunopeus on {self.nopeus} km/h'

if __name__ == '__main__':
    car = Auto('ABC-123', 142)
    car2 = Auto('ZXC-987', 195)
    print(car)
    print(car2)