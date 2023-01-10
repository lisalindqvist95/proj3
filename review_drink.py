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


def review():
    def get_data_str():
        system('clear')
        while True:
            """
            Get user data from terminal. Loop until data is valid.
            """
            print("Enter your table number.")
            print("Rate your drinks today between 1-5.")
            print("Enter your input with a comma between the numbers.")

            data_str = input("Enter your rating here:\n")
            review_data = data_str.split(",")

            if validate_data(review_data):
                print("Thank you!")

                break

        return review_data

    def validate_data(values):
        """
        Checks if data is invalid (more than 2 numbers or not numbers).
        """
        try:
            [int(value) for value in values]
            if len(values) != 2:
                raise ValueError(
                    f"2 values are required, you provided {len(values)}"
                )

        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        """
        Prints error message if data is invalid.
        """
        return True

    def update_worksheet(data, worksheet):
        """
        Exports data to Google sheets.
        """

        print("Applying your rating...\n")
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(data)
        print("Thank you for your review!\n")

    def main():
        """
        Executes all functions in doc.
        """
        data = get_data_str()
        review_data = [int(num) for num in data]
        update_worksheet(review_data, "review")
    main()


"""
Code from Code Institute Love Sandwiches Project.
"""
