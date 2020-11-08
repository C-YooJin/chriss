import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np

def Excel_Out(connection, startDt, endDt):
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            print(startDt)
            print(type(startDt))
            cursor.execute(("select * from covid.epidemiology where input_date between (%s) and (%s) order by input_date desc;"),(startDt,endDt))
            record = cursor.fetchall()
            print("You're connected to database: ", record)
            print(type(record))

            print(startDt, endDt)
            # list에 header붙여서 excel로 내보내면 될


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