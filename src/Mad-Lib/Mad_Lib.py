import random
import os
import re
# import yaml
from typing import List

#BASE_DIR = '/home/user/Documents/Mad-Libs'
BASE_DIR = os.getcwd() + "/data"
if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

ML_FILES = ['Mad_Lib1.txt', 'Mad_Lib2.txt', 'Mad_Lib3.txt']

CONVERT_BLANKS = {'_____(noun)': 'Enter a noun: ',
                  '_____(adjective)': 'Enter an adjective: ',
                  '_____(name)': 'Enter a name: ',
                  '_____(cap adjective)': 'Enter an adjective: ',
                  '_____(proper noun)': 'Enter a proper noun: ',
                  '_____(plural noun)': 'Enter a plural noun: ',
                  '_____(number)': 'Enter a number: ',
                  '_____(ing verb)': "Enter a verb which ends with '-ing': ",
                  '_____(last name)': 'Enter a last name: ',
                  '_____(s verb)': "Enter a verb which ends with '-s': ",
                  '_____(exclamation)': 'Enter an exclamation: ',
                  '_____(thing)': 'Enter a thing: ',
                  '_____(emotion)': 'Enter an emotion: ',
                  '_____(adverb)': 'Enter an adverb: ',
                  '_____(past tense verb)': 'Enter a verb in the past tense: ',
                  '_____(verb)': 'Enter a verb: '}


def choose_template():
    file = random.choice(ML_FILES)
    return file

def get_blanks(file):
    with open(f'{BASE_DIR}/{file}', 'r') as f:
        mad_lib_temp = f.read()
        pattern = r'_____\([\w ]{1,30}\)'
        mylist = re.findall(pattern, mad_lib_temp)
    return mylist

def ask_for_words(file, mylist):
    with open(f'{BASE_DIR}/{file}', 'r') as f:
        text = f.read()
    for item in mylist:
        word = input(CONVERT_BLANKS[item])
        if '_____(cap adjective)' == item:
            word = word.capitalize()
        text = text.replace(item, word, 1)
    return text

def print_text(text):
    split_text = text.split()

    n = 15
    while n < 230:
        split_text.insert(n, '\n')
        n+= 15
    printable_text = ' '.join(split_text)
    print(printable_text)

def repeat():
    while True:
        choice = input('Would you like to fill out another Mad Lib (y/n)? ')
        if choice.lower() in ['y', 'yes']:
            return True
        elif choice.lower() in ['n', 'no']:
            return False
        else:
            print('That is not valid.')
            print()

def print_template(file):
    with open(f'{BASE_DIR}/{file}', 'r') as f:
        text = f.read()
        print_text(text)


# MAIN

print()
print('Welcome to EZ Mad Libs!')

while True:
    print('\n\n')
    print("Here you can enter some words and a Mad Lib template will automatically be filled out with the words!")
    print()
    input('Hit enter to begin!! ')
    print()
    file = choose_template()
    print(file)
    blanks_list = get_blanks(file)
    text = ask_for_words(file, blanks_list)
    print()
    print(f'Original Template: \n\n')
    print_template(file)
    print(f'Filled in Mad Lib: \n\n')
    print_text(text)
    print()

    choice = repeat()

    if choice:
        continue
    else:
        print()
        print('Thank you for using EZ Mad Libs!')
        break

