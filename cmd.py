import sys
import json

datastore = json.load(open('mapping.json', 'r'))

def lookup(bus_number):
    bus = datastore[bus_number]
    if bus==None:
        print('Invalid Bus Number')
        exit()
    lat = bus['lat']
    lng = bus['lng']
    place = bus['place'].replace(',', ', ')
    speed = bus['speed']
    print('Location: {}, {}'.format(lat, lng))
    print('Place: {}'.format(place))
    if speed==0:
        print('Moving: False')
        print('Velocity: 0')
    else:
        print('Moving: True')
        print('\x1b[6;30;42m'+'Velocity: '+str(speed)+' km/hr'+'\x1b[0m')

if __name__ == "__main__":
    print()
    if len(sys.argv)==1:
        print('Missing parameter: bus number')
        print('USAGE: python3 cmd.py [BUS_NUMBER]')
        exit()
    else:
        bus_num = sys.argv[1]
        lookup(bus_num)
        print()
