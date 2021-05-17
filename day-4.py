import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
states = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
cpu_choice = random.randint(0, 2)
if player_choice in [0,1,2]:
    print(f"Your choice is: {states[player_choice]}")

    print(f"CPU choice is: {states[cpu_choice]}")

    if player_choice == cpu_choice:
        print("Draw!")
    elif player_choice - cpu_choice == -1 or player_choice - cpu_choice == 2:
        print("You lost")
    else:
        print("You won")
else:
    print("You have chosen wrong number!")
