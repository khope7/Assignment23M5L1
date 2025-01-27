# Task 3: Analyzing and Displaying Data
# 1. Modify the script to fetch data for three different Pokémon.
# 2. Create a function to calculate and return the average weight of these Pokémon.
# 3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**
# def fetch_pokemon_data(pokemon_name):
#     return #json response
# def calculate_average_weight(pokemon_list):
#     return #average weight
# pokemon_names = ["pikachu", "bulbasaur", "charmander"]
# Expected Outcome: The script should display the names and abilities of the three chosen Pokémon and their average weight.
# The function should correctly calculate and return the average weight based on the data fetched from the API. 


#Writing code for WebFundamentals Task1.3


import requests
import json

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    try:
        for name in pokemon_name:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            json_data = response.text

            pokemon_data = json.loads(json_data)

            print(f"Pokemon name: {pokemon_data["name"].title()}\n")
            print(f"Pokemon Abilities: {pokemon_data["abilities"]}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def calculate_average_weight(pokemon_list):
    total_weight = 0
    try:
        for element in pokemon_list:        
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{element}")
            json_data = response.text

            pokemon_data = json.loads(json_data)
            print(f"Pokemon {element.title()}'s weight:")
            print(pokemon_data["weight"])

            total_weight += int(pokemon_data["weight"])
        
        average_weight = total_weight / 3

        print(f"Pokemon total average weight: {average_weight:.2f}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


fetch_pokemon_data(pokemon_names)
calculate_average_weight(pokemon_names)






