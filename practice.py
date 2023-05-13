
import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sample_lett = random.sample(range(len(letters)), nr_letters)
sample_numb = random.sample(range(len(numbers)), nr_numbers)
sample_symb = random.sample(range(len(symbols)), nr_symbols)


letters_pass =""
for i in sample_lett: 
    letters_pass += letters[i]

numbers_pass = ""
for j in sample_numb: 
    numbers_pass += numbers[j]

symbols_pass = ""
for k in sample_symb: 
    symbols_pass += symbols[k]

final_pass_simple = letters_pass + numbers_pass + symbols_pass

print(f"Your non-random password is {final_pass_simple}")

list_pass = list(final_pass_simple)
list_pass = random.sample(list_pass, len(list_pass))

rand_pass = ""
for l in list_pass:
    rand_pass += l

print(f"Your random password is {rand_pass}")
