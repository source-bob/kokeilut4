import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    passwd = 'urkqsrk1029',
    autocommit = True
)

def hae_geo(koodi, koodi2):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident="{koodi}" or ident="{koodi2}";'


    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    points = []
    if kursori.rowcount > 0:
        for rivi in tulos:
            points.append(rivi)
    if points:
        ensi_points = points[0]
        toka_points = points[1]

        distance = geodesic(ensi_points, toka_points).kilometers

        print(f'Distance between {koodi} and {koodi2} is: {distance:.2f} km')

kood = input('anna koodi: ')
kood2 = input('anna toinen koodi: ')

hae_geo(kood, kood2)