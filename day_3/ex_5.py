"""
Instructions

You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
    Take both people's names and check for the number of times the letters in the word TRUE occurs. 
    Then check for the number of times the letters in the word LOVE occurs. 
    Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
te1 = name1.count("e") 

l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
le1 = name1.count("e") 

t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
te2 = name2.count("e") 

l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
le2 = name2.count("e") 

score_t = t1+t2
score_r = r1+r2
score_u = u1+u2
score_te = te1+te2
score_true = score_t + score_r + score_u + score_te

score_l = l1+l2
score_o = o1+o2
score_v = v1+v2
score_le = le1+le2
score_love = score_l + score_o + score_v + score_le

score_total = int(str(score_true) + str(score_love))

if score_total < 10 or score_total > 90:
    print(f"Your score is {score_true}{score_love}, you go together like coke and mentos.")
elif score_total >= 40 and score_total <= 50:
    print(f"Your score is {score_true}{score_love}, you are alright together.")
else:
    print(f"Your score is {score_true}{score_love}.")
