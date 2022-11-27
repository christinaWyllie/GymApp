import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(user = 'final', password = 'cpsc', 
                                        host = '127.0.0.1', database = 'gym_database')
    if connect.is_connected():
        print(connect.get_server_info())
        
except Error as e:
    print("Error occured while connecting.\n username, password or database name incorrect.\n")


connect.close()