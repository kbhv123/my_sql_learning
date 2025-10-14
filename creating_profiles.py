from profile_database import *

def creating_account():

    username = input("Please type in a username ")
    password = input("Please type in a password ")

    db_conn,db_commit = conn_to_database()

    db_conn.execute("INSERT INTO account(username,password_hash) VALUES (%s,%s)", (username, password))
    db_commit.commit()

    print (f"Account Created with {username}")



creating_account()