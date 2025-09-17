#test guess number

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Guess number 
          Try to guess what it's. Here are some clues:
          When I Say:   That means:
          Pico           One digit is correct but in the wrong position.
          Fermi          One digit os correct and in the right position.
          Bagels         No digit is correct.
          
          For example, if the secret number was 248 and you guess was 843, the clues would be Fermit.
          ''', format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum().upper()
        print('I have thought up a number')
        print('You have {} guessesto get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isalnum():
                print('Guesses #{}:'.format(numGuesses))
                guess = input('> ').upper()
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    
    numbers = list('123sds')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()