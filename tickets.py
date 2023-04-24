from flask import jsonify
import mysql.connector

def allTickets(config):
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)
    cur.execute("SELECT * FROM ticket")
    results = cur.fetchall()
    tickets = []
    for row in results:
        ticket = {
            'id': row[0],
            'end_date': row[1],
            'start_date': row[2],
            'cutomer_id': row[3],
            'festival_id': row[4],
        }
        tickets.append(ticket)

    cur.close()
    cnx.close()

    return jsonify({'tickets': tickets})