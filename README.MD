# Random Recipe Generator

This is a simple Python application that generates random food recipes using the Spoonacular API. Users can fetch random recipes from the API, view them in the application, and save them to a local SQLite database for future reference.

## Features

- Fetch random recipes from the Spoonacular API.
- View recipe details including title, ingredients, and instructions.
- Save fetched recipes to a local SQLite database.
- Retrieve and display random recipes from the local database.

## Requirements

- Python 3.x
- tkinter library (for GUI)
- Pillow library (for image processing)
- requests library (for making HTTP requests)
- Spoonacular API key

## Installation

1. Clone or download the repository to your local machine.
2. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Obtain a Spoonacular API key from [Spoonacular website](https://spoonacular.com/food-api) and replace `"YOUR_API_KEY_HERE"` with your actual API key in the `main.py` file.

4. Run the `main.py` script to launch the application:

    ```
    python main.py
    ```

## Usage

- Click on the "Fetch Recipes" button to fetch random recipes from the Spoonacular API.
- Click on the "Show Random Recipe" button to display a randomly selected recipe fetched from the API.
- View recipe details including title, ingredients, and instructions in the application window.
- Fetched recipes are automatically saved to the local SQLite database for future reference.
- You can view previously saved recipes by launching the application.
