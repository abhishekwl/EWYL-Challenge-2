from flask import Flask, render_template
import json

app = Flask(__name__)
datastore = json.load(open('mapping.json', 'r'))

@app.route('/api/bus/<number>', methods=['GET'])
def get_bus(number):
    try:
        bus = datastore[number]
        lat = float(bus['lat'])
        lng = float(bus['lng'])
        place = bus['place'].replace(',', ', ')
        speed = bus['speed']
        data = { 'success': True, 'error': None, 'id': number, 'latitude': lat, 'longitude': lng, 'place': place, 'speed': speed }
        return data
    except KeyError:
        return { 'success': False, 'error': 'Invalid bus number' }

@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
