import requests, json
from geopy.geocoders import Nominatim


class Location:
    def __init__(self):
        self.lat = self.set_current_location()[0]
        self.lng = self.set_current_location()[1]
        self.address = self.set_address()
        self.geolocoder = Nominatim(user_agent="South Korea", timeout=None)

    def set_address(self):
        address = self.geolocoder.reverse(f"{self.lat}, {self.lng}")
        return address

    def set_current_location(self):
        crd = self._current_location()
        return crd["lat"], crd["lng"]

    def _current_location(self):
        url = "http://www.geoplugin.net/json.gp"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to get current location")
        else:
            location = json.loads(response.text)
            crd = {
                "lat": str(location["geoplugin_latitude"]),
                "lng": str(location["geoplugin_longitude"]),
            }
            return crd
