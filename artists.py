from flask import jsonify
import mysql.connector

def allArtists(config):
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)
    cur.execute("SELECT * FROM artist")
    results = cur.fetchall()
    artists = []
    for row in results:
        artist = {
            'id': row[0],
            'email': row[1],
            'name': row[2],
            'password': row[3],
            'description': row[4],
            'genre': row[5],
            'rekening_nummer': row[6],
            'type_act': row[7]
        }
        artists.append(artist)

    cur.close()
    cnx.close()

    return jsonify({'artists': artists})