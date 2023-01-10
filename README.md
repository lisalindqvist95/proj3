# Interactive Drink Menu

Interactive Drink Menu is, just like the name implies, a drink menu for a restaurant which the user can interact with. When a lot more menus are digital and acciessible via QR-codes there is an opportunity to include more interactive features for the user. For example the possibility to get recommended drinks or rating their drinks which also can benefit the restaurant to improve their menu. A digital menu is also easier for the restaurant to update when an item runs out. 

Heres a link to the live [project]()

![Responsice Mockup](https://github.com/lucyrush/readme-template/blob/master/media/love_running_mockup.png)

## Features 

### Existing Features

- __Menu__

  - The menu lets the user select between the different features of the program. 
  - The user chooses which feature they want to access by inputting a number.
  - If the user inputs a number that is not part of the menu they will recieve an error message and get the chance to try again. 

![Menu](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __The Wine List__

  - This is the wine menu. 
  - It is compiled in lists that the restaurant staff can update by removing or adding items when needed.
  - The user returns to the main menu by hitting enter on their keyboard. 

![The Wine List](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)

- __Review Your Drink__

  - This feature lets the user rate their drink choice and their input is exported to a Google sheet for the restaurant to recieve the reviews. 
  - The user adds 
  - If the user enters invalid data the will recieve an error message to try again. 

![Review your drink](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)

- __Randomize Drink__

  - A fun feature for the user who can't choose their drink and want a surprise. 
  - The drink is chosen based on a computer randomized number. 

![Randomize Drink](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png)

- __Recommended Wines__ 

  - This feature allows the user to get a recommended wine based on their choice of food. 
  - One or more wines are recommended based on the food that the user inputs from the menu.
  - Invalid choises results in an error message. 

![Recommended Wines](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png)

- __Exit__

  - Breaks the loop and exits the program.

### Features Left to Implement

__Review__ 
- The review feature could be developed to be more specific and allow the user to rate more things, for example service.
- It would also be beneficial for the restaurant to know who left the review so that they can imporve their drinks. Although the users might want the possibility to be anonymous.

__Order__
- It would be useful if the user could use the app to order directly.
- If the menu is accessed via a QR-code this could potentially scan the table number so that the restaurant knows which table to serve. 

__Style__
- For this to be a desireble menu it would need some styling using HTML and CSS. 

## Data Model 

## Testing 

- The program has been manually tested by inserting invalid input, for example strings instead of numbers or numbers outside of menu choices. 

- Testinghas been done in loca terminal and the Heroku terminal. 

### Validator Testing 

- PEP8 Linter
  - No errors were found when passing through the PEP8 Linter, PEP8online.com

### Bugs

## Fixed Bugs

- Bugs with program closing before user chooses were fixed by including loops that the user will have to confitm to exit. 

- Bugs with program crashing by invalid input were fixed by incluting Try/Except statements. 

## Unfixed Bugs

- Since the user inserts the table-number and the review in the same input, there is a risk that the user will input the wrong table number or rating that is not between 1-5.This could be solved by using another type of form (for example via HTML) to get this information and separate the data collection. Or if you can get the Table/ordernumber via the QR-code you might not need to enter this manually, but this would requer more comlicated back-end coding.


## Deployment
The project was depoloyed via Heroku.
- Steps for deployment:
  - Save and push code to GitHub repository 
  - Create new Heroku app
  - Set the buildbacks to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on deploy

## Credits 

- 