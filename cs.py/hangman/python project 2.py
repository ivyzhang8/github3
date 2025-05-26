import random
import string

# word list file
WORDLIST_FILENAME = "./hangman/words.txt"

# loading words from file
def loadWords():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.readline().split()
        print(f"{len(wordlist)} words loaded.")
    return wordlist

# choosing a word
def chooseWord(wordlist):
    return random.choice(wordlist)

# checking your answer
def isWordGuessed(secretWord, lettersGuessed):
    return all(letter in lettersGuessed for letter in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    return ''.join(letter if letter in lettersGuessed else '_' for letter in secretWord)


def getAvailableLetters(lettersGuessed):
    return ''.join(letter for letter in string.ascii_lowercase if letter not in lettersGuessed)

# hangman functions
def hangman(secretWord):
    print("Welcome to Hangman!")
    print(f"The word has {len(secretWord)} letters.")
    lettersGuessed = []
    guessesLeft = 8

    while guessesLeft > 0:
        print(f"\nYou have {guessesLeft} guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        print("Letters guessed so far:", lettersGuessed)  
        guess = input("Please guess a letter: ").lower()

      #if statements
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue

        if guess in lettersGuessed:
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                return
        else:
            guessesLeft -= 1
            lettersGuessed.append(guess)
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
        
        
        print(f"Guesses left after this round: {guessesLeft}")

    print(f"Sorry, you ran out of guesses. The word was '{secretWord}'.")

# running the game
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
