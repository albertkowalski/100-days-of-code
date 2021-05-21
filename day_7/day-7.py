# Hangman Game
# Made using strings instead of lists

import random
import hangman_words
import art


print(art.logo)
word = random.choice(hangman_words.word_list)
word_underscored = ""
for letter in word:
    word_underscored += "_"
print(f"Hidden word is: {word}")
print(word_underscored)
lives = 6
game_won = False
while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in word_underscored:
        print("You already guessed this letter")
    else:
        for index in range(len(word)):
            if guess == word[index]:
                word_underscored = word_underscored[:index] + word[index] + word_underscored[index+1:]
        if word == word_underscored:
            game_won = True
            break
        if guess not in word:
            print(f"There is no {guess} in the word. You lose a life")
            lives -= 1
        print(f"{word_underscored} \n  {art.stages[lives]}")

if game_won:
    print("Congratulation, You won!")
else:
    print("Game Over. You lost!")
