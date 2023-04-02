#Importing connector.
import mysql.connector 
import secrets

#Variable for salt.
salt = secrets.token_hex(16)

#Connecting to Mysql Database.
mysqlconn = mysql.connector.connect(host="localhost", username="asteffes", password="asteffes", database = "asteffes")
mysqlcursor = mysqlconn.cursor()

#Sql statement.
sql = ("INSERT INTO hashsaltpy (uName, pWord) VALUES (uName, temp)")

#Executing changes to database.
mysqlcursor.execute(sql)

#Commit changes to database.
mysqlconn.commit()

#Close cursor and connection to database.
mysqlcursor.close()
mysqlconn.close() 

import secrets
salt = secrets.token_hex(16)

print("Hello, you are creating your username and password here:")

uName = input("Username?")
pWord = input("Password?")
#Built in hashing algorithm python has + salt from above.
temp = hash(pWord + salt)

print("Your account has been created now")

#Just confirming down below here.
print(uName)
print(pWord)
print(temp)