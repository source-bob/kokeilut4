import mysql.connector
from flask import Flask, request

app = Flask(__name__)
@app.route('/hae_tiedot/<koodi>')

def hae_tiedot(koodi):
    sql = f'SELECT name, municipality FROM airport WHERE ident="{koodi}"'

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    pää_tulos = tulos[0]
    palu = f'"ICAO": "{koodi}", "Name": "{pää_tulos[0]}", "Municipality": "{pää_tulos[1]}"'
    return palu


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456789',
    database='flight_game',
    autocommit=True
)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)