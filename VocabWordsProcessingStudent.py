## This program allows a user to work with vocabulary words.
# @author Joseph Kern
import random

def main() :
    vocabWords = {}
    getWords(vocabWords, "vocabWords.txt")

    # Menu options
    ADD_WORD = 1
    REMOVE_WORD = 2
    DISPLAY_WORDS = 3
    DISPLAY_WORDS_BY_LETTER = 4
    QUIZ_WORD = 5
    EXIT = 6

    # Continue to process requests until the user decides to exit.
    userChoice = 0
    while (userChoice != EXIT) :
        # Display the menu choices
        print("1) Add word and definition")
        print("2) Remove word")
        print("3) Display all words")
        print("4) Display words with same first letter")
        print("5) Quiz word")
        print("6) Exit")
        
        
        userChoice = int(input("Your choice: "))
        
        if (userChoice == ADD_WORD) :
            addWord(vocabWords)

        elif (userChoice == REMOVE_WORD) :
            removeWord(vocabWords)

        elif (userChoice == DISPLAY_WORDS) :
            showWords(vocabWords)

        elif (userChoice == DISPLAY_WORDS_BY_LETTER) :
            letter = input("Which letter? ")
            showWordsByLetter(vocabWords, letter)

        elif (userChoice == QUIZ_WORD) :
            quizWord(vocabWords)
        if (userChoice != EXIT) :    
            input("\nPress enter to continue")
            print()            

    storeWords(vocabWords, "vocabWordsNew.txt")

    print("Goodbye")

def addWord (words):
    newWord = input("Word: ")
    words[newWord] = input("Definition: ")
    print(f"{newWord} added.")

def removeWord (words):
    removeWord = input("Word to remove: ")
    if (removeWord in words):
        words.pop(removeWord) 
        print(f"{removeWord} removed from the vocabulary.")
    else:
        print(f"{removeWord} not found.")

# **showWords displays all the words and their definitions
# in ascending sorted order by words.
# @param words The current dictionary of vocabulary words
def showWords (words):
    for word in sorted(words):
        print(f"{word}: {words[word]}")

# **showWordsByLetter displays all the words that begin with a particular
# letter and their definitions in sorted order by words.
# @param words The current dictionary of vocabulary words
# @param letter The letter which the words must start with
def showWordsByLetter (words, letter):
    for word in sorted(words):
        if (word.find(letter.lower()) == 0):
            print(f"{word}: {words[word]}")


# **quizWord presents a randomly selected definition to the user, gives a
# hint as to which letter it starts with, and provides up to 3 tries for the
# correct word to be answered. The correct word is displayed if the word
# was not guessed in three tries.
# @param words The current dictionary of vocabulary words 
def quizWord(words):
    
    # Select random word
    word = random.choice(list(words))
    MAX_TRIES = 3
    numGuesses = 0    
    
    # Run guess loop
    while (numGuesses < MAX_TRIES):
        print(f"Definition: {words[word]}")
        guess = input(f"What is the word? (Begins with {word[0]}) ")
        if (guess == word):
            print("Correct!")
            numGuesses = MAX_TRIES + 1
        else:
            print("Incorrect")
            numGuesses += 1
            
    # Display correct answer if wrong
    if (numGuesses == MAX_TRIES):
        print(f"The correct word was: {word}")

# **storeWords stores the vocabulary dictionary back to file
# @param words The dictionary of word/definition pairs to store
# @param outFileName The name of the file where the new words are stored
def storeWords (words, outFileName):
    outFile = open(outFileName, "w")
    for word in words:
        outFile.write(f"{word}={words[word]}\n")

# getWords retrieves the set of words and their definitions from file
# @param words Empty dictionary that will store the word/definition pairs
# @param inFilename The name of the file to read
def getWords(words, inFileName):
    inFile = open(inFileName, "r")
    
    # For each line in the file, if it is a valid line with more than
    # one character, strip the trailing newline character,  parse it on
    # the =, and store into the dictionary
    for line in inFile :
        if (len(line) > 1) :
            line = line.rstrip()
            (word, definition) = line.split("=")
            words[word] = definition
    
    inFile.close()
    
main()