import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load animal data from the JSON file
animal_date = load_data("animals_data.json")

# Read the content of the animals_template.html
with open("animals_template.html","r") as file:
    read_html = file.read()


def display_animals_info(animal_info):
    """
    Displays selected info about each animal
    """

    # define an empty string
    output = ""

    for animal in animal_info:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        location = animal.get("locations",[])[0]
        animal_type = animal.get("characteristics", {}).get("type")

        # append information to each string
        output += "<li class='cards__item'>"
        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet : {diet}<br/>\n"
        if location:
            output += f"Location : {location}<br/>\n"
        if animal_type:
            output +=f"Type : {animal_type}<br/>\n"
        output += "</li>"
    return output

animals_short_info = display_animals_info(animal_date)
print(animals_short_info)


# Replace text in html with extracted info
main_html = read_html.replace("__REPLACE_ANIMALS_INFO__", animals_short_info)
print(main_html)

# Write the new HTML content to a new file, main.html
with open("main.html", "w") as final_file:
    final_file.write(main_html)
