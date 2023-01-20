import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="876briancleung",
  database = "cookbook"
)
cursor = mydb.cursor()

def salmon():
    cursor.execute("SELECT * FROM recipes WHERE ID= 6")
    records = cursor.fetchall()
    for x in records:
        print(x)

def pasta():
    cursor.execute("SELECT * FROM recipes WHERE ID= 1")
    records = cursor.fetchall()
    for x in records:
        print(x)

x = 1

while(x == 1):
    print("""I'm hungry and I need food. What should I cook? Press 1 for Teriyaki Salmon, 
    press 2 for Chicken Penne or press 3 for neither.""")

    food = input("> ")

    print("Here are the ingredients you need.")
    ####
    if food == "1":
        salmon()
        print("How would you like to cook it?")
        cook_method = input("> ")
        
        if cook_method == "1": # link code to recipe ID
            print("""Add salt and pepper and a teriyaki glaze on top if you want.
        Then bake in oven at 350 degrees for about 15 minutes depending on how well you want it cooked.""")
        elif cook_method == "2":
            print("""Add salt and pepper.
        Put a little oil and fry it skin side for 4 minutes then flip it over and fry for another minute.""")
        elif cook_method == "3":
            print("Season both sides with salt and pepper. Sear for 5 minutes on each side on high heat then bake in oven for 20 minutes at 375 degrees.")
        else:
            print("Well, there's always ramen.")

    elif food == "2":
        pasta()
        print("""How Would you like to cook it?.""")

        Pasta = input("> ")

        if Pasta == "1":
            print("""Boil a pot of water then put in your choice of pasta.
            Stir fry chicken, garlic, celery, salt, pepper.
            Add in the pasta and italian dressing.
            Reduce and then add parmesean cheese.
            Mix and enjoy.""")
            
        elif Pasta == "2":
            print("""Bring water to a boil, add salt.
            Put in pasta.
            Stir fry chicken, salt, pepper.
            Add parmesean sauce and mix.""")
        else:
            print("You're hangry.")

    else:
        print("You stubmle around and fall on a knife and die.  Good job!")

    print("""Return to the top?
    for yes, press 1
    for no, press 2""")
    doAgain = input("> ")
    if doAgain == "1":
        x = (1)
    else:
        x = (2)



