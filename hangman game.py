from hangman_word import word_list
from hangman_art import stages,logo

import random

lives = 6
print(logo)


chosen_word=random.choice(word_list).lower()


placeholder= ""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over=False
correct_letters=[]
while not game_over:
    print(f"{lives} /6 lives left...")
    guess=input("Guess a letter: ").lower()
    if guess in correct_letters:
       print(f"You've already guessed {guess}")

    display =""  

    for letter in chosen_word:
      if letter==guess:
        display+=letter
        correct_letters.append(letter)
      elif letter in correct_letters:
        display +=letter  
      else:
        display +="_"  
    print(display)

    

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word.You lose a life.")
        if lives == 0:
            game_over = True
            print(f"It was the {chosen_word} word.You lose!")  


    if "_" not in display:
        game_over=True
        print("you win.") 
    print(stages[lives])      

    