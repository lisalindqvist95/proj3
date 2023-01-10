from os import system
z = 1
while z == 1:
    system('clear')

    menuoptions = ["", "1. Winelist", "2. Review yor drink", "3. Randomize drink", "4. Recommended wines", "5. Exit"]

    print("**********************")
    print("         MENU         ")
    print("**********************")
    print(menuoptions[1])
    print(menuoptions[2])
    print(menuoptions[3])
    print(menuoptions[4])
    print(menuoptions[5])
    
    try:
        print()
        print("Enter your choice: ")
        menuSelect = int(input())
    
        if menuSelect == 1:
            from winelist import winelist 
            winelist()
    

        elif menuSelect == 2:
            from reviw import review
            review()
  
        elif menuSelect == 3:
            from randomize import randomfu
            randomfu()
    
        elif menuSelect == 4:
            from recommend import recommend
            recommend()

        elif menuSelect == 5:
            print("Exiting program")
            break

        else:
            print("Invalid choice. Please select a number between 1-5 from the menu.")
    except ValueError:
        print("Invalid choice. Please select a number between 1-5 from the menu.")
    ok = input("Press 'enter' to go back again.")