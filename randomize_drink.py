import random
from os import system


def randomize():
    """
    Function to randomize drink. Inside function a nr between 0-9 will be
    randomizeand and an if/else statement prints a drink based on the nr.
    """
    system('clear')
    random_object = random.randrange(10)
    print("We have selected a drink for you!\nYour drink is:")
    print()
    if random_object == 0:
        print("Mojito\n\n- rum\n- mint \n- lime \n- sugar\n- club soda\n")

    elif random_object == 1:
        print("Gimlet\n\n- gin\n- lime juice\n")

    elif random_object == 2:
        print("Margarita\n\n- tequila\n- triple sec\n- lime juice\n")

    elif random_object == 3:
        print("Cosmo\n\n- vodka\n- cointreau\n- lime\n- cranberry juice\n")

    elif random_object == 4:
        print("Negroni\n\n- gin\n- campari\n- sweet vermouth\n")

    elif random_object == 5:
        print("Moscow Mule\n\n- vodka\n- ginger beer\n- lime juice\n")

    elif random_object == 6:
        print("Martini\n\n- gin\n- dry vermouth\n- olive\n")

    elif random_object == 7:
        print("Manhattan\n\n- rye whiskey\n- vermouth\n- angostura bitters\n")

    elif random_object == 8:
        print("Whiskey Sour\n\n- whiskey\n- lemon juice\n- sugar\n")

    else:
        print("Spritz\n\n- Aperol\n- Prosecco\n- Soda\n")
