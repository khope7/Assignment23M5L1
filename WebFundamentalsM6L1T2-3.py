# Task 3: Data Presentation and Analysis - Perform a simple analysis, such as finding the planet with the longest orbit period or the heaviest planet. 

# import requests

# def fetch_planet_data():
#     # Enhance format the output in a more readable manner
#     return #list of planets

# def find_heaviest_planet(planets):
#     return #heaviest planet

# planets = fetch_planet_data()
# name, mass = find_heaviest_planet(planets)
# print(f"The heaviest planet is {name} with a mass of {mass} kg.")

#Writing code for WebFundamentals Task2.3

import requests

def fetch_planet_data():
    planet_names = []
    planet_sizes = []
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

#process each planet info
    count = 0
    for planet in planets:
        if planet['isPlanet']:
            count += 1
            name = planet.get("englishName") #get planet English name
            mass = planet['mass']['massValue'] #get planet mass
            orbit_period = planet.get("sideralOrbit") #get planet orbit period
            print(f"Planet {count}: {name}\n\tMass: {mass}\n\tOrbital Period: {orbit_period}\n")

            size = planet['mass']['massValue']
            planet_names.append(name)
            planet_sizes.append(size)

    return planet_names, planet_sizes

def find_heaviest_planet(names, masses):

    mass = max(masses)
    
    heaviest_planet = names[masses.index(mass)]

    print(f"The heaviest planet is {heaviest_planet} with a mass of {mass} kg.")

names, masses = fetch_planet_data()

find_heaviest_planet(names, masses)

