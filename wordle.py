import random
import os, time
words = ["stain","ratio","irate","stare","arise","roast","frame","graze","windy","paint","gourd","swing","audio","ready","pears","chief","touch","turns","stole","vowel","first","roast","meats","wrist","tough","daily","wheel","games","start","notes","money","value","float","perky","phone","hello","beans","books","jokes","thing","niece","smell","check","leave","barks","quick","think","doors","water","going","flaps","scurf","splay", "mouse","light","touch","boxes","flank","adult","agent","apple","beach","earth","drive","entry","fault","field","faith","final","force","major","metal","money","moter","power","river","ratio","price","plane","peace","reply","steel","stock","stone","watch","youth","value","video"]
word = random.choice(words)

word = word.lower()
#word = "hello"
x = 0
os.system('clear')
lettersCorrect = 0
print("the word is",len(word),"letters long \n")
guesses = 0


def dumbVal():
  if guesses == 1:
    return "st"
  elif guesses == 2:
    return "nd"
  elif guesses == 3:
    return "rd"
  elif guesses > 3:
    return "th"
output = []
redWords = []
yellowWords = []
greenWords = []
allLetters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


    

if len(word) != 5:
    print("ERROR word is over 5 characters")
while True:
    if guesses == 5:
      print("   You are out of guesses!")
      break
    guesses = guesses + 1
    print("\n")
    print("")


    for i in range (0,26):
        if allLetters[i] in list(yellowWords):
            print("\033[1;33m   " + (allLetters[i]) , end = '')

        elif allLetters[i] in list(redWords):
            print("\033[1;31m " + allLetters[i], end = '')

        elif allLetters[i] in list(greenWords):
            print("\033[1;32m " + allLetters[i], end = '')

        else:
            print("\033[1;30m " + allLetters[i], end = '')

    



    print("\n")
    print("\033[1;34m ")
    guess = input(str(guesses)  + dumbVal() + ' guess: ').lower()
    if len(guess) == 5:

        os.system('clear')

    
    #os.system('clear')


        for x in range (0,5):
            if word[x] == guess[x]: # green
                lettersCorrect = lettersCorrect + 1
            
                print("\033[1;32m ", guess[x], end = '')
                if guess[x] not in greenWords:
                    greenWords.append(guess[x])
            
            elif guess[x] in str(word):  # yellow
                print("\033[1;33m " ,guess[x], end = '')
                if guess[x] not in yellowWords:
                    yellowWords.append(guess[x])

            else: 
                print("\033[1;31m " ,guess[x], end = '') # red
                if guess[x] not in redWords:
                    redWords.append(guess[x])
                #blueWords.remove(guess[x])

            x = x + 1
 

        if guess == word:
            print("Yay!")
            break
    else:
        os.system('clear')
        print("Guess Must be 5 letters in length")
