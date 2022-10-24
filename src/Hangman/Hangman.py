'''
NOTES
 Level 1: Easy Peasy Lemon Squeezy ..... 3-10 letters
 Level 2: Using Your Brains ..... 11+ letters
 Level 3: Rage Quit ..... 1+ words
 '''


import random
from IPython.display import clear_output

WORDS = ['mouse', 'animals', 'dinosaur', 'fly', 'dog', 'cat', 'grater', 'cheese', 'mat', 'sat', 'algebra', 'test',
         'aquamarine', 'emeralds', 'winnie the pooh', 'act', 'add', 'subtract', 'difference', 'difficult', 'explain',
         'expert', 'zoo', 'cage', 'bird', 'out', 'own', 'paint', 'part', 'paper', 'pay', 'past', 'six', 'optic', 'eye',
         'mouth', 'hand', 'hair', 'harp', 'hare', 'sun', 'son', 'bug', 'lip', 'box', 'tree', 'table', 'talking', 'run',
         'walk', 'leaf', 'sheep', 'flock', 'herd', 'army', 'bank', 'ball', 'home', 'house', 'goal', 'gear', 'game',
         'wind', 'kind', 'zone', 'zero', 'splash', 'can', 'cub', 'cup', 'cow', 'fawns', 'fated', 'force', 'femur',
         'lemur', 'feral', 'ebony', 'black', 'red', 'bone', 'regard', 'annual', 'anyone', 'artist', 'bellows', 'forge',
         'school', 'college', 'old', 'young', 'career', 'store', 'car', 'beyond', 'honor', 'ticket', 'train', 'ship',
         'abolish', 'arachnophobia', 'zoology', 'geography', 'america', 'amnesia', 'insomnia', 'paranoia', 'pyromaniac',
         'megalomaniac', 'immobilize', 'matriarch', 'pediatrician', 'cardiologist', 'disintegrate', 'discombobulate',
         'denounce', 'hilarious', 'exceptional', 'magnificent', 'rhythm', 'cartography', 'photosynthesis', 'botanist',
         'bacteria', 'campaign', 'birthday', 'happened', 'payments', 'strategy', 'suddenly', 'beautiful', 'dedicated',
         'displayed', 'delivered', 'frequency', 'interview', 'practical', 'recommend', 'sometimes', 'temporary',
         'amendment', 'behaviour', 'commander', 'abdicated', 'abducting', 'abolishes', 'activator', 'abbreviate',
         'acquiesced', 'accessible', 'agoraphobia', 'bamboozled', 'bald', 'balderdash', 'ballerina', 'bicyclists',
         'ambidextrous', 'synchronization', 'blackjack', 'blissfully', 'blindfolds', 'blundering', 'floppy', 'flower',
         'seed', 'nursery', 'cannibal', 'ravioli', 'canvas', 'capacity', 'capability', 'capsize', 'grammatical',
         'pneumonoultramicroscopicsilicovolcanoconiosis', 'pseudopseudohypoparathyroidism',
         'floccinaucinihilipilification', 'antidisestablishmentarianism', 'supercalifragilisticexpialidocious',
         'incomprehensibilities', 'strengths', 'guinness', 'record', 'language', 'euouae',
         'honorificabilitudinitatibus', 'honor', 'uncopyrightable', 'subdermatoglyphic', 'sesquipedalianism', 'possess',
         'pneumonoultramicroscopicsilicovolcanoconiosis', 'wolf', 'adjective', 'island', 'hawaii', 'hymn', 'lynx',
         'xylophone', 'pygmy', 'gym', 'hunch', 'psychopath', 'detective', 'myth', 'flibbertigibbet', 'redundant']

SENTENCES = ['fat cat sat on the mat by the door', 'it rained today', 'i like cheese', 'pigs are cute',
             'the horse galloped across the plains', 'was this hard enough for you',
             'the quick brown fox leaped over the lazy dog', 'The squishy frog squelched through the mud',
             'bibbitty bobbity boo', 'i will always return', 'jack and jill went up a hill',
             'how much wood can a woodchuck chuck if a woodchuck could chuck wood', 'sally sold seashells by the seashore',
             'the cat and dog yowled and howled', 'the pen is mightier than the sword', 'better safe than sorry',
             'the moose is swimming the water', 'i am on fire please help', 'there once was a boy name harry who was destined to be a star',
             'sometimes the early bird does not get the worm', 'happy hunger games may the odds the ever in your favor',
             'destroying things is much easier than making them', 'with great power come a great need to take a nap',
             'life is only precious because it ends', 'do you always kill people when they blow their nose', 'my goal is to move just enough so people know I am still alive',
             'think of yourself not as an ugly person but as a beautiful monkey', 'keep calm and stay strong']


# FUNCTIONS
def get_guess_text(level):
    if level == 1:
        lvl_nums = (3, 10)
    elif level == 2:
        lvl_nums = (11,100)
    elif level == 3:
        sentence = random.choice(SENTENCES)
    while True:
        word = random.choice(WORDS)
        if level == 1:
            if lvl_nums[0] <= len(word) <= lvl_nums[1]:
                return word.upper()
        elif level == 2 and lvl_nums[0] <= len(word) <= lvl_nums[1]:
            return word
        elif level == 3:
            return sentence.upper()

def make_dashes(text):
    text = text.split()
    dashes = []
    for word in text:
        dashes.append('_'*(len(word)))
    dashes_string = ' '.join(dashes)

    final_dashes = []
    for part in dashes_string:
        final_dashes.append(part)

    return final_dashes

def wrong_guess(mylist):
    if len(mylist) == 0:
        print('____________________\n|  /               |\n| /                 \n|/                 \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("1/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 1:
        print('____________________\n|  /               |\n| /              =====\n|/              ( o_o )\n|                =====\n|                   \n|                  \n|                   \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("2/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 2:
        print('____________________\n|  /               |\n| /              =====\n|/              ( o_o )\n|                =====\n|                  |  \n|                  \n|                   \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("3/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 3:
        print('____________________\n|  /               |\n| /              =====\n|/              ( o_o )\n|                =====\n|                  |  \n|                  |  \n|                   \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("4/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 4:
        print('____________________\n|  /               |\n| /              =====\n|/              ( o_o )\n|                =====\n|                  |  \n|                  |  \n|                   \ \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("5/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 5:
        print('____________________\n|  /               |\n| /              =====\n|/              ( o_o )\n|                =====\n|                  |  \n|                  |  \n|                 / \ \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("6/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 6:
        print('____________________\n|  /               |\n| /              =====\n|/              ( 0o0 )\n|                =====\n|                --|  \n|                  |  \n|                 / \ \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("7/8 Life Savers Used: Don't use up all of your 8 lifesavers, or Bob will ...")
    elif len(mylist) == 7:
        print('____________________\n|  /               |\n| /              =====\n|/              ( x_x )\n|                =====\n|                --|--\n|                  |  \n|                 / \ \n|                   \n|                   \n|                  \n|                   \n|                   \n|                   ')
        print("8/8 Life Savers Used!")

def ask_letter():
    while True:
        letter = input('Enter a letter: ')
        if letter.isalpha():
            return letter.upper()
        else:
            print('That is invalid.')
            print()

def replace_dash(gtext, dash_sequence,letter):
    letter = letter.upper()
    gtext = gtext.upper()
    if letter in gtext:
        for i in range(len(gtext)):
            if gtext[i] == letter:
                dash_sequence[i] = gtext[i]

        return dash_sequence
    else:
        return []

def get_level():
    while True:
        lvl = input('Which level would you like to play (1/2/3)? ')
        if lvl == '1' or lvl== '2' or lvl == '3':
            return int(lvl)
        else:
            print('That is invalid.\n')

def main_stuff(text, dashes):
    wrong_check = []
    while True:
        clear_output()
        print(''.join(dashes))
        print()
        letter = ask_letter()
        new_dashes = replace_dash(text, dashes, letter)
        if not new_dashes:
            wrong_guess(wrong_check)
            wrong_check.append('WRONG!!!!! IN YO FACE!!')
        else:
            dashes = new_dashes

        if len(wrong_check) == 8:
            print('\n\nGAME OVER!! You Lose!')
            print(f'Original Text: {text}')
            print()
            break
        elif ''.join(dashes) == text.upper():
            print('\n\nGAME OVER!! You Win!')
            print(text.upper())
            print()
            break

def repeat():
    while True:
        choice = input('Would you like to play another round of Hangman (y/n)?')
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('That is invalid \n')

def main():
    print('\nWelcome to Hangman!')

    while True:
        print()
        print('To play Hangman, help Bob and guess all of the letters in the text before he swings!')

        input('Hit enter to begin the game. ')
        print('\n\nLevel 1: Easy Peasy Lemon Squeezy ..... 3-10 letters\nLevel 2: Using Your Brains ..... 11+ letters\nLevel 3: Rage Quit ..... 1+ words\n')
        print()
        print()
        level = get_level()

        text = get_guess_text(level)
        dashes = make_dashes(text)
        main_stuff(text, dashes)

        choice = repeat()
        if choice:
            clear_output(wait=False)
        else:
            print()
            print('Thanks for playing!')
            break


# MAIN

main()
