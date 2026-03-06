In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number.

# **The Program in Action**
```
When you run bagels.py, the output will look like this:
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
```
# **How It Works**


Keep in mind that this program uses not integer values but rather string
values that contain numeric digits. For example, '426' is a different value
than 426. We need to do this because we are performing string comparisons
with the secret number, not math operations. Remember that '0' can be
a leading digit: the string '026' is different from '26', but the integer 026 is
the same as 26.

```python
"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:      That means:
Pico             One digit is correct but in the wrong position.
Fermi            One digit is correct and in the right position.
Bagels           No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""

    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
```

After entering the source code and running it a few times, try making

experimental changes to it. The comments marked with (!) have sugges-
tions for small changes you can make. On your own, you can also try to fig-
ure out how to do the following:

- Change the number of digits for the secret number by changing `NUM_DIGITS`.
- Change the number of guesses the player gets by changing `MAX_GUESSES`.
- Try to create a version with letters as well as digits in the secret number.

# **Exploring the Program**

Try to find the answers to the following questions. Experiment with some
modifications to the code and rerun the program to see what effect the
changes have.
1. What happens when you change the `NUM_DIGITS` constant?
2. What happens when you change the `MAX_GUESSES` constant?
3. What happens if you set `NUM_DIGITS` to a number larger than 10?
4. What happens if you replace `secretNum = getSecretNum()` on line 30 with
`secretNum = '123'`?
5. What error message do you get if you delete or comment out `numGuesses
= 1` on line 34?
6. What happens if you delete or comment out `random.shuffle(numbers)` on
line 62?
7. What happens if you delete or comment out `if guess == secretNum:` on
line 74 and `return 'You got it!'` on line 75?
8. What happens if you comment out `numGuesses += 1` on line 44?



  
