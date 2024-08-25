import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port = 3306,
    database = 'ihmiset',
    user = 'artemlu',
    password = '123456',
    autocommit = True
)