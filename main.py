import random

words = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'pineapple', 'watermelon']
selected_word = random.choice(words)
blanks = '_' * len(selected_word)
remaining_chances = 5

while '_' in blanks and remaining_chances > 0:
  print(blanks)
  print(f"Remaining chances: {remaining_chances}")
  guess = input("Guess a letter: ").lower()

  if guess in selected_word:
    for i in range(len(selected_word)):
      if selected_word[i] == guess:
        blanks = blanks[:i] + guess + blanks[i+1:]
  else:
    remaining_chances -= 1
  if '_' not in blanks:
    print(f"You guessed the Right Word!")
    break
  elif remaining_chances == 0:
    print("You lose!")
    print(f"The word was: {selected_word}")
    break