import requests



api= "https://pokeapi.co/api/v2/pokemon/ditto"

list_pokemon= requests.get(api)


data=list_pokemon.json()


print(data['name'])


