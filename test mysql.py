
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Anfinsen",
  database="AJ"
)

mycursor = mydb.cursor()

sql = "INSERT INTO iphone (S_NO ,NAME ,RAM ,STORAGE) VALUES (%s, %s, %s, %s)"
val = (2,"12 pro","4GB","256GB")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

