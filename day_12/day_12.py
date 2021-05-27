import art
import random

print(art.logo)

number = random.randint(1, 101)
level = input("Which difficulty you choose? Type 'easy' for 10 chances and type 'hard' for 5 chances. ")
while not (level == 'easy' or level == 'hard'):
    level = input("Please type 'easy' or 'hard to move on.")
if level == 'easy':
    guests = 10
else:
    guests = 5
while guests > 0:
    print(f"You have {guests} attempts remaining to guess the number.")
    pick = int(input("Type your guess: "))
    while pick not in range(1, 101):
        pick = int(input("Please type correct number."))
    if pick == number:
        print("Congratulation, You won!")
        break
    elif pick > number:
        print("Too high.")
        guests -= 1
    else:
        print("Too low.")
        guests -= 1
if not guests > 0:
    print("You lost.")
