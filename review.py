from os import system
system('clear')
def review():
  
    food = input("Vilken maträtt beställde du?")
    drink = input("Vilken dryck beställde du?")
    while True:
        try:
            rating = int(input("På en skala på 1-5 hur mycket skulle du rekommendera den här drycken till maten?")) 
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except rating > 5:
          print("Oops!  That was no valid number.  Try again...")

    print(f"Du har ätit {food} och druckit {drink}, och du skulle ge denna kombinationen en rating på {rating} av 5.")


  