from os import system


def recommend():
    system('clear')
    meal = 0
    heading = "Recommended wines:\n"
    white_wine_tup = ("Tolloy Pinot Grigio", "Pascal Jolivet Sancerren",
                      "Allan Scott Sauvignon Blanc", "William Fevre Chablis")

    red_wine_tup = ("Evolution Pinot Noir",
                    "Terrazas de Los Andes Malbec Reserva",
                    "Baron de Brane Bordeaux Blend",
                    "Newton Unfiltered Cabernet")

    print("Choose a meal from the menu:\n")
    print("1. HALIBUT EN PAPILLOTE\nBlack beluga lentils, pattypan squash,"
          "champagne beurre blanc, candied lemon.\n")
    print("2. SCALLOP RISOTTO\nSeasonal mushrooms, brown butter\n")
    print("3. GRASS FED RIBEYE STEAK (12OZ)\nGrilled vine tomato,"
          "parmesan-truffle fries, herb compound butter\n")
    print("4. STEAKHOUSE BURGER\nBrioche bun, bacon, fries\n")
    meal = int(input("Enter the number of your choice\n"))
    while True:
        try:
            if meal == 1:
                system('clear')
                print(heading)
                slice_tup = white_wine_tup[0:2]
                for i in slice_tup:
                    print("*" + i + "\n")

            elif meal == 2:
                system('clear')
                print(heading)
                slice_tup = white_wine_tup[1:2:3]
                for i in slice_tup:
                    print("*" + i + "\n")

            elif meal == 3:
                system('clear')
                print(heading)
                slice_tup = red_wine_tup[1:3]
                for i in slice_tup:
                    print("*" + i + "\n")

            elif meal == 4:
                system('clear')
                print(heading)
                slice_tup = red_wine_tup[2:3]
                for i in slice_tup:
                    print("*" + i + "\n")

            else:
                if meal > 4 or meal < 1:
                    raise ValueError()

        except ValueError:
            print("Please choose a number between 1-4.")
        break
