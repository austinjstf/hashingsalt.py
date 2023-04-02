#Importing connector.
import mysql.connector 
import secrets

#Variable for salt.
salt = secrets.token_hex(16)

#Connecting to Mysql Database.
mysqlconn = mysql.connector.connect(host="localhost", username="", password="", database = "")
mysqlcursor = mysqlconn.cursor()

#Sql statement.
sql = ("INSERT INTO 'TableName' (Username, Password) VALUES (userName, hashedPassword)")

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

userName = input("Username?")
passWord = input("Password?")
#Built in hashing algorithm python has + salt from above.
hashedPassword = hash(passWord + salt)

print("Your account has been created now")

#Just confirming down below here.
print(userName)
print(passWord)
print(hashedPassword)