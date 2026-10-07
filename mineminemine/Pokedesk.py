import json
import os

idinuse = 0
language = ("none")

menu = "\npress any button to continue"

def open_file():
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, "pokedex.json")
    with open(path, "r", encoding="utf-8") as file:
        pokemon_data = json.load(file)
        return pokemon_data

def search_type(pokemon_data):
    search_type = input("Enter Pokémon type: ").capitalize()
    print(f"\nPokémon with type {search_type}:")
    for pokemon in pokemon_data:
        if search_type in pokemon["type"]:
            print(pokemon["name"]["english"])
            print(pokemon["description"])

def search_name(pokemon_data):
    search_name = input("Name?: ").capitalize()
    for pokemon in pokemon_data:
        if search_name == pokemon["name"][language]:
            print(pokemon["name"][language])
            print(pokemon["id"])
            print(pokemon["type"])
            print(pokemon["base"])
            return int(pokemon["id"])

def search_id(pokemon_data):
    idsearch = int(input("ID?: "))
    for pokemon in pokemon_data:
        if idsearch == pokemon["id"]:
            print(pokemon["name"]["english"])
            return pokemon["id"]

pokedesk = open_file()

def Lname():
    lan = ("none")
    choice = int(input("Select your language\n" \
    "1 - English\n" \
    "2 - Japanese\n" \
    "3 - Chinese\n" \
    "4 - French\n" \
    "Choice: "))
    if choice == 1:
        lan = ("english")
    elif choice == 2:
        lan = ("japanese")
    elif choice == 3:
        lan = ("chinese")
    elif choice == 4:
        lan = ("french")
    else:
        print("ERROR, FAILED TO SELECT A LANGUAGE")
    return lan
language = Lname()

print("\n\n")
while True:
    print("\n ★ ⋆˚꩜｡ Global Pokédex ⋆˚꩜｡ ★\n"
    "1 - search by name\n"
    "2 - search by type\n"
    "3 - search by id\n"
    "4 - reselect language\n"
    "5 - creature data in current id")
    if idinuse >= 1:
        print("id - ", idinuse)
    choice = int(input("choice: "))

    if choice == 1:
        idinuse = int(search_name(pokedesk))
        input(menu)

    elif choice == 2:
        search_type(pokedesk)
        input(menu)

    elif choice == 3:
        idinuse = int(search_id(pokedesk))
        input(menu)

    elif choice == 4:
        language = Lname()
        print("Language selected: ", language)
        input(menu)

    elif choice == 5:
        for pokemon in pokedesk:
            if idinuse == pokemon["id"]:
                    print(pokemon)
                    #str("ID: ")+str(pokemon["id"])+str("\n")+str("Name: ")+str(pokemon["name"][language])+str("\n")+str("Type: ")+str(pokemon["type"])+"\n"+str("Species: ")+str(pokemon["species"])+str("\n")
        input(menu)

    else:
        break