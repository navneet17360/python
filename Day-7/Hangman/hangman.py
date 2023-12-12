import random

from hangman_words import word_list


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

end_of_game = False
lives=6

chosen_word = random.choice(word_list)
length_chosen_word = len(chosen_word)
# print(chosen_word)
display = ["_" for _ in range(length_chosen_word)]

while not end_of_game:
    guess_letter = input("Please enter:").lower()

    for position in range(length_chosen_word):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter


    if guess_letter not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")
    






    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    
    
    print(stages[lives])
    

