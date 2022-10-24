# GLOBALS
VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


# FUNCTIONS
def vowel_ending():
    while True:
        ending = input('Choose what ending you would like for words that begin with vowels (-hay(h)/-yay(y)/-way(w) : ')
        if ending.lower() == 'h' or ending.lower() == '-hay' or ending.lower() == 'hay':
            ending = 'hay'
            return ending
        elif ending.lower() == 'y' or ending.lower() == '-yay' or ending.lower() == 'yay':
            ending = 'yay'
            return ending
        elif ending.lower() == 'w' or ending.lower() == '-way' or ending.lower() == 'way':
            ending = 'way'
            return ending
        else:
            print('Please enter a valid ending.')

def consonant_pl(word):
    pl_word = word[1:] + word[0] + 'ay'
    return pl_word

def double_consonant_pl(word):
    pl_word = word[2:] + word[0:2] + 'ay'
    return pl_word

def vowel_pl(word):
    pl_word = word + ending
    return pl_word

def make_pl(text):

    text = text.lower()

    words = text.split()

    for word in words:
        if word[-1] == ',' or word[-1] == ';' or word[-1] == '.':
            if word[0] in VOWELS:
                punc = word[-1]
                word = word[:-1]
                new_word = vowel_pl(word)
                new_word = new_word + punc
                pl_list.append(new_word)
            elif word[0] in CONSONANTS and word[1] in CONSONANTS:
                punc = word[-1]
                word = word[:-1]
                new_word = double_consonant_pl(word)
                new_word = new_word + punc
                pl_list.append(new_word)
            elif word[0] in CONSONANTS:
                punc = word[-1]
                word = word[:-1]
                new_word = consonant_pl(word)
                new_word = new_word + punc
                pl_list.append(new_word)
        elif word[0] in VOWELS:
            new_word = vowel_pl(word)
            pl_list.append(new_word)
        elif word[0] in CONSONANTS and word[1] in CONSONANTS:
            new_word = double_consonant_pl(word)
            pl_list.append(new_word)
        elif word[0] in CONSONANTS:
            new_word = consonant_pl(word)
            pl_list.append(new_word)

    pig_latin_string = ' '.join(pl_list)
    return pig_latin_string

def repeat():
    while True:

        choice = input('Would you like to convert more text (y/n) ? ')

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Sorry, that is invalid. ")
# MAIN
print()
print('Welcome to the Pig Latin Converter!----------------------------------------------------------------------------------------------------')
print()
print('Here you can enter in some text and receive a pig latin version of it!')

while True:

    pl_list = []

    print('REMINDER: This is a simple Pig Latin Converter. It will not recognize compound words or identify whether a y is acting as a vowel or not. Please take care.')
    print('REMINDER: The converter will not adjust for hyphens, parentheses, or special characters. You may type in commas, semicolons, periods and punctuaction at the end of the text.')
    print()
    input('Hit enter to convert your first lines! ')
    print()
    print()
    ending = vowel_ending()
    print()
    text = input('Enter the text you wish to convert: ')

    pig_latin_text = make_pl(text)

    print()
    print(f'Here is your converted text: {pig_latin_text}')
    print()
    print()
    choice = repeat()

    if choice:
        print()
        continue
    else:
        print()
        print('Thank you for using Pig Latin Converter!')
        break
