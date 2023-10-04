import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Anfinsen", database="AJ");
mycursor = mydb.cursor()

#mycursor.execute("""insert into iphone(S_NO, NAME, RAM, STORAGE)
#values(2,'iphone12','6GB','512 GB')""")
mycursor.execute("select * from iphone")
for x in mycursor:
    print(x)
