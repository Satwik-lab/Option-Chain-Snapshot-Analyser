import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root", password="satwik@2006",)
print("Connector version:", mysql.connector.__version__)
print("Server connected :", conn.is_connected())
cur = conn.cursor()
cur.execute("SELECT VERSION()")
print("MySQL server   :", cur.fetchone()[0])
cur.close()
conn.close()