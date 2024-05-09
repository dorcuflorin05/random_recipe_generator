"""Recipe Generator Application"""
from tkinter import messagebox
import yaml
from src.gui import RecipeGeneratorApp
from src.database import create_database

def load_config(filename="config.yaml"):
    """Load configuration settings from a YAML file."""
    with open(filename, "r") as f:
        config = yaml.safe_load(f)
    return config

def main():
    """The main function to initialize and run the Recipe Generator app."""
    create_database()
    config = load_config()
    api_key = config.get("api_key")
    if api_key is None:
        print("API key not found in config.yaml.")
        return

    try:
        app = RecipeGeneratorApp(api_key)
        app.mainloop()
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Config file not found.")
    except yaml.YAMLError:
        messagebox.showerror("YAML Error", "Error while parsing the YAML file.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
