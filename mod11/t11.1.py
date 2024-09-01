

class Publication:
    def __init__(self, nimi, type_x):
        self.type_x = type_x
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'{self.nimi} {self.type_x}')



class Book(Publication):
    def __init__(self, nimi, type_x, creator, sivut):
        super().__init__(nimi, type_x)
        self.creator = creator
        self.sivut = sivut

    def __str__(self):
        return f'book name: {self.nimi}\ntype: {self.type_x}\nwritten by: {self.creator}\npages: {self.sivut}'

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'written by: {self.creator}')
        print(f'pages: {self.sivut}')

class Journal(Publication):
    def __init__(self, nimi, type_x, creator):
        super().__init__(nimi, type_x)
        self.main_creator = creator

    def __str__(self):
        return f'name: {self.nimi}\ntype: {self.type_x}\ncreator: {self.main_creator}'

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'main creator: {self.main_creator}')

class Main:
    def __init__(self):
        self.library = {'books': [], 'journals': []}
        self.main_run()

    def main_run(self):
        self.ohje()
        while True:
            choice = input('add num: ')
            if choice == '1':
                self.new_record()
            elif choice == '2':
                self.read_lib()
            elif choice == '3':
                self.ohje()
            elif choice == '4':
                nimi = input('name: ')
                self.read_special(nimi)
            elif choice == '0':
                print('kiitos käynnistä')
                return

    def ohje(self):
        options = '''
        1 - make new
        2 - show
        3 - ohje
        4 - show special
        0 - exit
        '''
        print(options)

    def new_record(self):
        nimi = input('publication nimi: ')
        type = input('type (1 - book or 2 - journal): ')
        if type == '1':
            kirjoittaja = input('kirjoittaja: ')
            sivumaara = int(input('sivymäärä: '))
            self.library['books'].append(Book(nimi, 'book', kirjoittaja, sivumaara))
        elif type == '2':
            kirjoittaja = input('main redactor: ')
            self.library['journals'].append(Journal(nimi, 'journal', kirjoittaja))

    def read_lib(self):
        for item in self.library:
            for publication in self.library[item]:
                publication.tulosta_tiedot()
                print('_________')

    def read_special(self, nimi):
        for item in self.library:
            for publication in self.library[item]:
                if publication.nimi == nimi:
                    publication.tulosta_tiedot()

if __name__ == '__main__':

    book = Book('Hytti n:o 6', 'book', 'Rosa Liskom', 200)
    book.tulosta_tiedot()
    print('_________')
    journal = Journal('Aku Ankka', 'journal', 'Aki Hyyppä')
    journal.tulosta_tiedot()

    #lib = Main()


    