import random

HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 ========''','''

   +---+
   |   |
   0   |
       |
       |
       |
 ========''','''

   +---+
   |   |
   0   |
   |   |
       |
       |
 ========''','''

   +---+
   |   |
   0   |
   |\  |
       |
       |
 ========''','''

   +---+
   |   |
   0   |
  /|\  |
       |
       |
 ========''','''

   +---+
   |   |
   0   |
  /|\  |
   |   |
       |
 ========''','''

   +---+
   |   |
   0   |
  /|\  |
   |   |
    \  |
 ========''','''

   +---+
   |   |
   0   |
  /|\  |
   |   |
  / \  |
 ========''']


words = {'Animals':'baboon badger bat bear beaver camel at clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger trout turkey weasel whale wolf wombat zebra'.split(),
         'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0,len(wordDict[wordKey])-1)

    return [wordDict[wordKey][wordIndex],wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed Letters:',end=' ')
    for letter in missedLetters:
        print(letter,end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if(len(guess)) != 1:
            print('Please enter a single letter...')
        elif(guess in alreadyGuessed):
            print('You have already guessed that letter. Choose another one...')
        elif(guess not in 'abcdefghijklmnopqrstuvwxyz'):
            print('Please enter a LETTER...')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')

            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if(len(missedLetters) == len(HANGMANPICS)-1):
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct gusses, the word was "' + secretWord + '".')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break

