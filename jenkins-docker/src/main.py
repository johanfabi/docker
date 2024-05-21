"""
This module fetches data from the PokeAPI and prints information about a specific Pokemon.
"""

import requests


URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    name = data["name"]
    species = data["species"]["name"]
    types = [t["type"]["name"] for t in data["types"]]

    print(f"Nombre: {name}")
    print(f"Especie: {species}")
    print(f"Tipos: {', '.join(types)}")
else:
    print("Error al obtener los datos de la API")
