from os import system


def winelist():
    """
    Function prints out menu.
    """

    system('clear')
    print("Sparkling wines by the glass:\n")

    sparkling_list = ["Moet & Chandon Dom Pérignon",
                      "Perrier-Jouët Grand Brut"]

    for wine in sparkling_list:
        print(("* ") + wine + "\n\n")

    print("White wine:\n")

    white_list = ["Tolloy Pinot Grigio", "Pascal Jolivet Sancerren",
                  "Allan Scott Sauvignon Blanc", "William Fevre Chablis"]

    for wine in white_list:
        print(("* ") + wine + "\n\n")

    print("Red wine:\n")

    red_list = ["Evolution Pinot Noir", "Terrazas de Los Andes Malbec Reserva",
                "Baron de Brane Bordeaux Blend", "Newton Unfiltered Cabernet"]

    red_list.pop(0)
    red_list.append("La Crema Pinot Noir")

    for wine in red_list:
        print(("* ") + wine + "\n\n")

    print("Rosé wine:\n")

    rose_list = ["Domaine Sainte Marie Vie Vité",
                 "Chateau d'Esclans Whispering Angel"]

    for wine in rose_list:
        print(("* ") + wine + "\n\n")

    """
    Wine-list from
    https://www.theplazany.com/wp-content/uploads/2022/06/Champagne-Bar-Cocktail-Menu-June-2022.pdf
    """
