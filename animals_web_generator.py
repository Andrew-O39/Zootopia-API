import data_fetcher


def serialize_animal(animal_obj):
    """Converts an animal dictionary into an HTML <li> element for display on the website.
    Parameters:
        animal_obj (dict): A dictionary containing information about a single animal.
                           Expected keys include 'name', 'characteristics', and 'locations'.
    Returns:
        A string of HTML representing the animal, including its name, diet, location, and type."""

    output = '' # Start with an empty string
    output += '<li class="cards__item">\n' # Add opening <li> tag
    output += f'<div class="card__title">{animal_obj.get("name", "Unknown Animal")}</div>\n' # Add title
    output += '<p class="card__text">\n'  # Add opening <p> tag

    # Diet
    if animal_obj.get("characteristics") and "diet" in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    # Location
    if isinstance(animal_obj.get("locations"), list) and animal_obj["locations"]:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    # Type
    if animal_obj.get("characteristics") and "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '</p>\n'  # Close <p> tag
    output += '</li>\n' # Close <li> tag

    return output # Return the complete HTML string for the animal


def main():
    name = input("Enter a name of an animal: ").strip()
    try:
        with open("animals_template.html", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Template file not found.")
        return

    if not name:
        print("No animal name entered.")
        output = "<h2>No animal name entered.</h2>"

    else:
        animals_data = data_fetcher.fetch_animal_data(name)

        if not animals_data:
            output = f'<h2>The animal "{name}" does not exist. Would you like to try a different animal?</h2>'
        else:
            output_lines = [serialize_animal(animal) for animal in animals_data]
            output = ''.join(output_lines)

    # Replace placeholder with generated animal information
    if "__REPLACE_ANIMALS_INFO__" not in template_content:
        print("Warning: Placeholder '__REPLACE_ANIMALS_INFO__' not found in template.")
        return
    updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    try:
        # Write new content to "animals.html"
        with open("animals.html", "w") as output_file:
            output_file.write(updated_html)
        print("Successfully generated 'animals.html'")
    except Exception as e:
        print(f"Error: Failed to write 'animals.html': {e}")

# Run the main program
if __name__ == "__main__":
    main()