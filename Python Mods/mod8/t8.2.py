import mysql.connector

def hae_maa(koodi):
    sql = f'SELECT type, count(*) FROM airport WHERE iso_country="{koodi}" GROUP BY type ORDER BY count(*) DESC'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'airport type: {rivi[0]} ({rivi[1]} kpl)')

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345678',
    autocommit=True
)

kood = input('anna koodi: ')
hae_maa(kood)