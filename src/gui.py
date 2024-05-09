"""GUI of the Random Recipe Generator."""
import tkinter as tk
from PIL import Image, ImageTk
from src.database import insert_recipe, select_random_recipe
from src.spoonacular_api import fetch_recipes

class RecipeGeneratorApp(tk.Tk):
    """The main application window for the Random Recipe Generator."""
    def __init__(self, api_key):
        super().__init__()
        self.title("Random Recipe Generator")
        self.geometry("650x780")
        self.configure(bg="#E6EBE0")
        self.api_key = api_key

        image = Image.open("src/image.png")
        image = image.resize((100, 100), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self, image=self.photo, bg="#E6EBE0")
        self.image_label.pack(pady=10)

        self.fetch_button = tk.Button(self, text="Fetch Recipes", command=self.fetch_recipes, bg="#FFFFFF",
                                      font=("Comfortaa", 14), relief=tk.RIDGE, bd=0, padx=15,
                                      pady=10, borderwidth=0, highlightthickness=0)
        self.fetch_button.pack(pady=5)

        self.show_button = tk.Button(self, text="Show Random Recipe", command=self.show_random_recipe,
                                     bg="#FFFFFF", font=("Comfortaa", 14), relief=tk.RIDGE,
                                     bd=0, padx=15, pady=10, borderwidth=0, highlightthickness=0)
        self.show_button.pack(pady=5)

        self.title_label = tk.Label(self, text="", font=("Comfortaa", 24, "bold"),
                                    bg="#E6EBE0", fg="#ED6A5A")
        self.title_label.pack(pady=10)

        self.ingredients_label = tk.Label(self, text="Ingredients",
                                          font=("Comfortaa", 15, 'bold'),
                                          bg="#E6EBE0", fg="#5D576B")
        self.ingredients_label.pack(pady=5)

        self.ingredients_text = tk.Text(self, height=8, width=50, bg="#E6EBE0",
                                        font=("Comfortaa", 12), bd=0)
        self.ingredients_text.pack(pady=5)

        self.steps_label = tk.Label(self, text="Steps", font=("Comfortaa", 15, 'bold'),
                                    bg="#E6EBE0", fg="#5D576B")
        self.steps_label.pack(pady=5)

        self.instructions_text = tk.Text(self, height=10, width=50, bg="#E6EBE0",
                                         font=("Comfortaa", 12), bd=0)
        self.instructions_text.pack(pady=5)

        self.delicious_label = tk.Label(self, text="That sounds delicious, what are you waiting for?",
                                        font=("Comfortaa", 15, 'bold'), bg="#E6EBE0", fg="#ED6A5A")

    def fetch_recipes(self):
        """Fetches recipes from the Spoonacular API using the provided API key."""
        recipes = fetch_recipes(self.api_key)
        for recipe in recipes:
            title = recipe['title']
            ingredients_list = [ingredient['name'] for ingredient in recipe['extendedIngredients']]
            ingredients = ', '.join(ingredients_list)
            instructions = recipe['instructions']
            insert_recipe(title, ingredients, instructions)
        self.waiting_label = tk.Label(self, text="The recipes are waiting for you",
                                      font=("Comfortaa", 15, 'bold'), bg="#E6EBE0", fg="#ED6A5A")
        self.waiting_label.pack(pady=5)

    def show_random_recipe(self):
        """Displays a randomly selected recipe in the application window."""
        recipe = select_random_recipe()
        if recipe:
            self.title_label.config(text=recipe[1])
            self.ingredients_text.delete(1.0, tk.END)
            self.ingredients_text.insert(tk.END, recipe[2])
            self.instructions_text.delete(1.0, tk.END)
            self.instructions_text.insert(tk.END, recipe[3])
            if not hasattr(self, 'delicious_label_displayed'):
                self.delicious_label.pack(pady=5)
                self.delicious_label_displayed = True
