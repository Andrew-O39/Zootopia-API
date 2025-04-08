# Zootopia Animals' Data Web Generator

This project generates a website that displays information about animals fetched from the [API Ninjas Animals API](https://api.api-ninjas.com/v1/animals). The website lets users input the name of an animal, and the corresponding details about a user-selected animal is fetched and displayed dynamically.

## Features

The Program:
- Takes user input for an animal name
- Fetches animal data from the API
- Displays diet, location, and type in a styled website
- Handles invalid input or animals not found gracefully
- API key securely managed using `.env`
- Modular code with `fetch_animal_data()` and `serialize_animal()` separation
- Basic error handling for file access and network issues

---

## Technologies Used

- Python 3
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- HTML (template-based)
- [API Ninjas - Animals API](https://api.api-ninjas.com/v1/animals)

---

## Getting Started

### 1. Clone the Repository
First, clone the project repository to your local machine using:

- git clone https://github.com/Andrew-O39/Zootopia-API.git
- cd Zootopia-API

### 2. Install Dependencies
Install the required Python dependencies using: pip install -r requirements.txt

### 3. Run the Website Generator
To generate the website, simply run the Python script that fetches the animal data and generates the HTML file using: python animals_web_generator.py.

### 4. Enter the Animal Name
When prompted, enter the name of an animal (e.g., “cheetah”, “fox”, "lion") to retrieve its data. The script will fetch the data from the API and generate an HTML file displaying the information.
If no animal data is found, the website will display a friendly message saying that the animal does not exist. Moreover, if no animal name is entered, the website will display a friendly message to remind you that you did not enter any animal name.

## Contributing

Contributions are warmly welcome! If you would like to contribute to this project, please follow these guidelines:
1. **Fork the repository:**
   - Click the "Fork" button on the GitHub page to create a copy of this repository under your own GitHub account.

2. **Clone your fork:**
   - Clone your fork to your local machine.
   
3. **Create a new branch:**
   - Create a new branch for the feature or fix you want to work on.

4. **Make your changes:**
   - Implement your changes in the codebase. Be sure to test thoroughly to ensure it works as expected.
   
5. **Commit your changes:**
   - Commit your changes with a meaningful commit message.

6. **Push to your fork:**
   - Push your changes back to your fork.
   
7. **Submit a Pull Request:**
   - Go to the GitHub repository where you forked the project and submit a Pull Request (PR) with a description of what you’ve done.
   
Note:
   - 1. Make sure your changes are aligned with the project’s style and don’t break existing functionality. 
     2. Make sure that your contributions follow PEP 8 coding conventions. 
     3. Make your PRs are small and focused so that I can easily review and merge them. Thanks in advance.