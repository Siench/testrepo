import random

word_list = ["mamifero", "escorpion", "programacion", "calculadora"]
word_to_guess = random.choice(word_list)

guesses = []
lives = 6
correct_guesses = []
incorrect_guesses = []

def create_hidden_word(word, correct_guess):
  hidden_word = ""
  for letter in word:
    if letter in correct_guess:
      hidden_word += letter
    else:
      hidden_word += "_"
  return hidden_word

while lives > 0:
  hidden_word = create_hidden_word(word_to_guess, correct_guesses)
  print("**********")
  print("Secret word:", hidden_word)
  print("Guesses made:", guesses)
  print("Correct guesses:", correct_guesses)
  print("Incorrect guesses:", incorrect_guesses)
  print("Lives remaining:", lives)
  print("**********")
  print("\n")
  user_char_input = input("Enter a letter: ")
  guesses.append(user_char_input)
  print("\n")

  if user_char_input in word_to_guess:
    if user_char_input not in correct_guesses:
      correct_guesses.append(user_char_input)
      print("Correct guess!\n")
  else:
    lives -= 1
    incorrect_guesses.append(user_char_input)
    print(f"Incorrect guess. Lives remaining: {lives}\n")

  if set(correct_guesses) == set(word_to_guess):
    print("Congratulations! You win!\n")
    break

if lives == 0:
  print("You lose. The word was:", word_to_guess)