
def add_recipe(filename="recipes.csv"):
    import csv

try:
    with open('recipes.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
except:
    with open('recipes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Recipe Name', 
            'Ingredients', 
            'Preparation Time (minutes)', 
            'Instructions', 
            'Difficulty'
        ])
        print('\n\nnew recipes.csv created')

print("\n=== Add a New Recipe ===")
j=0
while j<1 : 
    name = input(" enter your Recipe Name")
    j=j+1
    if isinstance(name, str) and name.isalpha():
        print("please enter your name as String ")
        j=0
    
Ingredients = input ( 'enter your gradients with comma')
i = 0
while i < 1:
    try:
        Preparation = int(input("Enter your Preparation Time (minutes): "))
        if Preparation <= 0:
            print("Please enter your Preparation Time with a positive number")
            i = 0
        else:
            i = 1
    except:
        print("Enter your Preparation Time as a number")
        i = 0

Instructions = input  ( " enter your Instructions ")
i=0
while i<1 :
    x= input ( " enter your Difficulty as number ( 1-Easy , 2-Medium , 3-Hard )")
    if(x==1):
        Difficulty = 'Easy'
        i=1
    elif(x==2) :
        Difficulty = 'Medium'
        i=1
    elif(x==3) :
        Difficulty = 'Hard'
        i=1
    else :
        print ('invalid number')
        i=0
new_recipes  = {'Recipe Name' : name ,
'Ingredients' : Ingredients ,
'Preparation Time (minutes)' : Preparation  ,
'Instructions' : Instructions ,
'Difficulty' : Difficulty }
with open('recipe.csv', 'a', newline='') as file:
    fn = [  'Recipe Name', 'Ingredients', 'Preparation Time (minutes)', 'Instructions', 'Difficulty' ]
    writer = csv.DictWriter(file, fieldnames=fn)
    writer.writerow(new_recipes)

    
