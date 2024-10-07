import mysql.connector
import random
def continet(continent):
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
        sql=f"SELECT DISTINCT country.name FROM country INNER JOIN airport ON country.iso_country = airport.iso_country WHERE airport.continent = '{continent}';  "

        cursor.execute(sql)
        airports = cursor.fetchall()
        if airports:  # Check if there are results
            random_airport = random.choice(airports)  # Choose a random airport
            #print(f"sinun peli alka kaupungissa {random_airport[0]}")  # Print the 'ident' of the random airport
            return random_airport[0]
        else:
            print("No airports found in this continent.")

        cursor.close()
        yh.close()
    except mysql.connector.Error as err:
        print(err.msg)