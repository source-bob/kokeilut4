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
            if kerros > self.yla or kerros < self.ala:
                print('siirto epämahdollista')
                break
            elif self.kerros < kerros and self.kerros + 1 <= self.yla:
                self.kerros_ylos()
            elif self.kerros > kerros and self.kerros - 1 >= self.ala:
                self.kerros_alas()
            elif self.kerros == kerros:
                print(f'Siirto tehty {kerros} kerrokseen')
                break


class Talo:
    def __init__(self, hissi_kpl, ala, yla):
        self.ala_k = ala
        self.yla_k = yla
        self.hissi_kpl = hissi_kpl
        self.hisseja_lista = []
        self.hisseja(self.hissi_kpl, self.ala_k, self.yla_k)

    def __str__(self):
        for item in self.hisseja_lista:
            print(f'Hissi num {self.hisseja_lista.index(item) + 1} on {item.kerros} kerroksessa')
        return f'Talossa on {len(self.hisseja_lista)} hisseja ja {self.yla_k} kerroksia'

    def hisseja(self, kpl, ala, yla):
        for i in range(1, kpl + 1):
            self.hisseja_lista.append(Hissi(ala, yla))

    def aja_hissiä(self, numero, kerros):
        self.hisseja_lista[numero - 1].siirry_kerrokseen(kerros)



if __name__ == '__main__':
    check = input('haluatko laitaa taloa?(y/n): ')
    if check == 'n':
        print('kiitos käynnistä')
    elif check == 'y':
        floors = int(input('Kuinka paljon kerroksia?: '))
        lifts = int(input('Kuinka paljon hissiä?: '))
        house2 = Talo(lifts, 1, floors)
        print(house2)

        while True:
            print('ohje:')
            print('1 - siirtä hissi')
            print('2 - näyttää hissejä')
            print('0 - exit')
            checker = input('anna luku: ')
            if checker == '0':
                print('kiitos käynnistä')
                break
            elif checker == '1':
                h_num = int(input('laitaa hissin numero: '))
                k_num = int(input('laitaa kerros: '))
                house2.aja_hissiä(h_num, k_num)
            elif checker == '2':
                print(house2)



