import mysql.connector
from mysql.connector import Error

def date_goal(first_name, level, cont, city2,ident,player_points,player_fuel):
    try:

        yh = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='demogame',
            user='root',
            password='',
            autocommit=True
        )

        if yh.is_connected():
            cursor = yh.cursor()

            query = "INSERT INTO player_goal (first_name, player_level, continet, airport_name, ident,player_points,player_fuel) VALUES (%s, %s, %s, %s, %s,%s,%s)"
            value = (first_name, level, cont, city2, ident,player_points,player_fuel)

            cursor.execute(query, value)
            yh.commit()

            print("DATA INSERTED CORRECTLY..")

    except Error as e:
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()