import mysql.connector
import random

def airport_name_city(country):
    try:
        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='demogame',
            user='root',
            password='',
            autocommit=True
        )
        cursor = yh.cursor()


        sql = f"SELECT airport.name, airport.municipality FROM airport INNER JOIN country ON country.iso_country = airport.iso_country WHERE country.name = '{country}'"
        cursor.execute(sql)
        airports = cursor.fetchall()

        #
        if airports:
            random_airport = random.choice(airports)
            airport_name, municipality = random_airport[0], random_airport[1]

            return airport_name, municipality
        else:
            print("No airports found in this country.")

        cursor.close()
        yh.close()

    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")