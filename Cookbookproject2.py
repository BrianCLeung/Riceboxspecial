x = 1

while(x == 1):
    print("""You enter a kitchen and see salmon, chicken, and pasta.
    Which do you choose for dinner? #1 salmon or #2 chicken pasta.""")

    food = input("> ")

    if food == "1":
        print("How should I cook it?")
        print("1. I can bake it.")
        print("2. Fry it on a pan.")
        print("3. or both.")

        cook_method = input("> ")

        if cook_method == "1": 
            print("""Add salt and pepper and a teriyaki glaze on top if you want.
        Then bake in oven at 350 degrees for about 15 minutes depending on how well you want it cooked.""")
        elif cook_method == "2":
            print("""Add salt and pepper.
        Put a little oil and fry it skin side for 4 minutes then flip it over and fry for another minute.""")
        elif cook_method == "3":
            print("Season both sides with salt and pepper. Sear for 5 minutes on each side on high heat then bake in oven for 20 minutes at 375 degrees.")
        else:
            print("Well, there's always ramen.")
            print("Or I go hungry.")

    elif food == "2":
        print("""You don't have enough ingredients, consider purchasing a bottle of sauce.
        We only have:
        . Salt and pepper.
        2. Parmesean cheese.
        3. Butter.
        4. and you only have chicken.
        How should you go about this?
        Option 1 would be to just go buy the sauce
        Option 2 would be to go to the store and buy ingredients to MAKE it
        Option 3 is...I don't know yet, let's see what you do first.""")


        Pasta = input("> ")

        if Pasta == "1":
            print("well there you go, to the store and back within the half hour, now you don't have to wait too long to eat.")
            print("Good job!")
        elif Pasta == "2":
            print("Do you seriously want to take all this time to make sauce you've never made, when your're THIS hangry?? ")
            print("BE SMART!")
        else:
            print("You're Hangry")

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