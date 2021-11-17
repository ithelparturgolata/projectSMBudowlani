import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Savakiran03", database="bazasm")
cursor = mydb.cursor()

#make a function to access the db
def user_login():
    try:
        cursor.execute("SELECT * FROM uzytkownicy WHERE Uzytkownik = %s AND Haslo = %s")
        return (cursor.fetchone())
    except:
        return False

