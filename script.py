import mysql.connector
from mysql.connector import Error

def Excel_Out(connection, startDt, endDt):
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("select database();")
            cursor.execute("select * from mysql.user;")
            record = cursor.fetchall()
            print("You're connected to database: ", record)

            print(startDt, endDt)







        else:
            print("if connection fail")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        else:
            print("응아니야")