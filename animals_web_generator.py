import data_fetcher

def serialize_animal(animal_obj):
    """Converts an animal dictionary into an HTML <li> element for display on the website."""
    output = [] #Initialize an empty list
    output.append('<li class="cards__item">\n')
    output.append(f'<div class="card__title">{animal_obj.get("name", "Unknown Animal")}</div>\n')
    output.append('<p class="card__text">\n')

    # Diet
    if animal_obj.get("characteristics") and "diet" in animal_obj["characteristics"]:
        output.append(f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n')

    # Location
    if isinstance(animal_obj.get("locations"), list) and animal_obj["locations"]:
        output.append(f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n')

    # Type
    if animal_obj.get("characteristics") and "type" in animal_obj["characteristics"]:
        output.append(f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n')

    output.append('</p>\n')
    output.append('</li>\n')
    return ''.join(output)  # Join all elements of the list into a single string


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
        print("Error: Placeholder '__REPLACE_ANIMALS_INFO__' not found in the template. Please check your template.")
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