import datetime
from datetime import date
import os
import random
import string
import yaml


# GLOBAL
TEST = False      # True for testing, False for input prompts
CONF = yaml.safe_load(open('Journal.yml'))
#BASE_DIR = '/home/user/Documents/Journals'
BASE_DIR = os.getcwd()

ALPHABET = list(string.ascii_letters) + list(string.digits)


# FUNCTION
def ask_for_new_folder_name():
    """
    Asks the user to enter a name for a new foler they are creating
    """
    if TEST:
        return CONF['folder_name'] + str(random.randint(1,100))
    while True:
        new_folder_name = input("Enter what you wish the name of the new folder to be: ")
        if os.path.isdir(f'{BASE_DIR}/{new_folder_name}'):
            print('Seems like a folder with the name already exists. Please enter a new name.')
            print()
            continue
        return new_folder_name

def ask_for_new_file_name_infol(folder_name):
    """
    Asks the user to enter a name for a new file they are creating
    """
    if TEST:
        return CONF['file_name'] + str(random.randint(1,100))
    while True:
        new_file_name = input('Enter what you wish the name of the new file to be (e.g. journal-data-file-1.txt): ')
        if os.path.isfile(f'{BASE_DIR}/{folder_name}/{new_file_name}'):
            print('Seems like a file with that name already exists. Please enter a new name.')
            print()
            continue
        return new_file_name

def ask_for_new_file_name():
    """
    Asks the user to enter a name for a new file they are creating
    """
    if TEST:
        return CONF['file_name'] + str(random.randint(1,100))
    while True:
        new_file_name = input('Enter what you wish the name of the new file to be: ')
        if os.path.isfile(f'{BASE_DIR}/{new_file_name}'):
            print('Seems like a file with that name already exists. Please enter a new name.')
            print()
            continue
        return new_file_name

def make_password():
    pwd = random.choices(population=ALPHABET, k=7)
    password = ''.join(pwd)
    return password

def make_new_folder():
    """
    Creates a new folder
    """
    new_folder_name = ask_for_new_folder_name()
    os.mkdir(f'{BASE_DIR}/{new_folder_name}')
    password = make_password()
    print(f'Your password is: {password} .')
    print('Save your password in a safe place so that every time you open this folder, you can access it.')

    with open('Journal_Passwords.txt','a') as f:
        f.write(f'\n{new_folder_name}, {password}')

def make_new_file_infol(folder_name):
    """
    Creates a new file and writes nothing to it.
    """
    new_file_name = ask_for_new_file_name_infol(folder_name)
    with open(f'{BASE_DIR}/{folder_name}/{new_file_name}', 'w') as f:
        timestamp = get_timestuff()
        f.write(f'CREATED: {timestamp}\n')

def make_new_file():
    """
    Creates a new file and writes nothing to it.
    """
    new_file_name = ask_for_new_file_name_infol(BASE_DIR)
    with open(f'{BASE_DIR}/{new_file_name}', 'w') as f:
        timestamp = get_timestuff()
        f.write(f'CREATED: {timestamp}\n')

def enter_password(folder):
    while True:
        pwd = input('Enter the password: ')
        with open('Journal_Passwords.txt', 'r') as f:
            passwords = f.read()
        if f'{folder}, {pwd}' in passwords:
            break
        else:
            print('Seems like the password you entered is not valid. Please try again.')
            print()

def which_folder_to_open():
    """
    Asks the user which folder they want to open
    """
    if TEST:
        return CONF['folder_name']
    while True:
        folder_name = input('Enter the name of the folder you wish to open: ')
        if os.path.isdir(f'{BASE_DIR}/{folder_name}'):
            enter_password(folder_name)
            return folder_name
        else:
            print('Seems like the folder name you entered is not valid.')



def which_file_to_open_infol(folder_name):
    """
    Asks the user which file they want to open.
    This is for files that are within folders.
    """
    # if TEST:
    #     return CONF['file_name']
    while True:
        file_name = input('Enter the full name of the file you wish to open: ')
        print(f'File path: {BASE_DIR}/{folder_name}/{file_name}')
        if os.path.isfile(f'{BASE_DIR}/{folder_name}/{file_name}'):
            return file_name
        else:
            print('Seems like the file name you entered is not valid.')
            print()

def which_file_to_open():
    """
    Asks the user which file they want to open.
    This is for files that are not within folder.
    """
    # if TEST:
    #     return CONF['file_name']
    while True:
        file_name = input('Enter the full name of the file you wish to open: ')
        if os.path.isfile(f'{BASE_DIR}/{file_name}'):
            return file_name
        else:
            print('Seems like the file name you entered is not valid.')
            print()

def get_timestuff():
    """
    Gets the current date and time
    """
    now = datetime.datetime.now()
    today = date.today()
    date_text = today.strftime("%B %d, %Y")
    current_time = now.strftime("%H:%M:%S")
    timestamp = f'{date_text} - {current_time}'
    return timestamp

def make_journal_entry_infol():
    while True:
        folder_name = which_folder_to_open()
        file_name = which_file_to_open_infol(folder_name)
        entry = input("Enter the entry here (NOTE: For new lines, enter a backslash then 'n'): ")
        split_entry = entry.split('\\n')
        new_entry = '\n'.join(split_entry)
        print(f'Here is the entry:\n\n{new_entry}')
        print()
        choice = input('Add entry to journal (y/n)? ')
        if choice =='y':
            with open(f'{BASE_DIR}/{folder_name}/{file_name}','a') as f:
                timestamp = get_timestuff()
                entry_text = f'{timestamp}\n{new_entry}'
                f.write(f'\n\n\n{entry_text}')
            print('Entry logged.')
            break
        else:
            print()
            continue

def make_journal_entry():
    while True:
        file_name = which_file_to_open()
        entry = input("Enter the entry here (NOTE: For new lines, enter a backslash then 'n'): ")
        split_entry = entry.split('\\n')
        new_entry = '\n'.join(split_entry)
        print(f'Here is the entry:\n\n{new_entry}')
        print()
        choice = input('Add entry to journal (y/n)? ')
        if choice =='y':
            with open(f'{BASE_DIR}/{file_name}','a') as f:
                timestamp = get_timestuff()
                entry_text = f'{timestamp}\n{new_entry}'
                f.write(f'\n\n\n{entry_text}')
            print('Entry logged.')
            break
        else:
            print()
            continue

def main_make_new_file():
    while True:
        choice = input('Would you like to create a new file that is within a folder other than Journals (y/n)? ')
        if choice == 'y':
            folder_name = which_folder_to_open()
            make_new_file_infol(folder_name)
            print('New file created.')
            print()
            break
        elif choice =='n':
            make_new_file()
            print('new file created.')
            print()
            break
        else:
            print('Seems like that is not valid.')

def main_create_entry():
    while True:
        choice = input('Would you like to add an entry to a file which is within a folder other than Journals (y/n)? ')
        if choice == 'y':
            make_journal_entry_infol()
            break
        elif choice == 'n':
            make_journal_entry()
            break
        else:
            print('Seems like what you entered is not valid.')
            print()

def main_stuff():
    while True:
        choice = input('Would you like to create a folder, create a file, or write a journal entry (cfol/cfile/e): ')
        if choice == 'cfol':
            make_new_folder()
            break
        elif choice == 'cfile':
            main_make_new_file()
            break
        elif choice =='e':
            main_create_entry()
            break
        else:
            print('Seems like what you entered is not valid.')
            print()

def repeat():
    while True:
        choice = input('Would you like to use Journals 4 All again (y/n)? ')
        if choice == 'y':
            return True
        elif choice =='n':
            print()
            print('Thank you for using Journals 4 All!')
            return False
        else:
            print('Seems like what you entered is not valid.')

# MAIN

print('Welcome to Journals 4 All!')

while True:
    print()
    print('Here you can write in journals and save them right here on your computer!')

    main_stuff()
    choice = repeat()
    if choice:
        continue
    else:
        break
