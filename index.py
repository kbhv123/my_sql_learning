import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase1"
)


mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testdatabase1")

#mycursor.execute("CREATE TABLE PERSON (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DESCRIBE PERSON")
#for x in mycursor:
    #print(x)

#mycursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)", ("Tim", 19))
#mycursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)", ("Joe", 22))
#db.commit()

mycursor.execute("SELECT * FROM person")

for x in mycursor:
    print(x)
