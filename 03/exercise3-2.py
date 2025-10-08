"""
Pizza Delivery Program
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# todo: work out how much they need to pay based on their size choice
if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
elif size == "L":
    pizza_price = 25
else:
    print("Wrong option, please try again.")

# todo: work out how much to add to their bill based on their pepperoni choice
"""
if size == "S" and pepperoni == "Y":
    pizza_price += 2
elif size == "M" and pepperoni == "Y":
    pizza_price += 3
elif size == "L" and pepperoni == "Y":
    pizza_price += 3
"""

if pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3


# todo: work out their final amount based on whether if they want extra cheese
if extra_cheese == "Y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")