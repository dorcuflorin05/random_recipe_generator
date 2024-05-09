"""Management in the Random Recipe Generator."""
import sqlite3
import os

DB_FILE = 'data/recipes.db'

def create_database():
    """Creates a SQLite database for storing recipe data."""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS recipes 
                     (id INTEGER PRIMARY KEY, title TEXT, ingredients TEXT, instructions TEXT)''')
        conn.commit()
        conn.close()

def insert_recipe(title, ingredients, instructions):
    """Inserts a recipe into the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
              (title, ingredients, instructions))
    conn.commit()
    conn.close()

def select_random_recipe():
    """Selects a random recipe from the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM recipes ORDER BY RANDOM() LIMIT 1")
    recipe = c.fetchone()
    conn.close()
    return recipe
