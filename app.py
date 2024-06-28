import requests
import geocoder

API_KEY = 'da3a7df90e87c269d5e1f792410788f3'


def get_location():
    g = geocoder.ip('me')
    print(g.latlng)


def main():
    location = get_location()
    if location:
        lat, lon = location
        print(location)

get_location()