import random
from Hangman_art import logo, stages
from Hangman_words import word_list
from replit import clear

print(logo)
end_of_game = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display += '_'

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    clear()

    if guess in display:
        print(f'You have already guessed {guess}')

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f'{guess} is not in the word. Lose a life bitch!')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'The word is {chosen_word}. You suck! Looser.')

    print(stages[lives])

    if '_' not in display:
        end_of_game = True
        print('You fucking Win!')
