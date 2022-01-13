import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
# print(f'The solution is {chosen_word}.')

#Create blanks
word_in_blank = []
for blank in range(word_length):
    word_in_blank += "_"

while "_" in word_in_blank:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in word_in_blank:
        print(f"You\'ve already guessed \'{guess}\'.")

    #Check guessed letter
    for i in range(word_length):
        if chosen_word[i] == guess:
            word_in_blank[i] = guess

        # #letter = chosen_word[i]        
        # if letter == guess:
        #     word_in_blank[i] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in word_in_blank:
            print(f"This is not in the chosen word: \'{guess}\'. You are one step closer to be hanged.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(word_in_blank)}")

    #Check if user has got all letters.
    if "_" not in word_in_blank:
        game_over = True
        print("You won!")

    #Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
