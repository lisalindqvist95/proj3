from os import system
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('drink_review_data')

name = SHEET.worksheet('name')
data = name.get_all_values()

z = 1
while z == 1:
    """
    Loop for the system to run until user chooses to exit.
    """
    
    system('clear')
    """
    Clear terminal.
    """
    print(data)
    menuoptions = ["", "1. Winelist", "2. Review yor drink",
                   "3. Randomize drink", "4. Recommended wines", "5. Exit"]
    """
    List of menu options.
    """

    print("**********************")
    print("         MENU         ")
    print("**********************")
    print(menuoptions[1])
    print(menuoptions[2])
    print(menuoptions[3])
    print(menuoptions[4])
    print(menuoptions[5])
    """
    Print out the menu for the user.
    """

    try:
        print()
        print("Enter your choice: ")
        menu_select = int(input("\n"))
        """
        Collect user input, menu choice.
        """

        if menu_select == 1:
            from winelist import winelist
            winelist()
            """
            Call function from winelist.py if user chooses menu option one.
            """

        elif menu_select == 2:
            from review_drink import review
            review()
            """
            Call function from review_drink.py if user chooses menu option two.
            """

        elif menu_select == 3:
            from randomize_drink import randomize
            randomize()
            """
            Call function from randomize_drink.py if user chooses menu option three.
            """

        elif menu_select == 4:
            from recommend_drink import recommend
            recommend()
            """
            Call function from recommend_drink.py if user chooses menu option four.
            """

        elif menu_select == 5:
            print("Exiting program.")
            break
            """
            Exit program if user chooses menu option five.
            """
        else:
            print("Invalid choice. Please select a number between 1-5.")
            """
            Let user know the have to choose a number between 1-5
            in case they choose another number.
            """
    except ValueError:
        print("Invalid choice. Please select a number between 1-5.")
        """
        Let user know the have to choose a number between 1-5
        in case they press another key.
        """
    go_back = input("Press 'enter' to go back again.\n")
    """
    Let the user return to the main menu.
    """
