
from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = float(luku)
        is_prime = True
        if luku < 2:
            is_prime = False
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                is_prime = False

        tilakoodi = 200
        vastaus = {
            'status': tilakoodi,
            'luku': luku,
            'isPrime': is_prime
        }



    except ValueError:
        tilakoodi = 400
        vastaus = {
            'status': tilakoodi,
            'teksti': 'Virheellinen yhteenlaskettava'
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        'status': '404',
        'teksti': 'Virheellinen päätepiste'
    }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)