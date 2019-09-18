import reverse_geocoder as rg
import json

def reverse_geocode(lat, lng):
    res = rg.search((lat, lng))[0]
    res = list(res.items())
    name = res[2][1]
    admin1 = res[3][1]
    cc = res[5][1]
    return (name, admin1, cc)

graph = dict()

with open('data.json','r') as f:
    datastore = json.load(f)
    bus_list = datastore['busDetails']
    for bus in bus_list:
        bus_num = bus['busNum']
        bus_reg_num = bus['busRegNum']
        route_num = bus['routeNum']
        gps = bus['gps']
        lat = bus['lat']
        lng = bus['lng']
        if lat!=None and lng!=None:
            result = reverse_geocode(lat, lng)
            city_name = result[0]
            state = result[1]
            country = result[2]
            place = city_name+','+state+','+country
            vel = gps[108:]
            speed = vel[0:vel.index(' ')]
            speed = float(speed)
            data = { 'lat': lat, 'lng': lng, 'place': place, 'speed': speed }
            graph[int(bus_num)] = data

with open('mapping.json', 'w') as f:
    json.dump(graph, f)

