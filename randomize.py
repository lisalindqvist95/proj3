import random
from os import system
def randomfu():
    system('clear')
    randomObjekt = random.randrange(10)
    print("Your drink is:")
    print()
    if (randomObjekt == 0):
        print("Mojito\n\n- mint leaves\n- white rum\n- lime juice\n- syrup\n")

    elif (randomObjekt == 1):
        print("Gimlet\n\n- vodka\n- syrup\n- lime juice\n")
            
    elif (randomObjekt == 2):
		    print("Margarita\n\n- silver tequila\n- Cointreau\n- lime juice\n")
    
    elif (randomObjekt == 3):
	      print("Cosmopolitan\n\n- citrus vodka\n- 1 oz Cointreau\n- lime juice\n- cranberry juice\n")
    
    elif(randomObjekt == 4):
		     print("Negroni\n\n- gin\n- Campari\n- sweet vermouth\n")
    
    elif (randomObjekt == 5):
	      print("Moscow Mule\n\n- vodka\n- ginger beer\n- lime juice\n")
     
    elif (randomObjekt == 6):
        print("Martini\n\n- gin\n- dry vermouth\n- olive\n")
      
    elif (randomObjekt == 7):
        print("Manhattan\n\n- rye whiskey\n- sweet vermouth\n- Angostura bitters\n");
   
    elif (randomObjekt == 8):
        print("Whiskey Sour\n\n- whiskey\n- lemon juice\n- sugar\n- egg white\n")
    
    elif (randomObjekt == 9):
        print("Spritz\n\n- Aperol\n- Cinzano Prosecco\n- Soda\n")

    else:
        print(randomObjekt)
       
        




   