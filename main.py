#Allows for random.choice() to be used
import random
#Stopwatch timer
import time 

wins = 0
losses = 0
attempts = 0
globalLoop = True 
mainLoop = True 
guessLoop = True #Loop for user guessing

#Word Bank for categories
foodwordsList = ['mango', 'dragonfruit', 'pineapple', 'macaron', 'croissant', 'eggroll', 'mushroom', 'hummus', 'sashimi', 'burrito', 'quesadilla', 'dumpling', 'blackberry', 'raspberry', 'cantaloupe', 'cashew', 'chocolate', 'cucumber', 'doughnut', 'durian', 'hamburger', 'halibut', 'jackfruit', 'lasagna', 'lobster', 'macaroni', 'potatoes', 'marshmallow', 'oatmeal', 'pasta', 'pomegranate', 'popcorn']
animalsList = ['penguin', 'beaver', 'sheep', 'buffalo', 'chimpanzee', 'chameleon', 'clownfish', 'chipmunk', 'dolphin', 'donkey', 'elephant', 'eagle', 'falcon', 'flamingo', 'giraffe', 'gorilla', 'gazelle', 'hippo', 'horse', 'jellyfish', 'salmon', 'kangaroo', 'koala', 'lobster', 'leopard', 'llama', 'monkey', 'octopus', 'ostrich', 'parrot', 'pigeon', 'piranha', 'platypus', 'turtle', 'peacock', 'pufferfish', 'porcupine', 'raccoon', 'rhinoceros', 'sparrow', 'squirrel', 'starfish', 'swordfish', 'urchin', 'vulture', 'zebra']
countriesList = ['china', 'canada', 'japan', 'argentina', 'austria', 'brazil', 'germany', 'belgium', 'cuba', 'denmark', 'sweden', 'egypt', 'ecuador', 'france', 'finland', 'greece', 'hungary', 'iceland', 'india', 'ireland', 'italy', 'singapore', 'ireland', 'korea', 'kyrgyzstan', 'mexico', 'madagascar', 'netherlands', 'poland', 'philippines', 'portugal', 'russia', 'spain', 'switzerland', 'thailand', 'ukraine', 'vietnam', 'zimbabwe']
coloursList = ['purple', 'blue', 'orange', 'cyan', 'green', 'violet', 'magenta', 'silver', 'brown', 'black', 'white', 'yellow', 'indigo']
randomList = foodwordsList + countriesList + animalsList + coloursList

#SOUND EFFECTS
# from replit import audio

#Function for drawing current state of hangman
def attempt():
  #NEW FUNCTION
  global losses
  global mainLoop
  global guessLoop
  global categoryLoop
  if attempts == 0:
    hangman0()
  elif attempts == 1:
    hangman1()
  elif attempts == 2:
    hangman2()
  elif attempts == 3:
    hangman3()
  elif attempts == 4:
    hangman4()
  elif attempts == 5:
    hangman5()
  elif attempts == 6:
    hangman6()
    # source1 = audio.play_file("buzzer-or-wrong-answer-20582.mp3")
    endtime = time.time()
    print('\033[1m'"YOU LOSE!!!!!"'\033[0m')
    print(f"{word:s} is the correct answer!")
    losses = losses + 1
    print(f"You currently have {wins:d} wins and {losses:d} losses!")
    stopwatch = int(endtime - start_time)
    print(f"That hangman round took you {stopwatch:d} seconds!")
    print("\n")
    mainLoop = False
    guessLoop = False
    globalLoop = True
    

#Function for each stage of hangman
def hangman0():
  print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')


def hangman1():
  print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
def hangman2():
  print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
  
def hangman3():
  print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
        
def hangman4():
  print( '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

def hangman5():
  print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

def hangman6():
  print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

#Function for word selection for the user
def word_selection(category):
  word = random.choice(category)
  wordlength = len(word)
  print(wordlength * "__ ")
  return word

#Main function for user guessing selected word
def main():
  global wins
  global losses
  global attempts
  global guessLoop
  global mainLoop
  guessLoop = True
  correct_guessed_letters = []
  guessed_words = []
  incorrect_guessed_letters = []
  #guessing system
  while guessLoop:
      guess = input("Please enter a letter: ")
      currentword = ""
      if guess.isalpha() == True:
        if guess.lower() == word:
          # source = audio.play_file("khan-academy-sound-1.mp3")
          endtime = time.time()
          print(f"{guess:s} is the correct word!")
          print('\033[1m'"Congrats! YOU WIN!"'\033[0m')
          print("\n")
          wins = wins + 1
          print(f"You currently have {wins:d} wins and {losses:d} losses!")
          stopwatch = int(endtime - start_time)
          print(f"That hangman round took you {stopwatch:d} seconds!")
          print("\n")
          
          guessLoop = False
          mainLoop = False
        elif len(guess) > 1:
          print("Please guess a single letter without spaces or the entire word!")
        elif guess.lower() in incorrect_guessed_letters or guess.lower() in correct_guessed_letters:
          print("You have already guessed that letter!")
          continue
        elif guess.lower() in word:
          # source = audio.play_file("khan-academy-sound-1.mp3")
          print(f"Good job! {guess:s} is in the word!")
          correct_guessed_letters.append(guess.lower())
          print("Correct letters: ", correct_guessed_letters)
          print("Incorrect letters: ",incorrect_guessed_letters)
          attempt()
          print("\n")
      
          for guess in word:
            if guess.lower() in correct_guessed_letters:
              currentword += guess + " "
            else:
              currentword += "__ "
          print("Current Word: ", currentword)
          print("\n")
          word_check = True
          while word_check:
            if "__" in currentword:
              break
            else:
              # source = audio.play_file("khan-academy-sound-1.mp3")
              endtime = time.time()
              print('\033[1m'"Congrats! YOU WIN!"'\033[0m')
              wins = wins + 1
              print(f"You currently have {wins:d} win and {losses:d} losses!")
              stopwatch = int(endtime - start_time)
              print(f"That hangman round took you {stopwatch:d} seconds!")
              print("\n")
              guessLoop = False
              mainLoop = False
              break
        else:
          # source1 = audio.play_file("buzzer-or-wrong-answer-20582.mp3")
          print(f"Try again! {guess:s} is not in the word")
          incorrect_guessed_letters.append(guess)
          print("Correct letters: ", correct_guessed_letters)
          print("Incorrect letters: ",incorrect_guessed_letters)
          attempts = attempts + 1
          attempt()
          for guess in word:
            if guess.lower() in correct_guessed_letters:
              currentword += guess + " "
            else:
              currentword += "__ "
                
          print("Current Word: ", currentword)
          print("\n")
      else:
        print("Please guess a single letter without spaces or the entire word!")


#Main Program
wins = 0
losses = 0
while globalLoop:
  try:
    print("=" * 90)
    print('\033[1m'"Welcome to Hangman!"'\033[0m')
    decision = input("Would you like to play? Yes/No: ")
    print("=" * 90)
    mainLoop = True
    while mainLoop:
      categoryLoop = True
      while categoryLoop:
        if decision.lower() in ["no", "n", "nope", "noo", "nah", "absolutely not", "no thanks", "bye"]:
          print("See you next time!")
          mainLoop = False
          globalLoop = False
          break
          
        elif decision.lower() in ["yes", "y", "ye", "yup", "affirmative", "of course", "yep", "sure", "yuh", "yeh"]:
          print("You will be given a vocabulary word that you will attempt to guess. You can guess one letter at a time or the entire word. Once the hangman has been fully drawn, you lose!")
          print("\n")
          # print('\033[1m'"Please do not input letters too quickly as it will slow down the program!"'\033[0m')
          print("\n")
          category = input("What category of vocabulary would you like to choose? (Colours [EASY], Animals [MED], Food [MED], Countries [HARD], Random [SUPER HARD]): ")
          categoryLoop = False
        else:
          print("Please respond with Yes/Y or No/N.")
          print("\n")
          decision = input("Would you like to play? Yes/No: ")
          break
  
        if category.lower() == "food":
          attempts = 0
          print("You have selected Food!")
          start_time = time.time()
          print("\n")
          word = word_selection(foodwordsList)
          main()
        elif category.lower() == "countries":
          attempts = 0
          print("You have selected Countries!")
          start_time = time.time()
          print("\n")
          word = word_selection(countriesList)
          main()
        elif category.lower() == "animals":
          attempts = 0
          print("You have selected Animals!")
          start_time = time.time()
          print("\n")
          word = word_selection(animalsList)
          main()
        elif category.lower() == "random":
          attempts = 0
          print("You have selected Random!")
          start_time = time.time()
          print("\n")
          word = word_selection(randomList)
          main()
          
        elif category.lower() == "colours":
          attempts = 0
          print("You have selected Colours!")
          start_time = time.time()
          print("\n")
          word = word_selection(coloursList)
          main()
        else:
          print("\n")
          print('\033[1m'"Please select one of the provided options"'\033[0m')
          print("\n")
#Prevents error from occuring when pressing Ctrl + C, instead ends program
  except KeyboardInterrupt:
    print("\n")
    print('\033[1m'"Game has been interrupted. Closing program."'\033[0m')
    globalLoop = False
    mainLoop = False
    break


endtime = time.time()
stopwatch = print("Total Time:",int(endtime - start_time))

#FEEL FREE TO DISPLAY COMMENTS