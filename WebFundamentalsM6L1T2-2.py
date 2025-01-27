# Task 2: Fetch Data from a Space API Write a Python script that makes a GET request to a space API
# (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.
# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.

# Code Example:
# import requests
# def fetch_planet_data():
#     url = "https://api.le-systeme-solaire.net/rest/bodies/"
#     response = requests.get(url)
#     planets = response.json()['bodies']

##process each planet info
#     for planet in planets:
#         if planet['isPlanet']:
#             name = #get planet English name
#             mass = #get planet mass
#             orbit_period = #get planet orbit period
#             print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# fetch_planet_data()

#Writing code for WebFundamentals Task2.2

import json
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

#process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get("englishName") #get planet English name
            mass = planet.get("mass") #get planet mass
            orbit_period = planet.get("sideralOrbit") #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

