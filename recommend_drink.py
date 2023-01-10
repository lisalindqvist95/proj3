from os import system


def recommend():
    system('clear')
    meal = 0
    heading = "Recommended wines:\n"
    """
    Heading for all if/else statements below
    """

    white_wine_tup = ("Tolloy Pinot Grigio", "Pascal Jolivet Sancerren",
                      "Allan Scott Sauvignon Blanc", "William Fevre Chablis")

    red_wine_tup = ("Evolution Pinot Noir",
                    "Terrazas de Los Andes Malbec Reserva",
                    "Baron de Brane Bordeaux Blend",
                    "Newton Unfiltered Cabernet")
    """
    Tuples containg wine-selection.
    """

    print("Choose a meal from the menu:\n")
    print("1. HALIBUT EN PAPILLOTE\nBlack beluga lentils, pattypan squash,"
          "champagne beurre blanc, candied lemon.\n")
    print("2. SCALLOP RISOTTO\nSeasonal mushrooms, brown butter\n")
    print("3. GRASS FED RIBEYE STEAK (12OZ)\nGrilled vine tomato,"
          "parmesan-truffle fries, herb compound butter\n")
    print("4. STEAKHOUSE BURGER\nBrioche bun, bacon, fries\n")
    """
    Print out the menu that the user can choose from.
    """

    meal = int(input("Enter the number of your choice\n"))
    """
    Get user input.
    """

    while True:
        try:
            if meal == 1:
                system('clear')
                print(heading)
                slice_tup = white_wine_tup[0:2]
                for i in slice_tup:
                    print("*" + i + "\n")
                """
                If user chooses option 1 they will recieve a suggestion
                from the white wine tuple.
                """

            elif meal == 2:
                system('clear')
                print(heading)
                slice_tup = white_wine_tup[1:2:3]
                for i in slice_tup:
                    print("*" + i + "\n")
                """
                If user chooses option 2 they will recieve a suggestion
                from the white wine tuple.
                """

            elif meal == 3:
                system('clear')
                print(heading)
                slice_tup = red_wine_tup[1:3]
                for i in slice_tup:
                    print("*" + i + "\n")
                """
                If user chooses option 3 they will recieve a suggestion
                from the red wine tuple.
                """

            elif meal == 4:
                system('clear')
                print(heading)
                slice_tup = red_wine_tup[2:3]
                for i in slice_tup:
                    print("*" + i + "\n")
                """
                If user chooses option 4 they will recieve a suggestion
                from the red wine tuple.
                """

            else:
                if meal > 4 or meal < 1:
                    raise ValueError()
            """
            Check if user inputs invalid number.
            """

        except ValueError:
            print("Please choose a number between 1-4.")
        break


"""
Food menu from:
https://www.hilton.com/en/hotels/nyccnci-conrad-new-york-midtown/dining/dabble/?WT.mc_id=zlada0ww1CH2psh3ggl4ampanc5dkt6NYCCNCI7_153682779_1003528&gclid=Cj0KCQiAtvSdBhD0ARIsAPf8oNnS0MLheFT-zCeFlZ_lNykji4kJnOaVp12Rx0hTuugspU82tBjJS28aAiDOEALw_wcB&gclsrc=aw.ds&htmlMenu4ActiveTab=2
"""
