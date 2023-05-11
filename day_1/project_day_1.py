"""
This program generates a band name by combining the user's hometown and pet name.

Usage:
1. Run the program
2. Enter the city where you grew up
3. Enter the name of a pet

The program then combines the city and pet names to generate a band name.

"""

# Print a greeting message to the user
print("Hello! Welcome to 'Band Name Generator' program!")

# Get the name of the city where the user grew up
city = input("Where did you grow up?\n")

# Get the name of the user's pet
pet = input("What is your pet's name?\n")

# Combine the city and pet names to generate a band name, and print it to the user
print(f"Your band name could be {city} {pet}.")

