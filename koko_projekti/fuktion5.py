import mysql.connector
from mysql.connector import Error

def final_date(ident):
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
            consulta = "SELECT first_name, player_points FROM player_goal WHERE ident = %s "
            cursor.execute(consulta, (ident,))
            resultados = cursor.fetchall()

            if resultados:

                for fila in resultados:
                    print(f"NAME: {fila[0]}, POINTS IS: {fila[1]}")
            else:
                print(f"No data found for the identifier {ident}")

    except Error as e:
        print(f"Error connecting to database: {e}")

    finally:

        if cursor:
            cursor.close()
        if yh.is_connected():
            yh.close()

