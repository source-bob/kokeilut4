import mysql.connector
from mysql.connector import Error
def date(first_name, last_name,ident, age ):
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
            query = "insert into player_information(first_name,last_name,ident, age)VALUES(%s, %s, %s,%s )"
            valores = (first_name, last_name,ident, age)
            cursor.execute(query, valores)
            yh.commit()
            print("DATA INSERTED CORRECTLY..")
    except Error as e:
        print(f"Error connecting to database: {e}")

    finally:
        if yh.is_connected():
            cursor.close()
            yh.close()


