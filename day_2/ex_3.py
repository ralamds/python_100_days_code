# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)

days = (90 - age) * 365 
weeks = (90 - age) * 52
months = (90 - age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
