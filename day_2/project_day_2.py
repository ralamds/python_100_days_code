"""
This program calculates the amount each person should pay when splitting a bill with a tip included.

Usage:
1. Run the program
2. Enter the total bill amount.
3. Enter the tip percentage to give. The options are 10%, 12%, or 15%.
4. Enter the number of people splitting the bill.

The program then calculates the total bill with the tip included, and the individual amount each person should pay.

"""

# Print a welcome message to the user
print('Welcome to the tip calculator!')

# Get the total bill amount from the user
total_bill = float(input('What was the total bill?'))

# Get the tip percentage to give from the user
tip = float(input('How much tip would you like to give? 10, 12, or 15?'))

# Get the number of people splitting the bill from the user
n_ppl = int(input('How many people to split the bill?'))

# Calculate the tip percentage as a decimal
tip_percent = tip / 100

# Calculate the total bill with the tip included
bill_with_tip = total_bill * (1 + tip_percent)

# Calculate the individual amount each person should pay, rounded to 2 decimal points
indv_pay = round(bill_with_tip / n_ppl, 2) 

# Print the individual amount each person should pay
print(f'Each person should pay: {indv_pay}')


