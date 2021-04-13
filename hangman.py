import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    wordcomp = '_' * len(word)
    guessed = False
    guessedlets = []
    tries = 6
    print('Let\'s play!')
    print('The word has', len(word), 'letters.')
    print(display_hangman(tries))
    print(wordcomp)
    print('\n')
    while not guessed and tries > 0:
        glet = input('Guess a letter: ').upper()
        if glet.isalpha():
            if glet not in word:
                print('Wrong!')
                tries -= 1
                guessedlets.append(glet)
            elif glet in guessedlets:
                print('You already guessed that.')
            else:
                print('Correct!')
                guessedlets.append(glet)
                wordlst = list(wordcomp)
                indices = [i for i, letter in enumerate(word) if letter == glet]
                for index in indices:
                    wordlst[index] = glet
                wordcomp = ''.join(wordlst)
                if '_' not in wordcomp:
                    guessed = True
        else:
            print('Not a valid character.')
        print(display_hangman(tries))
        print(wordcomp)
        print('\n')
    if guessed and tries > 0:
        print('Congrats, you found it!!')
    elif tries == 0:
        print('Sorry mate, the word was:', word)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input('Play again?   (Y/N)').upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()