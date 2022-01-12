import random

word_list = ["aardvark", "baboon", "camel", "farmer", "Obama", "Jordan"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Make a guess. Enter a letter: ")

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
