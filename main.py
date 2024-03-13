secretWord = "Indonesia"
guessedLetter = []
chances = 6

while chances <= 6:
  guess = input("Guess my letter")

  if len(guess)!=1:
    print("Please enter only one letter")
  elif not guess.isalpha():
    print("please give me one letter")
  elif guess.lower() in guessedLetter:
    print("u guessed that already")
  else:
    guessedLetter.append(guess.lower())
    if guess.lower() in secretWord.lower():
      print("congrats you guessed a letter")
    else:
      chances -= 1
      print("Better luck next time. You have {} chances left.".format(chances))

  display = ""
  for letter in secretWord:
    if letter.lower() in guessedLetter: 
      display += letter
    else:
      display += "_"
  print(display)
  
  if "_" not in display:
    print("Congratulations! You guessed the word:", secretWord) 
    break
  if chances == 0:
    print("Sorry, you ran out of chances. The word was:", secretWord)