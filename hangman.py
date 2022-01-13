import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

chosen_word = random.choice(word_list)
#print(chosen_word)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You\'ve already guessed \'{guess}\'.")
