import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    database='demogame',
    autocommit=True
)

def universal_execute(kysely, palaute=False):
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(kysely)
    if palaute:
        res = cursor.fetchall()
        return res
    
def clear_data():
    kyselyt = [
        'SET FOREIGN_KEY_CHECKS = 0;',
        'TRUNCATE TABLE property;',
        'TRUNCATE TABLE ports;',
        'TRUNCATE TABLE player;',
        'SET FOREIGN_KEY_CHECKS = 1;'
    ]

    for kysely in kyselyt:
        universal_execute(kysely)

def get_zones():
    kysely = '''WITH random_countries AS (
SELECT c.iso_country
FROM country c
INNER JOIN airport a ON c.iso_country = a.iso_country
WHERE a.type!="closed"
GROUP BY c.iso_country
HAVING COUNT(a.id) > 2
ORDER BY RAND()
LIMIT 9
)
SELECT rc.iso_country, COUNT(a.id) AS airport_count
FROM random_countries rc
INNER JOIN airport a ON rc.iso_country = a.iso_country
GROUP BY rc.iso_country
ORDER BY airport_count;'''

    return universal_execute(kysely, True)

def get_ports():
    zones = get_zones()
    ports = []
    i = 1
    for zone in zones:
        kysely = f'''SELECT a.iso_country, a.name AS airport_name, a.type, c.name AS country_name, a.ident
FROM airport a
LEFT JOIN country c ON a.iso_country = c.iso_country
WHERE a.iso_country = "{zone['iso_country']}"
AND a.type !="closed"
ORDER BY RAND()
LIMIT 2;'''
        airports = universal_execute(kysely, True)
        for airport in airports:
            cost = i * 15 + 40
            ports.append(airport)
            add_port(a_name=airport['airport_name'], a_type=airport['type'], country_name=airport['country_name'], iso=airport['iso_country'], price=cost, ident=airport['ident'])
            i += 1
    return ports

def add_port(a_name=None, a_type=None, country_name=None, iso=None, price=None, id=None, ident=None, push=False, owner=None, lvl=1):
    if push:
        kyselyt = [
            f'''UPDATE ports
            SET id = id + 1
            WHERE id>={id}
            ORDER BY id DESC;''',
            f'''INSERT INTO ports (id, name, type, owner)
            VALUES ({id}, "{a_name}", "{a_type}", "{owner}")'''
            ]
        for kysely in kyselyt:
            universal_execute(kysely)
    elif not push:
        kysely = f'''INSERT INTO ports (name, type, country, iso_country, price, ident, lvl)
        VALUES ("{a_name}", "{a_type}", "{country_name}", "{iso}", {price}, "{ident}", {lvl})'''
        universal_execute(kysely)

def create_board():
    map = {
        1: 'start',
        4: 'bonus',
        7: 'bill',
        10: 'airbus',
        13: 'bonus2',
        15: 'rent',
        18: 'billx2',
        21: 'chance',
        24: 'kirppis',
        26: 'bonus3'
    }
    for item in map:
        add_port(a_name=map[item], a_type=map[item], push=True, id=item, owner='not availible')

def get_info(base, port=None):
    if port:
        kysely = f'''SELECT * FROM {base}
WHERE id={port}'''
    elif not port:
        kysely = f'''SELECT * FROM {base}'''
    res = universal_execute(kysely, True)
    return res

def new_char(name):
    kysely = f'''INSERT INTO player (name, money, position) VALUES ("{name}", {1510}, {0})'''
    universal_execute(kysely)

def get_info_pl(id):
    kysely = f'''SELECT * FROM player
    WHERE NAME="player {id}"'''
    res = universal_execute(kysely, True)
    return res

def get_pos(id):
    kysely = f'''SELECT position FROM player
    WHERE NAME="player {id}"'''
    res = universal_execute(kysely, True)
    return res[0]['position']

def change_position(id, amount):
    kysely = f'''UPDATE player
    SET position = position + {amount}
    WHERE NAME="player {id}"'''
    universal_execute(kysely)

def set_position(id):
    kysely = f'''UPDATE player
    SET position = 0
    WHERE NAME="player {id}"'''
    universal_execute(kysely)

def add_money(id, amount):
    kysely = f'''UPDATE player
    SET money = money + {amount}
    WHERE NAME="player {id}"'''
    universal_execute(kysely)

def render_text_in_box(text, x, y, max_width, fontti, screen, rev=False):
        words = text.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            test_line = current_line + word + ' '
            width, _ = fontti.size(test_line)

            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

        if current_line:
            lines.append(current_line)

        for i, line in enumerate(lines):
            if rev:
                teksti = fontti.render(line, True, (255, 255, 255))
            elif not rev:
                teksti = fontti.render(line, True, (0, 0, 0))
            screen.blit(teksti, (x, y + i * fontti.get_height())) 



def add_property(name, port):
    kyselyt = [
        f'''INSERT INTO property (owner, id) VALUES ("{name}", {port.id})''',
        f'''UPDATE ports SET owner = "{name}" WHERE id = {port.id}'''
        ]
    for kysely in kyselyt:
        universal_execute(kysely)
    port.set_params()

def get_property(p_name):
    kysely = f'''SELECT id, name
    FROM ports
    WHERE id IN(   
        SELECT id 
        FROM property
        WHERE owner = "{p_name}"
	);'''
    res = universal_execute(kysely, True)
    ports = []
    for port in res:
        ports.append((port['id'], port['name']))
    return ports

def add_level(port_name, port_price):
    kysely = f'UPDATE ports SET lvl = lvl + 1, price = {port_price} WHERE name = "{port_name}"'
    universal_execute(kysely)

def delete_owner(prop ,id):
    kyselyt = [
        f'DELETE FROM property WHERE id = {id}',
        f'UPDATE ports SET owner = NULL WHERE id = {id}'
        ]
    for kysely in kyselyt:
        universal_execute(kysely)

def get_player_prope(p_name):
    kysely = f'''SELECT name, price
    FROM ports
    WHERE id IN(
    SELECT id
    FROM property
    WHERE owner="{p_name}")'''

    res = universal_execute(kysely, True)
    return res

def save_results(round, player, prop_money, upd=False):
    kysely = '''INSERT INTO airpoly_results (pyörät, voittaja, pääoma) VALUES (%s, %s, %s);'''
    universal_execute(kysely)

def get_round():
    kysely = '''SELECT pyörät FROM airpoly_results
    ORDER BY peli_id DESC
    LIMIT 1'''
    
    res = universal_execute(kysely, True)[0]['pyörät']
    return res



def save_game(round, player_name=None, prop_money=None, exit=False):
    kysely = '''SELECT voittaja FROM airpoly_results
    ORDER BY peli_id DESC
    LIMIT 1'''

    res = universal_execute(kysely, True)
    
    if exit:
        if len(res) == 0:
            save_results(round, 'not finished', 0)
        elif len(res) == 1:
            name = res[0]['voittaja']
            if name == 'not finished':
                update_last(round, 'not finished', 0)
            elif name != 'not finished':
                save_results(round, 'not finished', 0)
    elif not exit:
        if len(res) == 0:
            save_results(round, player_name, prop_money)
        elif len(res) != 0:
            name = res[0]['voittaja']
            if name == 'not finished':
                update_last(round, player_name, prop_money)
            elif name != 'not finished':
                save_results(round, player_name, prop_money)



    
def update_last(round, player_name=None, prop_money=False):
    kysely = f'''UPDATE airpoly_results
    SET pyörät = {round}, voittaja = "{player_name}", pääoma = {prop_money}
    WHERE peli_id = (SELECT MAX(peli_id) FROM airpoly_results)'''
    universal_execute(kysely)

def count_prope(name):
    data = get_player_prope(name)
    capital = 0
    for item in data:
        capital += item['price']
    return capital

def get_results():
    kysely = 'SELECT * FROM airpoly_results'
    res = universal_execute(kysely, True)
    if len(res) == 0:
        res = 'nothing to show'
    return res