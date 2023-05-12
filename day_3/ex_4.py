"""
Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""
small_pizza = 15 
medium_pizza = 20 
large_pizza = 25 

pep_sp = 2
pep_mlp = 3

extra_cz = 1

size =input("What size do you want: S, M or L \n").upper()
pep = input("Do you want pepperoni?\n").upper()
ext_cz = input("Do you want extra cheese?\n").upper()

price = 0

if ext_cz == "Y": 
    price += extra_cz
    if size == "S":
        price += small_pizza
        if pep == "Y":
            price += pep_sp
    elif size == "M":
        price += medium_pizza
        if pep == "Y":
            price += pep_mlp
    elif size == "L":
        price += large_pizza
        if pep == "Y":
            price += pep_mlp
    else:
        print("Enter valid size")
else:
    if size == "S":
        price += small_pizza
        if pep == "Y":
            price += pep_sp
    elif size == "M":
        price += medium_pizza
        if pep == "Y":
            price += pep_mlp
    elif size == "L":
        price += large_pizza
        if pep == "Y":
            price += pep_mlp
    else:
        print("Enter valid size")

print(f"Your final bill is: ${price}.")