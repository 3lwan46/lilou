import csv

def banner():
    print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

██╗░░░░░██╗██╗░░░░░░█████╗░██╗░░░██╗
██║░░░░░██║██║░░░░░██╔══██╗██║░░░██║
██║░░░░░██║██║░░░░░██║░░██║██║░░░██║
██║░░░░░██║██║░░░░░██║░░██║██║░░░██║
███████╗██║███████╗╚█████╔╝╚██████╔╝
╚══════╝╚═╝╚══════╝░╚════╝░░╚═════╝░
""")


def menu():
    print("\nPlease select an option:\n")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion")
    print("5. Exit")


def start():
    banner()   # print once
    while True:
        menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            view_all()
        elif choice == "4":
            random_recipe()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again!\n")


# functions

def search_recipe():
    print(">>> Search Recipe function called")

def view_all():
    print(">>> View All Recipes function called")

def random_recipe():
    print(">>> Random Recipe function called")



def add_recipe(filename="recipes.csv"):
    print("\n--- Add a New Recipe ---")
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (separated by commas): ")
    prep_time = input("Enter preparation time (minutes): ")
    instructions = input("Enter cooking instructions: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

    # open file and append the recipe
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, ingredients, prep_time, instructions, difficulty])

    print(f"Recipe '{name}' has been added!\n")


# Run program
start()
