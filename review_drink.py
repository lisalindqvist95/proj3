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
        while True:
            print("Rate your drinks today between 1-5.")

            data_str = int(input("Enter your rating here:\n"))

            if validate_data(data_str):
                print("Data is valid!")
                break

        return data_str

    def validate_data(values):
        try:
            [int(value) for value in values]
            if len(values) != 1:
                raise ValueError(
                    f"1 value between 1-5 is required, you provided {len(values)}"
                )
                
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
       
        return True
  

    def update_worksheet(data, worksheet):

        print(f"Updating {worksheet} worksheet...\n")
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(data)
        print(f"{worksheet} worksheet updated successfully\n")

    def main():
        data = get_data_str()
        data_str = [int(num) for num in data]
        update_worksheet(data_str, "review")
    main()
