import data1 as data
import pygame
import random

class Menu:
    def __init__(self, rows):
        self.rows = rows

class Peli:
    def __init__(self):
        pygame.init()
        self.player1 = Player()
        self.player2 = Player()

        self.näytön_leveys = 1060
        self.näytön_korkeus = 720
        self.näyttö = pygame.display.set_mode((self.näytön_leveys, self.näytön_korkeus))

        self.addit_points = []
        self.points = self.make_points()
        self.start_x = self.näytön_leveys / 2 - 50
        self.start_y = self.näytön_korkeus / 2 - 50
        
        
        self.players = [self.player1, self.player2]

        self.ports = []
        self.round = None
        self.circles = 0

        self.fontti = pygame.font.SysFont('Arial', 14)
        self.turn = 1
        self.last_roll = None
        self.loop()

    

    def loop(self):
        game = self.menu1()
        if game == 3:
            self.show_results()
            self.menu1()
        if game == 2 and len(data.get_info('ports')) < 18:
            self.last_game()
            game -= 1
        
        if game == 1:
            data.clear_data()
            data.get_ports()
            data.create_board()
            self.player1.create_new()
            self.player2.create_new()
            self.round = 1
            for player in self.players:
                player.start()
                player.set_params()
        elif game == 2:
            self.round = data.get_round()
            for player in self.players:
                player.set_params()

        
        
        self.make_ports()
        while True:
            self.check_events()
            self.show()
            self.turns()
    
    def show_results(self):
        res = data.get_results()
        x = self.start_x
        y = self.start_y
        
        font = pygame.font.SysFont('Arial', 14)
        screen = self.näyttö
        max_w = 400
        next = False


        jonot = [jono for jono in res]

        screen.fill((0, 0, 0))
        

        while not next:
            temp_y = y

            
            for i, jono in enumerate(jonot):
                merkkijono = f'{jono['peli_id']}: {jono['pyörät']} {jono['voittaja']} {jono['pääoma']}'
                data.render_text_in_box(merkkijono, x, temp_y, max_w, font, screen, True)
                
                temp_y += 20

            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_f:
                        next = True
                elif event.type == pygame.QUIT:
                    exit()

            pygame.display.update()
        return
        

    def show(self):
        self.piirrä_näyttö()
        pygame.display.flip()

    def piirrä_näyttö(self):
        self.näyttö.fill((0, 0, 0))
        self.show_board()
        
    def show_ports(self):
        for i in range(0, 28):
            self.ports[i].show_port(self.näyttö, self.points[i][0], self.points[i][1], self.fontti)

    def make_ports(self):
        for i in range(1, 29):
            self.ports.append(Port(i))

    def heittaa_nappi(self):
        return random.choice(list(range(1, 7)))
    
    def show_players(self):
        i = 70
        color = (0, 0, 255)
        for player in self.players:
            pygame.draw.circle(self.näyttö, color, (self.points[player.position][0] + i - 20, self.points[player.position][1] + 35), 5)
            i += 20
            color = (255, 0, 0)
    
    def turns(self):
        for player in self.players:
            if player.rent == True:
                self.rentoutu(player)
            elif player.rent == False:
                self.first(player)
                paikka = self.ports[player.position]
                if paikka.owner == None:
                    self.buy(paikka, player)
                elif paikka.owner != None and paikka.owner != 'not availible':
                    if player.name != paikka.owner:
                        if player.money - paikka.price / 10 < 0:
                            while player.money - paikka.price / 10 < 0:
                                self.not_enough(player, 'to pay fee, you have to sell something', True)
                        self.exchange(player, paikka)
                elif paikka.owner == 'not availible':
                    self.check_ruutu(paikka, player)
            

                set_checking = self.check_sets(player.name, True)
                if set_checking[0] == True:
                    self.third(set_checking[1], player)
                

        self.turn += 1

    def check_ruutu(self, paikka, player):
        bonus = 75
        bill = 50
        paikat = {
            'bonus': 1,
            'bill': 2,
            'airbus': 3,
            'bonus2': 4,
            'rent': 5,
            'billx2': 6,
            'chance': 7,
            'kirppis': 8,
            'bonus3': 9,
            'start': 0
        }
        chosen = paikat[paikka.name]
        if chosen == 1:
            self.bonus(bonus, player)
        elif chosen == 2:
            self.bill(bill, player)
        elif chosen == 3:
            self.airtaxi(player)
        elif chosen == 4:
            self.bonus(bonus * 2, player)
        elif chosen == 5:
            self.rent(player)
        elif chosen == 6:
            self.bill(bill * 2, player)
        elif chosen == 7:
            self.chance(player)
        elif chosen == 8:
            self.kirppis(player)
        elif chosen == 9:
            self.bonus(bonus * 3, player)
        elif chosen == 0:
            pass

    def rent(self, player):
        x = self.start_x
        y = self.start_y
        data.render_text_in_box(f'voit rentoutua 1 turn (Y/N)', x, y, 100, self.fontti, self.näyttö, True)
        self.show_players()
        check = False
        yes = False

        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        yes = True
                        check = True
                    elif event.key == pygame.K_n:
                        check = True
        if yes:
            player.rent = True
        pygame.display.update()
        self.show()

    def rentoutu(self, player):
        x = self.start_x
        y = self.start_y
        data.render_text_in_box(f'tämä turn oot levämässä (d)', x, y, 100, self.fontti, self.näyttö, True)
        self.show_players()
        player.rent = False
        check = False

        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        check = True
        pygame.display.update()
        self.show()


    def kirppis(self, player):
        x = self.start_x
        y = self.start_y
        items = random.randint(1, 15)
        cash = items * 15
        player.add_money(cash)
        data.render_text_in_box(f'Myit tavaroita ja sait {cash} (d)', x, y, 100, self.fontti, self.näyttö, True)
        self.show_players()
        check = False

        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        check = True
        pygame.display.update()
        self.show()
    
    def chance(self, player):
        x = self.start_x
        y = self.start_y
        max_w = 200
        jonot = [
            f'Turn: {self.turn} ({player.name})',
            'Haluatko try chance? (Y/N)',
            'if nappi on 1 - hävitset puoli rahaa, mut muuita antaa nappi X 100']
        for jono in jonot:
            data.render_text_in_box(jono, x, y, max_w, self.fontti, self.näyttö, True)
            y += 20
        check = False
        chance_try = False
      
        self.show_players()
        while not check:

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        chance_try = True
                        check = True
                    elif event.key == pygame.K_n:
                        check = True
                elif event.type == pygame.QUIT:
                    exit()
        
        self.piirrä_näyttö()
        pygame.display.update()
        
        
        if chance_try:
            self.chances(player)
            return

    def chances(self, player):
        
        x = self.start_x
        y = self.start_y

        
        cube = random.randint(1, 6)
        if cube == 1:
            data.render_text_in_box(f' cube is {cube} you loose half money {player.money / 2} (d)', x, y, 200, self.fontti, self.näyttö, True)
            player.add_money(-player.money / 2)
        elif cube != 1:
            data.render_text_in_box(f'cube is {cube} you got money {cube * 100} (d)', x, y, 200, self.fontti, self.näyttö, True)
            player.add_money(cube * 100)

        

        self.show_players()
        chosen = False

        while not chosen:
            pygame.display.flip()
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        chosen = True
                elif event.type == pygame.QUIT:
                    exit()

        pygame.display.update()
        self.show()
        return

            
            
        


    def airtaxi(self, player):
        x = self.start_x
        y = self.start_y
        distance = random.randint(1, 9)
        for i in range(distance):
            player.change_position()
        data.render_text_in_box(f'oot lentanut lisäksi {distance} points (d)', x, y, 100, self.fontti, self.näyttö, True)
        player.position += distance
        self.show_players()
        check = False
        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        check = True
        pygame.display.update()
        self.show()

    def bonus(self, amount, player):
        x = self.start_x
        y = self.start_y
        check = False
        player.add_money(amount)
        data.render_text_in_box(f'sait {amount} bonus! (d)', x, y, 100, self.fontti, self.näyttö, True)
        self.show_players()
        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        check = True
        pygame.display.update()
        self.show()

    def bill(self, amount, player):
        x = self.start_x
        y = self.start_y
        check = False
        if player.money - amount < 0:
            while player.money - amount <0:
                self.not_enough(player, f'to pay bill {amount}, sell something', True)
        player.add_money(-amount)
        data.render_text_in_box(f'sait {amount} bill! (d)', x, y, 100, self.fontti, self.näyttö, True)
        self.show_players()
        while not check:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        check = True
        pygame.display.update()
        self.show()

    def third(self, sets, player):
        x = self.start_x
        y = self.start_y
        max_w = 300
        check = False
        lvl_up = False
        
        jonot = [
            f'Turn: {self.turn} ({player.name})',
            'Haluatko add lvl to your property?',
            f'nappi oli: {self.last_roll}'
        ]

        for jono in jonot:
            data.render_text_in_box(jono, x, y, max_w, self.fontti, self.näyttö, True)
            y += 20

        self.show_players()
        while not check:

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        lvl_up = True
                        check = True
                    elif event.key == pygame.K_n:
                        check = True
                elif event.type == pygame.QUIT:
                    exit()
        
        self.piirrä_näyttö()
        pygame.display.update()
        
        
        if lvl_up:
            self.property_level(sets, player, True)
            return

        

    def property_level(self, set_property, player, lvl=False, sell=False):
        pygame.display.update()
        self.show()
        x = self.start_x
        y = self.start_y

        arrow = Arrow(x, y + 20, len(set_property))
        poly_points = arrow.points_now
        arrow_points = []
        data.render_text_in_box(f'which one?', x, y, 100, self.fontti, self.näyttö, True)
        y += 20

        prices = []
        for prop in set_property:
            for port in self.ports:
                if port.name == prop:
                    price = port.price
                    prices.append(price)
            data.render_text_in_box(f'{prop} ({price})', x, y, 300, self.fontti, self.näyttö, True)
            arrow_points.append([x - 15, y + 5])
            y += 20

        self.show_players()
        chosen = False
        idx = None

        while not chosen:
            pygame.display.flip()
            pygame.draw.polygon(self.näyttö, (0, 0, 0), poly_points)
            pygame.draw.polygon(self.näyttö, arrow.color, arrow.points_now)
            poly_points = arrow.points_now 
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        idx = arrow_points.index(arrow.x_y_now)
                        chosen = True
                    elif event.key == pygame.K_DOWN:
                        arrow.move_down()
                    elif event.key == pygame.K_UP:
                        arrow.move_up()
                elif event.type == pygame.QUIT:
                    exit()

            
            
        if chosen:
            if lvl:
                if player.money - prices[idx] >= 0:
                    self.lvl_up(set_property[idx])
                    player.add_money(-prices[idx])
                    self.show()
                    pygame.display.update()
                elif player.money - prices[idx] < 0:
                    self.show()
                    pygame.display.update()
                    self.not_enough(player, 'upgrade')
            elif sell:
                self.sell(set_property[idx])
                player.add_money(prices[idx])
                self.show()
                pygame.display.update()
        
    def sell(self, prope):
        id = None
        for port in self.ports:
            if port.name == prope:
                port.owner = None
                id = port.id
        
        data.delete_owner(prope, id)
        pygame.display.update()
        self.show()
        
        
        
        
    def not_enough(self, player, target, sell=False):
        x = self.start_x
        y = self.start_y
        data.render_text_in_box(f'not enough money to {target}, press d to continue', x, y, 300, self.fontti, self.näyttö, True)
        self.show_players()
        chosen = False
        while not chosen:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        chosen = True
        if sell:
            prope = self.check_sets(player.name, False, True)
            if len(prope) == 0:
                self.raha_loppu(player)
                winner = None
                for gamer in self.players:
                    if gamer.name != player.name:
                        winner = gamer
                self.finish_game(winner)
            self.property_level(prope, player, False, True)
            pygame.display.update()
            self.show()
        pygame.display.update()
        self.show()

    def raha_loppu(self, player):
        x = self.start_x
        y = self.start_y
        data.render_text_in_box(f'Anteeksi, sulla ei ole mitään, {player.name} loose (d)', x, y, 300, self.fontti, self.näyttö, True)
        self.show_players()
        chosen = False
        while not chosen:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        chosen = True
        return

    def lvl_up(self, port):
        for unit in self.ports:
            if unit.name == port:
                unit.add_lvl()
            


    def check_sets(self, p_name, setts=False, all=False):
        sets_property = []
        ports = [port for port in self.ports if port.owner == p_name]
        if setts:
            sets = 0
            if len(ports) > 1:
                for i in range(0, len(ports)):
                    if i + 1 < len(ports):
                        if ports[i].country == ports[i + 1].country:
                            sets_property.append(ports[i].name)
                            sets_property.append(ports[i + 1].name)
                            sets += 1
            
        
            if sets > 0:
                return (True, sets_property)
            elif sets == 0:
                return (False, sets_property)
        elif all:
            for port in ports:
                sets_property.append(port.name)
            return sets_property
        
    def save_game(self, round):
        data.save_game(round, None, None, True)

    def first(self, player):
        x, y = self.start_x, self.start_y
        jonot = [f'Round: {self.round}' , f'Turn: {self.turn} ({player.name})', 'Haluatko heittää nappi? (y)', f'nappi oli: {self.last_roll}']
        max_w = 200
        
        for jono in jonot:
            data.render_text_in_box(jono, x, y, max_w, self.fontti, self.näyttö, True)
            y += 20
        
        self.show_players()
        nappi = False
        while not nappi:

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        nappi = True
                elif event.type == pygame.QUIT:
                    self.save_game(self.round)
                    exit()


        if nappi:
            num = self.heittaa_nappi()
            for i in range(0, num):
                if player.position + 1 >= 28:
                    player.set_position()
                    player.add_money(590)
                    self.circles += 1
                    if self.circles == 2:
                        self.round += 1
                        self.circles = 0
                        if self.round == 16:
                            self.calculate_results()
                elif player.position + 1 < 28:
                    player.change_position()  # Изменяем позицию игрока
                player.position = data.get_pos(player.id)
            self.last_roll = num
            
            pygame.display.update()
            self.show() 
        return

    def calculate_results(self):
        x, y = self.start_x, self.start_y
        ress = []
        capital = None
        for player in self.players:
            property_count = player.count_property()
            ress.append(property_count)

        
        if ress[0] > ress[1]:
            voittaja = self.players[0]
            capital = ress[0]
        elif ress[1] > ress[0]:
            voittaja = self.players[1]
            capital = ress[1]

        jonot = [
            f'the game is over in {self.round} rounds',
            f'{voittaja.name} on voittanut with {capital} capital! (d)'
        ]
        

        pygame.display.update()
        self.show()
        for jono in jonot:
            data.render_text_in_box(jono, x, y, 300, self.fontti, self.näyttö, True)
            y += 20
        answer = False
        while not answer:
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            answer = True
                    elif event.type == pygame.QUIT:
                        exit()
        
        pygame.display.update()
        self.show()
        self.finish_game(voittaja)

    
    def buy(self, port, player):
        check = player.money - port.price
        if check >= 0:
            data.render_text_in_box(f'haluatko ostaa? d/n', self.näytön_leveys / 2 - 50, self.näytön_korkeus / 2 - 50, 100, self.fontti, self.näyttö, True)
        elif check < 0:
            data.render_text_in_box(f'not enough money to buy property, press d', self.näytön_leveys / 2 - 50, self.näytön_korkeus / 2 - 50, 100, self.fontti, self.näyttö, True)
        self.show_players()
        chosen = False
        prop = False
        while not chosen:
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            if check >= 0:
                                prop = True
                            chosen = True
                        elif event.key == pygame.K_n:
                            chosen = True
                    elif event.type == pygame.QUIT:
                        exit()
        if prop:
            player.add_property(port)
        pygame.display.update()
        self.show()

    def exchange(self, player, port):
        x, y = self.start_x, self.start_y
        fee = port.price // 10

        jonot = [
            f'u paid fee {fee}',
            f'{port.owner} receive fee',
            '(d) to continue'
        ]

        for jono in jonot:
            data.render_text_in_box(jono, x, y, 300, self.fontti, self.näyttö, True)
            y += 20
        self.show_players()
        for gamer in self.players:
            if gamer.name == player.name:
                gamer.add_money(-fee)
            if gamer.name == port.owner:
                gamer.add_money(fee)
        answer = False
        while not answer:
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            answer = True
                    elif event.type == pygame.QUIT:
                        exit()
        self.show()
        pygame.display.update()

    def show_board(self):
        data.render_text_in_box(f'{self.player1.get_info_p()[0]}', self.addit_points[11][0], self.addit_points[11][1], 60, self.fontti, self.näyttö, True)
        data.render_text_in_box(f'{self.player2.get_info_p()[0]}', self.addit_points[18][0], self.addit_points[18][1], 60, self.fontti, self.näyttö, True)
        self.show_players()
        self.show_ports()

    

       

    def ruutu(self, x, y):
        return pygame.draw.rect(self.näyttö, (255, 255, 255), (x, y, 100, 100))

    def make_points(self):
        point_maker = []
        start_px = self.näytön_leveys - 105
        start_py = self.näytön_korkeus - 105
        finish_px = self.näytön_leveys - 105*10
        finish_py = self.näytön_korkeus - 105*6

        for x in range(start_px, finish_px - 105, -105):
            point_maker.append((x, start_py))
            if x != finish_px and x != start_px:
                self.addit_points.append((x, start_py - 105))
        for y in range(start_py - 105, finish_py, -105):
            point_maker.append((finish_px, y))
            if y > finish_py and y < start_py - 105:
                self.addit_points.append((finish_px + 105, y))
        for x in range(finish_px, start_px + 105, 105):
            point_maker.append((x, finish_py))
            if x != start_px and x != finish_px:
                self.addit_points.append((x, finish_py + 105))
        for y in range(finish_py + 105, start_py, 105):
            point_maker.append((start_px, y))
            if y != start_py - 105 and y != finish_py:
                self.addit_points.append((start_px - 105, y))

        return point_maker

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def menu1(self):
        x = self.start_x
        y = self.start_y
        y_temp = y
        font = self.fontti
        screen = self.näyttö
        max_w = 200
        arrow = Arrow(x, y, 3)
        next = False
        arrow_pt = []
        for i in range(3):
            arrow_pt.append([x - 15, y_temp + 5])
            y_temp += 20

        poly_points = arrow.points_now

        jonot = ['new game', 'continue last game', 'katso results']
        
        his = 'Peli on vuoropohjainen strategiapeli, jossa on taloudellinen painotus. Kaksi pelaajaa kilpailevat lentokenttien ostamisesta ja hallinnoinnista. Peli perustuu SQL-tietokantaan ja on toteutettu käyttämällä Pygame-moduulia. Tavoitteena on säilyttää pääoma pidempään kuin vastustaja, ajamalla hänet konkurssiin lentokenttien ostamisen, tulojen keräämisen, sakkojen maksamisen ja muiden pelitapahtumien kautta.'

        while not next:
            screen.fill((0, 0, 0))
            data.render_text_in_box(his, x - 200, y - 150, 500, font, screen, True)
            data.render_text_in_box('play?', x - 200, y + 150, max_w, font, screen, True)
            y_temp = y
            for i, jono in enumerate(jonot):
                data.render_text_in_box(jono, x, y_temp, max_w, font, screen, True)
                
                y_temp += 20

            pygame.draw.polygon(screen, (0, 0, 0), poly_points) 
            poly_points = arrow.points_now  
            pygame.draw.polygon(screen, arrow.color, poly_points)  

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        arrow.move_down()
                    elif event.key == pygame.K_UP:
                        arrow.move_up()
                    elif event.key == pygame.K_f:
                        next = True
                        idx = arrow_pt.index((arrow.x_y_now))
                elif event.type == pygame.QUIT:
                    exit()

            pygame.display.update()

        if next:
            self.fontti = pygame.font.SysFont('Arial', 10)
            if idx == 0:
                return 1
            elif idx == 1:
                return 2
            elif idx == 2:
                return 3

            

    def finish_game(self, player):
        x = self.start_x
        y = self.start_y

        prop_money = 0
        max_w = 500

        data.render_text_in_box('the game is finished', x, y, max_w, self.fontti, self.näyttö, True)
        y += 20
        data.render_text_in_box(f'{player.name} won! (y)', x, y, max_w, self.fontti, self.näyttö, True)
        y += 20
        stats = player.get_stats()
        for prop in stats:
            jono = f'{prop["name"]:>40} {prop["price"]}'
            prop_money += prop['price']
            data.render_text_in_box(jono, x, y, max_w, self.fontti, self.näyttö, True)
            y += 20
        prop_money += player.money
        
        data.save_game(self.round, player.name, prop_money, False)
        chosen = False
        data.clear_data()
        while not chosen:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        chosen = True
                elif event.type == pygame.QUIT:
                    exit()

        if chosen:
            self.fontti = pygame.font.SysFont('Arial', 14)
            self.loop()
            pygame.display.update()
            self.show()
    
    def last_game(self):
        x, y = self.start_x, self.start_y
        
        while True:

            self.näyttö.fill((0, 0, 0))

            data.render_text_in_box('last game is over (d)', x, y, 200, self.fontti, self.näyttö, True)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        return
                elif event.type == pygame.QUIT:
                    exit()
            pygame.display.update()

class Arrow:
    
    def __init__(self, x, y, options):
        self.leveys = 1060
        self.korkeus = 720
        self.color = (255, 255, 255)
        self.x_y_now = [x - 15, y + 5]
        self.options = options
        self.pos = 1
        self.points_start = (x - 10, y + 7), (x - 15, y + 9), (x - 15, y + 5)
        self.points_now = self.points_start
        
    def move_up(self):
        new_points = []
        if self.pos - 1 > 0:
            for point in self.points_now:
                new_points.append((point[0], point[1] - 20))
            self.x_y_now[1] -= 20
            self.points_now = new_points
            self.pos -= 1
            print('new points: ', self.points_now)
            
    def move_down(self):
        new_points = []
        if self.pos + 1 < self.options + 1:
            for point in self.points_now:
                new_points.append((point[0], point[1] + 20))
            self.x_y_now[1] += 20
            self.points_now = new_points
            self.pos += 1
            print('new points: ', self.points_now)

class Player:

    cur_id = 1
    
    def __init__(self):
        self.id = Player.cur_id
        Player.cur_id += 1

    def set_params(self):
        inf = self.get_info_p()[1]
        self.name = inf['name']
        self.position = inf['position']
        self.money = inf['money']
        self.rent = False

    def create_new(self):
        data.new_char(f'player {self.id}')

    def get_info_p(self):
        pl = data.get_info_pl(self.id)[0]
        string = f'''{pl['name']} money: {pl['money']} position: {pl['position']}'''
        
        return [string, pl]
    
    def change_position(self):
        data.change_position(self.id, 1)

    def count_property(self):
        prope = data.count_prope(self.name)
        all = prope + self.money
        return all
    
    def set_position(self):
        self.position = 0
        data.set_position(self.id)

    def add_money(self, amount):
        data.add_money(self.id, amount)
        self.money += amount

    def add_property(self, port):
        data.add_property(self.name, port)
        self.add_money(-port.price)

    def start(self):
        data.set_position(self.id)
        self.position = data.get_pos(self.id)

    def get_stats(self):
        return data.get_player_prope(self.name)

class Port:
    def __init__(self, id):
        self.id = id
        self.sq = False
        self.set_params()

    def __str__(self):
        if self.owner != 'not availible':
            return f'name: {self.name}\ntype: {self.type}\ncountry: {self.country}\nprice: {self.price}\nowner: {self.owner}'
        elif self.owner == 'not availible':
            return f'name: {self.name}'
    
    def set_params(self):
        values = data.get_info('ports', self.id)[0]
        if not values['iso_country']:
            self.name = values['name']
            self.type = values['type']
            self.owner = values['owner']
        elif values['iso_country']:
            self.name = values['name']
            self.type = values['type']
            self.country = values['country']
            self.price = values['price']
            self.alku_hinta = self.id * 15 + 40
            self.owner = values['owner']
            self.sq = True
            self.lvl = int(values['lvl'])

    def show_port(self, screen, x, y, fontti):
        
        self.ruutu(screen, x, y)
        self.show_info(screen, x, y, fontti)
        
    def show_info(self, screen, x, y, fontti):
        alku_x = x
        alku_y = y
        x += 2
        y += 2

        if self.owner != 'not availible':
            string = [self.name, self.type, self.country, self.price, self.owner, self.lvl]

        elif self.owner == 'not availible':
            string = [self.name]
        step = 1
        for value in string:
            if step == 6:
                x = alku_x + 75
                y = alku_y + 70
                value = f'lvl {value}'
            data.render_text_in_box(str(value), x, y, 95, fontti, screen)
            if step == 1:
                y += 40
            elif step == 3:
                y += 20
            else:
                y += 10
            step += 1

    def add_lvl(self):
        
        self.lvl += 1
        self.price = round(self.alku_hinta * self.lvl * 0.75)
        data.add_level(self.name, self.price)

    
    def ruutu(self, screen, x, y):
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    
    

Peli()