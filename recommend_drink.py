from os import system

def recommend():
    system('clear')
    x = 0
    try:
        whitewineArray = ["Husets Vita 385:-, 95:-\n\n", "Santa Tresa Rina Ianca, Sicilien (Bio) 395:-, 100:-\n\n"]

        redwineArray = ["Nivuro, Santa Tersea, Sicilien (Bio) 395:- , 100:-\n\n", "Corte Giara Corvina, Allegrini, Veneto, 400:-, 110:-\n\n"]
            
        print("Skriv in siffran på din maträtt från menyn: ")
        print("____________________")
        print("1. Linguini Vongole\nLinguini m vongole, vitlök, vittvin, peperoncini, tomat, olivolja, persilja.\n")
        print("2. Linguini al Tonno\nLinguini m färsk tonfisk, vitlök, persilja, peperoncini, cocktail tomat, oliver,lök, kapris,olivolja.\n")
        print("3. Linguini Carbonara\nLinguini m pancetta, vittvin, grädde, lök, svart peppar, äggula.\n")
        print("4. Penne Stravaganti\nPastarör m oxfilé, champinjoner, grädde, skysås, vitlök, peperoncini.\n")
      
        x = int(input("Skriv in ditt val\n"))
        if (x == 1):
            system('clear')
            print("Rekommenderade viner:\n")
            for i in whitewineArray:
                print(i)
              
        elif (x == 2):
            system('clear')
            print("Rekommenderade viner:\n") 
            whitewineArray[0] = "Soave ”Vinge della Corte”, Corte Adami, Venetien 435:-\n\n";
            for i in whitewineArray:
                print(i)
                
        elif (x == 3):
            system('clear')
            print("Rekommenderade viner:\n")

            for i in redwineArray:
                print(i)
          
        elif (x == 4):
            system('clear')
            print("Rekommenderade viner:\n")

            redwineArray[0] = "Testal Rosso del Veronese, Nicolis, Veneto 550:-\n\n";
            for i in redwineArray:
                print(i)
        
        else:
            system('clear')
            print("Du gjorde inget giltigt val!\nGå tillbaka till menyn och gör ett nytt val")
  
    except:
            print("Oops!  That was no valid number.  Try again...")