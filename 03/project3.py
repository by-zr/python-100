# Treasure Island
print('''
**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

input1 = input("Type 'left' or 'right' ").lower()

if input1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    input2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across ").lower()
    if input2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        input3 = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
        if input3 == "yellow":
            print("Congratulations, you've found the treasure!")
        elif input3 == "red":
            print("It's a room full of fire. Game over.")
        elif input3 == "blue":
            print("You entered a room full of beast. Game over.")
        else:
            print("Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")


"""***
"left")
print("You've coem to a lake. There is an island in the middle of the lake")
print("You arrive at the island unharmed. There is a house with 3 doors.")
print("One red, one yellow and one blue. Which colour do you choose?")
"""