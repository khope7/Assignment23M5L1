# Task 2: Fetching Data from the Pokémon API
# 1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).
# 2. Extract and print the name and abilities of the Pokémon.
# Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

#Writing code for WebFundamentals Task1.2

import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

json_data = response.text

pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["abilities"])




