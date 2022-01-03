import mysql.connector

conn = mysql.connector.connect(host = 'localhost',username = 'root',password = 'anu_2001',database = 'student')
my_cur = conn.cursor()

conn.commit()
conn.close()

print("suc")