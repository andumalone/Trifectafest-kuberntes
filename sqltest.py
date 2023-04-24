import mysql.connector

config = {
    'user': 'test',
    'password': 'Passw0rd',
    'host': 'yc2303.mysql.database.azure.com',
    'database': 'test'
}

cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
cur.execute("SELECT * FROM artist")
results = cur.fetchall()
for row in results:
    print(row)

cur.close()
cnx.close()