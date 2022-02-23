import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="Savakiran03",
                               database="bazasm")
cursor = mydb.cursor()

options = []
sql = "SELECT idTresc, naglowekTresc, tekstTresc FROM tresc"
cursor.execute(sql)
ids = cursor.fetchall()
for i in ids:
    options.append(str(i[0]) + "  - " + i[1])

#make a function to access the db
# def user_login():
#     try:
#         cursor.execute("SELECT * FROM uzytkownicy WHERE Uzytkownik = %s AND Haslo = %s")
#         return (cursor.fetchone())
#     except:
#         return False

