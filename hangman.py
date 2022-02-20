import random
from string import ascii_lowercase


def is_input_correct(input_: str) -> bool:
    if len(input_) > 1:
        print('You should input a single letter')
        return False

    if input_ not in ascii_lowercase:
        print('Please enter a lowercase English letter')
        return False

    return True


# constants
words = ['python', 'java', 'kotlin', 'javascript']
current_lives = 8
lives = current_lives
hyphens = '-'


# start the game
word = random.choice(words)
puzzle = list(hyphens) * len(word)
history = []

print('H A N G M A N')

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        lives = current_lives
        puzzle = list(hyphens) * len(word)
        history = []
    elif choice == 'exit':
        exit()
    else:
        continue

    while lives:
        # print()
        print("\n", ''.join(puzzle), sep='')

        if list(puzzle) == list(word):
            print('You guessed the word!\nYou survived!\n')
            break

        user_input = input('Input a letter: ')

        if not is_input_correct(user_input):
            continue

        if user_input in puzzle:
            print('You\'ve already guessed this letter')
        if user_input in history:
            print('You\'ve already guessed this letter')
        if user_input not in word and user_input not in history:
            print('That letter doesn\'t appear in the word')
            history.append(user_input)
            lives -= 1

        if user_input in word:
            for letter_number in range(len(word)):
                if word[letter_number] == user_input:
                    puzzle[letter_number] = user_input
        # lives -= 1

        if lives <= 0:
            print('You lost!\n')
            break
# print("""\nThanks for playing!
# We'll see how well you did in the next stage""")
