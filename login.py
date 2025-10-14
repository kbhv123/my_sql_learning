from profile_database import *

def login():
    username = input("Please put in your username: ")
    password = input("Please put in your password: ")

    db_conn, _ = conn_to_database()

    query = "SELECT * FROM account WHERE username = %s AND password_hash = %s"
    db_conn.execute(query, (username, password))
    verify = db_conn.fetchone()
    if verify:
        print("Logged in successfully")
    else:
        print("Your username or password is incorrect: ")
        login()

login()