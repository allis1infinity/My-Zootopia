import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load animal data from the JSON file
animal_date = load_data("animals_data.json")

def display_animals_info(animal_info):
    """
    Displays selected info about each animal
    """
    for animal in animal_info:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        location = animal.get("locations",[])[0]
        animal_type = animal.get("characteristics", {}).get("type")

        # print info only if it exists
        if name:
            print(f"Name : {name}")
        if diet:
            print(f"Diet : {diet}")
        if location:
            print(f"Location : {location}")
        if animal_type:
            print(f"Type : {animal_type}")
        print("")

display_animals_info(animal_date)

