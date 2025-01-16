
import mysql.connector
from mysql.connector import Error

def incrementar_columna(ident, player_points):
    try:
        # Conexión a la base de datos
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

            # Incrementar el valor de la columna "score"
            incrementar_query = "UPDATE player_goal SET player_points = player_points + %s WHERE ident = %s"
            cursor.execute(incrementar_query, (player_points, ident))
            yh.commit()

            print("Valor incrementado correctamente.")

    except Error as e:
        print(f"Error connecting to database: {e}")
        if yh.is_connected():
            yh.rollback()

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()