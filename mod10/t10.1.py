class Hissi:

    def __init__(self, ala, yla):
        self.kerros = 1
        self.ala = ala
        self.yla = yla

    def __str__(self):
        return f'Hissi on {self.kerros} kerroksessa                                                                                                                            '

    def kerros_alas(self):
        self.kerros -= 1

    def kerros_ylos(self):
        self.kerros += 1

    def siirry_kerrokseen(self, kerros):
        while True:
            if self.kerros < kerros and self.kerros + 1 <= self.yla:
                self.kerros_ylos()
                print(f'hissi siiretty {self.kerros} kerrokseen')
            elif self.kerros > kerros and self.kerros - 1 >= self.ala:
                self.kerros_alas()
                print(f'hissi siiretty {self.kerros} kerrokseen')
            elif self.kerros == kerros:
                print(f'Hissi on {self.kerros} kerroksessa')
                break


if __name__ == '__main__':
    lift = Hissi(1, 10)
    lift.siirry_kerrokseen(10)
    lift.siirry_kerrokseen(1)