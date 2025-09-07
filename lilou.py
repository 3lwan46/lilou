import csv
import random
import re

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

    print("\nWelcome to LILOU, Please select an option:\n")
    print("1. 🍕🍔🌭🍳 Add a new recipe to the collection")
    print("2. 🔍Search for recipes by ingredient")
    print("3. 👀View all recipes")
    print("4. 📄View a random recipe suggestion")
    print("5. Generate a shopping list🛒")
    print("6. Sorting Recipes by Rating 📶")
    print("7. Edit ingredients⚙️")
    print("8. ⏲️Cooking time ;)")
    print("9. ✨Suggest")
    print("10. Exit")
    

with open("recipes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) #reader that reads each row as a dictionary instead of a list.
    print("CSV headers:", reader.fieldnames)



def start():
    banner()
    while True:
        menu()
        choice = input("\nEnter your choice (1-10): ")


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
        elif choice=="7":
            edit_ingredients()
        elif choice=="8":
         while True:
             result = cooking()
             if result == "again":
                    continue
             elif result == "menu":
                    break 
             elif result == "exit":
                    print ("Goodbye!")
                    return
             else:
                    break 
        elif choice == "9":
            suggest_recipes()
            
        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again!\n")


# functions:
#-----------------------------------------------------------------------------------------
def search_recipe(filename="recipes.csv"):
    ingredient = input("Enter ingredient to search: ").strip().lower()

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        found = False
        for row in reader:
            if row["Recipe Name"] == "Recipe Name":
                continue  

            if ingredient in row["Ingredients"].lower():
                print("-----------------------------------------------------------------------------------------")
                print(f"🍽️  Recipe: {row['Recipe Name']}")
                print(f"🥗  Ingredients: {row['Ingredients']}")
                found = True

        if not found:
            print(f"\n❌ No recipes found containing '{ingredient}'.")

#-----------------------------------------------------------------------------------------
def view_all(): # to print name and time only
    with open("recipes.csv","r") as file:
        reader = csv.reader(file)
        head = next(reader)
        print(f"{head[0]:40} {head[2]:15}")
        print(".."*50)
        for row in reader:
            print(f"{row[0]:40}{row[2]:20}")

#-----------------------------------------------------------------------------------------

def random_recipe(filename="recipes.csv"):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            recipes = []

            for row in reader:
                if row["Recipe Name"] == "Recipe Name":
                    continue
                recipes.append(row)

            if not recipes:
                print("No recipes found in your collection.")
                return

            recipe = random.choice(recipes)
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
def shopping_list(filename="recipes.csv"):
    print("\nWelcome to the shopping list!")
    print("Type the recipe name you want to buy, or type 'end' to finish.\n")

    total_ingredients = {}  # store ingredient totals hereee

    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        recipes = list(reader)

    while True:
        recipe_name = input("Enter recipe name (or 'end' to finish): ").strip()
        if recipe_name.lower() == "end":
            break

        recipe = None
        for r in recipes:
            if r['Recipe Name'].strip().lower() == recipe_name.lower():
                recipe = r
                break

        if not recipe:
            print(f"❌ Recipe '{recipe_name}' not found.")
            continue

        print(f"\n✅ Added ingredients from {recipe['Recipe Name']}")

        for part in recipe['Ingredients'].split(";"):
            if "=" in part:
                name, amount = part.split("=", 1)
                name = name.strip()
                amount = amount.strip()

                # separate number and unit
                num = ""
                unit = ""
                for ch in amount:
                    if ch.isdigit() or ch == ".":
                        num += ch
                    else:
                        unit += ch
                unit = unit.strip()
                num = float(num) if num else 1

                key = f"{name} ({unit})" if unit else name

                if key in total_ingredients:
                    total_ingredients[key] += num
                else:
                    total_ingredients[key] = num

    # Print final shopping list
    print("\n🛒 Final Shopping List:")
    if total_ingredients:
        for ing, amount in total_ingredients.items():
            print(f"- {ing}: {amount}")
    else:
        print("No ingredients selected.")



#-----------------------------------------------------------------------------------------
###-- add function ... 


def add_recipe():
    # Define the correct headers
    headers = ['Recipe Name','Ingredients','Preparation Time (minutes)',
               'Cooking Instructions','Difficulty Level','Categorize','Customer Rate']

    # Create file if it doesn't exist
    try:
        with open('recipes.csv', 'r', newline='', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        with open('recipes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            print('New recipes.csv created.')

    print("\n=== Add a New Recipe ===")

    # Recipe Name
    while True:
        name = input("Enter the recipe name: ").strip()
        if name:
            break
        print("Please enter a valid name.")

    # Ingredients
    ingredients_list = []
    while True:
        ing = input("Enter an ingredient (or type 'Exit' to finish): ").strip()
        if ing.lower() == 'exit':
            break
        if ing:
            ingredients_list.append(ing)
    Ingredients = "; ".join(ingredients_list)

    # Preparation Time
    while True:
        try:
            prep_time = int(input("Enter Preparation Time (minutes): "))
            if prep_time > 0:
                break
        except ValueError:
            pass

    # Cooking Instructions
    Instructions = input("Enter Cooking Instructions: ").strip()

    # Difficulty Level
    while True:
        try:
            diff = int(input("Enter Difficulty (1-Easy, 2-Medium, 3-Hard): "))
            if diff == 1:
                Difficulty = 'Easy'
            elif diff == 2:
                Difficulty = 'Medium'
            elif diff == 3:
                Difficulty = 'Hard'
            else:
                continue
            break
        except ValueError:
            continue

    # Category
    Categorize = input("Enter Category (Breakfast/Lunch/Dinner/Snack/Dessert): ").strip()

    # Customer Rate
    while True:
        try:
            Customer_Rate = float(input("Enter Customer Rate (0.0 to 5.0): "))
            if 0 <= Customer_Rate <= 5:
                break
        except ValueError:
            continue

    # Prepare the dictionary
    new_recipe = {
        'Recipe Name': name,
        'Ingredients': Ingredients,
        'Preparation Time (minutes)': prep_time,
        'Cooking Instructions': Instructions,
        'Difficulty Level': Difficulty,
        'Categorize': Categorize,
        'Customer Rate': Customer_Rate
    }

    # Append to CSV
    with open('recipes.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(new_recipe)

    print(f"\n✅ Recipe '{name}' added successfully!")

#-----------------------------------------------------------------------------------------
#to edit ingredient quantities based on desired number of servings 
def edit_ingredients(filename="recipes.csv"):

    with open(filename, mode='r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        recipes = list(reader)

    if not recipes:
        print("No recipes found.")
        return

    # recipe name from the user
    recipe_name = input("Enter the recipe name: ").strip().lower()

    recipe = None
    for r in recipes:
        if r['Recipe Name'].strip().lower() == recipe_name:
            recipe = r
            break

    if not recipe:
        print("Recipe not found!")
        return

    # display ingredients
    ingredients = recipe['Ingredients'].split(';')
    print("\nCurrent ingredients:")
    for ing in ingredients:
        print(ing.strip())


    ingredient_to_edit = input("\nEnter the ingredient to edit: ").strip().lower()


    found_index = -1 #-1 cmeans “nothing found yet”
    for i, ing in enumerate(ingredients):
        name = ing.split('=')[0].strip().lower()
        if ingredient_to_edit == name:
            found_index = i
            break

    if found_index == -1:
        print("Ingredient not found!")
        return

    updated_qty = input("Enter the updated quantity (with unit): ").strip()

    # update the ingredient in filw
    ingredient_name = ingredients[found_index].split('=')[0].strip()
    ingredients[found_index] = f"{ingredient_name}={updated_qty}"

    # update the recipe inngredients
    recipe['Ingredients'] = '; '.join(ingredients)

    with open(filename, mode='w', newline='', encoding="utf-8-sig") as file:
        fieldnames = recipes[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recipes)

    print("\nIngredient updated successfully!\n")

#-----------------------------------------------------------------------------------------
def view_sorted_by_rating(filename="recipes.csv"):
    try:
        with open(filename, "r", encoding="utf-8-sig") as f:  # utf-8-sig removes hidden BOM chars
            reader = csv.DictReader(f)

            # normalize headers (remove spaces, lowercase)
            field_map = {name.strip().lower(): name for name in reader.fieldnames}
            name_field = field_map.get("recipe name")
            rate_field = field_map.get("customer rate")

            recipes = list(reader)

        if not recipes:
            print("No recipes available.")
            return

        # sort by rating, default to 0 if missing
        recipes.sort(key=lambda r: float(r.get(rate_field, 0) or 0), reverse=True)

        print("\n[ Recipes Sorted by Rating ]")
        for recipe in recipes:
            print(f"{recipe[name_field]} - {recipe[rate_field]} ⭐")
        print("------------------------------")

    except FileNotFoundError:
        print("recipes.csv not found.")



#-----------------------------------------------------------------------------------------
def cooking(filename="recipes.csv"):

    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        recipes = list(reader)

    if not recipes:
        print("No recipes found.")
        return

    # Show recipe names
    print("\nAvailable Recipes:")
    for i, r in enumerate(recipes, start=1): #enumerate used to adds a counter (index) 1.2.3....
        print(f"{i}. {r['Recipe Name']}")

    # make user select recipe
    choice = input("\nEnter the recipe name you want to cook: ").strip() # to remove whitespace...
    selected = None
    for r in recipes:
        if r["Recipe Name"].strip().lower() == choice.lower():
            selected = r
            break

    if not selected:
        print("Recipe not found.")
        return

    # select the amount
    try:
        amount = int(input("Enter the number of servings/pieces you want to cook: "))
        if amount < 1:
            print("Amount must be at least 1.")
            return
    except ValueError:
        print("Invalid number.")
        return

    # Parse ingredients
    ingredients_dict = {}
    for part in selected["Ingredients"].split(";"):
        if "=" in part:
            name, qty = part.split("=")
            ingredients_dict[name.strip()] = qty.strip()

    # Scale ingredients
    scaled = {}
    for item, qty in ingredients_dict.items():
        # extract first number (assumes user wrote numeric qty at start)
        match = re.match(r"(\d+\.?\d*)(.*)", qty) #عشان يطلع الارقام من قسم المكونات ويحسبهم حسبب الكمية الي اليوزر يحددها
        if match:
            number = float(match.group(1)) * amount
            unit = match.group(2)
            scaled[item] = f"{number:.2f}{unit}"
        else:
            scaled[item] = qty  # leave as-is if no number found

    # Display scaled ingredients
    print(f"\nIngredients for {amount} servings of {selected['Recipe Name']}:")
    for item, qty in scaled.items():
        print(f"{item}: {qty}")

#-----------------------------------
    #Save user logs 
    def add_user_choice_to_file(line, logs):
        with open(logs, "a") as f:
          f.write(f"{line}\n")
          print(f"Successfully appended to {logs}")
        
    log_line = (
        f"Cooked: {selected['Recipe Name']} | "
        f"servings={amount} | "
        f"items={len(scaled)} | "
        f"category={selected['Categorize']}"
        )
    add_user_choice_to_file(log_line, "logs.csv")
    

    #Ask the user again 
    ask= input("Do you want to cook another recipe? (yes/no):").strip().lower()
    if ask == "yes":
        return "again"

    next_input = input("Do you want to exit or return to menu? (exit/menu): ").strip().lower()
    return next_input
#---------------------------------------------------------------------------------------------------
    #Suggest Recipes

def suggest_recipes():
    import csv, random

    count_breakfast = 0 
    count_dinner = 0 
    count_lunch = 0

    # --- Step 1: Read last 7 log entries ---
    try:
        with open("logs.csv", "r") as f:
            lines = f.readlines()
            logs_length = len(lines)
            if logs_length == 0:
                print("📂 No cooking history found in logs yet.")
                return

            start_index = max(0, logs_length - 7)
            while start_index < logs_length:
                line = lines[start_index].strip()
                if "category=Breakfast" in line:
                    count_breakfast += 1
                elif "category=Lunch" in line:
                    count_lunch += 1
                elif "category=Dinner" in line:
                    count_dinner += 1
                start_index += 1
    except FileNotFoundError:
        print('❌ logs.csv not found.')
        return
    except Exception as e:
        print(f'⚠️ Error while reading logs.csv: {e}')
        return

    # --- Step 2: Read recipes by category ---
    breakfast_recipes = []
    lunch_recipes = []
    dinner_recipes = []

    try:
        with open("recipes.csv", "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            # Normalize headers
            field_map = {name.strip().lower(): name for name in reader.fieldnames}
            name_field = field_map.get("recipe name")
            category_field = field_map.get("categorize")

            if not name_field or not category_field:
                print("❌ CSV is missing 'Recipe Name' or 'Categorize' column.")
                return

            for row in reader:
                category = row[category_field].strip().lower()
                if "breakfast" in category:
                    breakfast_recipes.append(row[name_field])
                if "lunch" in category:
                    lunch_recipes.append(row[name_field])
                if "dinner" in category:
                    dinner_recipes.append(row[name_field])

    except FileNotFoundError:
        print("❌ recipes.csv not found.")
        return
    except Exception as e:
        print(f"⚠️ Error while reading recipes.csv: {e}")
        return

    # --- Step 3: Suggest recipe based on least cooked category ---
    if count_breakfast == count_lunch == count_dinner == 0:
        print("📂 No categories found in recent logs.")
        return

    least_cooked = min(count_breakfast, count_lunch, count_dinner)
    least_categories = []
    if count_breakfast == least_cooked:
        least_categories.append(("Breakfast", breakfast_recipes))
    if count_lunch == least_cooked:
        least_categories.append(("Lunch", lunch_recipes))
    if count_dinner == least_cooked:
        least_categories.append(("Dinner", dinner_recipes))

    if least_categories:
        category, recipes = random.choice(least_categories)
        if recipes:
            suggest = random.choice(recipes)
            print(f"👉 You cooked the least {category} recipes recently.")
            print(f"✨ Suggestion: {suggest}")
        else:
            print(f"⚠️ No recipes available for {category}.")
    else:
        print("Keep cooking more and I'll suggest new recipes.")

# Run program
start()
