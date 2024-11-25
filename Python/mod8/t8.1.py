import mysql.connector

def hae_lentokenttä(koodi):
    sql = f'SELECT name, municipality FROM airport WHERE ident="{koodi}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'airport name: {rivi[0]}\nmunicipality: {rivi[1]}')

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '123456789',
    autocommit = True
)

kood = input('anna koodi: ')
hae_lentokenttä(kood)