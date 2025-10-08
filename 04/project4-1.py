# Rock Paper Scissors

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

graphic = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

computer_choice = random.randint(0, 2)
print(f"Computer choose: {computer_choice}")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print('Error')

print(f"You chose: {your_choice}")

if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)
else:
    print('Error')


if computer_choice == 0 and your_choice == 0:
    print("It's a tie.")
elif computer_choice == 0 and your_choice == 1:
    print("You win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose.")
elif computer_choice == 1 and your_choice == 0:
    print("You win!")
elif computer_choice == 1 and your_choice == 1:
    print("It's a tie.")
elif computer_choice == 1 and your_choice == 2:
    print("You lose.")
elif computer_choice == 2 and your_choice == 0:
    print("You win!")
elif computer_choice == 2 and your_choice == 1:
    print("You lose.")
elif computer_choice == 2 and your_choice == 2:
    print("It's a tie.")
else:
    print("Invalid choice")