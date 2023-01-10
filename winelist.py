from os import system

def winelist(): 
    system('clear')
    print("Mousserande Viner:")
    print()

    SparklingList = ["Rotari Cuvèe 28 piccolo (200 ml)\n", "Rotari Cuvèe 28\n"]

    for x in SparklingList:
        print(("* ") + x)

    print()
    print()

    print("Vita Viner:")
    print()

    WhiteList = [
    "Husets Vita 385:-, 95:-\n",
    "Santa Tresa Rina Ianca, Sicilien (Bio) 395:- 100:-\n","Soave ”Vinge della Corte”, Corte Adami, Venetien 435:-\n","Pinot Grigio Ciani, Trentino 450:-\n"]

    for x in WhiteList:
        print(("* ") + x)

    print()
    print()

    print("Röda Viner:")
    print()

    redList = [
    "Nivuro, Santa Tersea, Sicilien (Bio) 395:- , 100:-\n", "Corte Giara Corvina, Allegrini, Veneto, 400:-, 110:-\n", "Chianti Riserva, Collezione Oro, Piccini, Toscana 430:-\n",
"Barbera dÀsti, Cerutti, Piemonte 460:-\n", "Valpolicella Ripasso, Corte Adami , Veneto 485:-\n", "Pinot Nero, Endrizzi, Trentino, 495:-\n",
 "Testal Rosso del Veronese, Nicolis, Veneto 550:-\n", "Langhe Nebbiolo, La Spinetta, Piemonte 575:-\n", "Barolo, Broccardo, Piemonte 585:-\n", "Barbaresco, Giacone, Casina Alberta, Piemonte 595:-\n", "Podere 29, Gelso d´Oro, Puglia 595:-\n"]

    for x in redList:
        print(("* ") + x)

    print()
    print()

    print("Rosé Viner:")
    print()

    RoseList = ["Husets rosé 385:-, 95:- gl\n\n"]

    for x in RoseList:
        print(("* ") + x)