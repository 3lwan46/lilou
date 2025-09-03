import csv
import random

def banner():
    print("""


██╗░░░░░██╗██╗░░░░░░█████╗░██╗░░░██╗
██║░░░░░██║██║░░░░░██╔══██╗██║░░░██║
██║░░░░░██║██║░░░░░██║░░██║██║░░░██║
██║░░░░░██║██║░░░░░██║░░██║██║░░░██║
███████╗██║███████╗╚█████╔╝╚██████╔╝
╚══════╝╚═╝╚══════╝░╚════╝░░╚═════╝░

 🍳 Lilou's Cooking Corner 🍽️
""")


def menu():

    print("\nHi, Please select an option:\n")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion")
    print("5. generate a shopping list")
    print("6. Sorting Recipes by Rating")
    print("8. Exit")
    

with open("recipes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("CSV headers:", reader.fieldnames)



def start():
    banner()   # print once
    while True:
        menu()
        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            view_all()
        elif choice == "4":
            random_recipe()
        elif choice =="5":
            shopping_list()
        elif choice=="6":
            view_sorted_by_rating()
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again!\n")


# functions
#-----------------------------------------------------------------------------------------
def search_recipe(): #works but have issues, plz fix
    with open("recipes.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  
        ingredient = input("Enter ingredient: ").lower()
        
        for row in reader:
            ingredients = row[1].lower().split(",")
            if ingredient in [i.strip() for i in ingredients]:
                print(row[0], "-", row[1], "ingredients")


#-----------------------------------------------------------------------------------------
def view_all(): 
    print(">>> View All Recipes function called")# write the function here
import csv


def recipes_table():
    with open("recipes.csv","r") as file:
        reader = csv.reader(file)
        head = next(reader)
       
  
        print(f"{head[0]:20} {head[1]:40}{head[2]:15}")
        print(".."*50)
        for row in reader:
            print(f"{row[0]:20}{row[1]:40}{row[2]:20}")
       
recipes_table()

#-----------------------------------------------------------------------------------------
def random_recipe(filename="recipes.csv"):# make sure its run
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            recipes = list(reader)  # convert to list so we can use random.choice

            if not recipes:
                print("No recipes found in your collection.")
                return

            recipe = random.choice(recipes)  # pick random recipe
            print("\n--- Random Recipe Suggestion ---")
            print(f"Recipe Name: {recipe['Recipe Name']}")
            print(f"Ingredients: {recipe['Ingredients']}")
            print(f"Preparation Time: {recipe['Preparation Time (minutes)']} minutes")
            print(f"Cooking Instructions: {recipe['Cooking Instructions']}")
            print(f"Difficulty Level: {recipe['Difficulty Level']}")
            print(f"Category: {recipe['Categorize']}")
            print(f"Customer Rate: {recipe['Customer Rate']}")
            print("-------------------------------\n")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



#-----------------------------------------------------------------------------------------
def shopping_list(filename="recipes.csv"):# all good
    print("\nWelcome to shopping list!")
    recipe_name = input("Which recipe would you like to buy? Enter the name: ")

    found = False
    with open(filename, "r", encoding="utf-8-sig") as f:  # utf-8-sig handles BOM from Excel
        reader = csv.DictReader(f)

        # normalize fieldnames (lowercase, strip spaces)
        field_map = {name.strip().lower(): name for name in reader.fieldnames}

        for row in reader:
            recipe_field = field_map.get("recipe name")
            ingredients_field = field_map.get("ingredients")

            if recipe_field and ingredients_field:
                if row[recipe_field].strip().lower() == recipe_name.strip().lower():
                    print(f"\nIngredients for {row[recipe_field]}:\n{row[ingredients_field]}")
                    found = True
                    break

    if not found:
        print(f"\nSorry, recipe '{recipe_name}' not found in your collection.")



#-----------------------------------------------------------------------------------------
###-- add function ... 


#-----------------------------------------------------------------------------------------
def view_sorted_by_rating(filename="recipes.csv"):# works good
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            recipes = list(reader)

        if not recipes:
            print("No recipes available.")
            return

        # sort by rating (already numbers in CSV, but safer to cast to float)
        recipes.sort(key=lambda r: float(r["Customer Rate"]), reverse=True)

        print("\n[ Recipes Sorted by Rating ]")
        for r in recipes:
            print(r["Recipe Name"], "-", r["Customer Rate"] ,"⭐")
        print("------------------------------")

    except FileNotFoundError:
        print("recipes.csv not found.")

# Run program
start()
