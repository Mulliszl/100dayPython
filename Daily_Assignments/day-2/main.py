### Day 2 Project: Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the bill split calculator.\n")
bill = float(input("What is the total bill? \n$"))
tip = int(input("What is percent is the the tip? \n"))
split = input("How many people are splitting the bill? \n")
tip_int = tip /100 + 1
total = round(float(bill) * tip_int /int(split), 2)
total = "{:.2f}".format(total)

print(f" Your bill of {bill}, with a tip of {tip}% split between {split} people totals to: \n ${total} per person.")