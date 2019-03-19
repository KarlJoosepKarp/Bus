import requests
import datetime

bus_stations = {
    "keemia": [59.3969, 24.6664],
    "baltijaam": [59.4398, 24.7378],
    "vambola": [59.3997, 24.6901],
    "akadeemiatee": [59.4013, 24.6599],
    "lepistiku": [59.4031, 24.6988],
    "bussijaam": [59.4268, 24.7709]

}


class Location:

    def __init__(self):
        """Construtor."""
        self.dep_x = 0
        self.dep_y = 0
        self.arrival_x = 0
        self.arrival_y = 0
        self.app_id = "qA3CXfaPayS5ICW64N5y"
        self.app_code = "Bw2qNWvlHYjkC_NRlbkn0Q"
        self.time = datetime.datetime.now().isoformat()

    def find_deb_coordinates(self, start):
        for keys, values in bus_stations.items():
            if keys == start:
                self.dep_x = bus_stations.get(keys)[0]
                self.dep_y = bus_stations.get(keys)[1]

    def find_arrival_coordinates(self, end):
        for keys, values in bus_stations.items():
            if keys == end:
                self.arrival_x = bus_stations.get(keys)[0]
                self.arrival_y = bus_stations.get(keys)[1]

    def next_departures(self, start, end):
        self.find_arrival_coordinates(start)
        self.find_deb_coordinates(end)
        debartures = []
        api_request = requests.get(
            f"https://transit.api.here.com/v3/route.json?dep={self.dep_x}%2C%20{self.dep_y}&arr={self.arrival_x}%2C%20{self.arrival_y}&time={self.time}&app_id={self.app_id}&app_code={self.app_code}&routing=all").json()
        for connection in api_request["Res"]["Connections"]["Connection"]:
            message = ""

            message += "Bus: "+connection["Sections"]["Sec"][1]["Dep"]["Transport"]["name"]+" -"
            message += connection["duration"]+"  "
            message += connection["Dep"]["time"]
            message += "->"
            message += connection["Arr"]["time"]
            debartures.append(message)
            message = ""
        print(debartures)
        return debartures


