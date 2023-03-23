Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #This program calculates and displays travel expenses
>>> #22 MAR 23
>>> #CTI-110 P1HW2 - Travel Expense
>>> #Tracey Alston
>>> #
>>> 
>>> #Enter Budget: 1200
>>> #Enter your travel destination: Nashville
>>> #How much do you think you will spend on gas: 250
>>> #Approximately, how much will you need for accommodation/hotel? 600
>>> #Last, how much do you need for food? 300
>>> 
>>> #---------------------------Travel Expenses-----------------------------
>>> #Location: Nashville
>>> #Initial: Budget
>>> 
>>> Fuel = 250
>>> Accommodation = 600
>>> Food = 300
>>> 
>>> Expenses = Fuel + Accommodation + Food
>>> 
>>> print('Expenses are:', Expenses)
Expenses are: 1150
>>> 
>>> Budget = 1200
>>> Expenses = 1150
>>> Results = Budget -
SyntaxError: incomplete input
>>> Results = Budget - Expenses
>>> 
>>> print('Results are:', Results)
Results are: 50
