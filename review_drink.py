from os import system


def review():
    system('clear')

    food = input("Vilken maträtt beställde du?\n")
    drink = input("Vilken dryck beställde du?\n")
    while True:
        try:
            rating = int(input("På en skala på 1-5 hur mycket skulle du rekommendera den här drycken till maten?\n")) 
            if rating > 5 or rating < 1:
                raise ValueError()
            break
        except ValueError:
            print("That was not a valid choice, please choose a number between 1-5.")

    print(f"Du har ätit {food} och druckit {drink}, och du skulle ge denna kombinationen en rating på {rating} av 5.")