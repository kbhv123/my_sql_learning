import mysql.connector
import os


def conn_to_database():

    db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd= os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
    )

    mycursor = db.cursor()

    return mycursor,db

#mycursor.execute("CREATE DATABASE User_Profiles")



#mycursor.execute("CREATE TABLE ACCOUNT (username VARCHAR(255) NOT NULL, password_hash VARCHAR(255) NOT NULL, account_ID int PRIMARY KEY AUTO_INCREMENT)")