from flask import jsonify
import mysql.connector

def allBookings(config):
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)
    cur.execute("SELECT * FROM booking")
    results = cur.fetchall()
    bookings = []
    for row in results:
        booking = {
            'id': row[0],
            'compensations': row[1],
            'booking_request_id': row[2],
        }
        bookings.append(booking)

    cur.close()
    cnx.close()

    return jsonify({'bookings': bookings})