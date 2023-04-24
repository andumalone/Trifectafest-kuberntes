from flask import Flask , jsonify
import rahul
import andu
import toon
import bookings
import tickets
import artists
app = Flask(__name__)

config = {
    'user': 'test',
    'password': 'Passw0rd',
    'host': 'yc2303.mysql.database.azure.com',
    'database': 'test'
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

@app.route("/rahul")
def rahul1():
    return rahul.functie1()

@app.route("/andu")
def andu1():
    return andu.functie2()

@app.route("/toon")
def toon1():
    return toon.functie3()

@app.route('/artists', methods=['GET'])
def get_artists():
    result = artists.allArtists(config)
    return result

@app.route("/bookings", methods=['GET'])
def get_bookings():
    result = bookings.allBookings(config)
    return result

@app.route("/tickets", methods=['GET'])
def get_tickets():
    result = tickets.allTickets(config)
    return result

if __name__ == '__main__':
    app.run(debug=True)
