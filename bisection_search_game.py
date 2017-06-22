print('Please think of a number between 0 and 100!')

low = 0
high = 100

selection = 'x'

while selection != 'c' : 
  guess = int((low+high)/2)
  print("Is your secret number " + str(guess) +"?")
  
  print("Enter 'h' to indicate the guess is too high.",end=' ')
  print("Enter 'l' to indicate the guess is too low.",end=' ')
  print("Enter 'c' to indicate I guessed correctly.",end=' ')

  selection = input()
  if selection == 'h':
    high = int((low+high)/2)
  elif selection == 'l':
    low = int((low+high)/2)
  elif selection == 'c' :
    break
  else:
    print ("Sorry, I did not understand your input.")
  
print("Game over. Your secret number was: " + str(guess))
