import os

# FUNCTIONS
def check_words(text):
    split_text = text.split()
    text_len = len(split_text)
    return text_len

def file_txt():

    while True:
        try:
            mypath = input('Enter the full path to your file here: ')
            with open(mypath, 'r') as f:
                text = f.read()
                text_len = check_words(text)
            return text_len
        except:
            print('Oops, looks like the path you entered is invalid.')
            continue

def summary(mydir):
    base_dir = mydir
    mydir_list = os.listdir(base_dir)
    mylist = []

    while True:
        try:
            for file in mydir_list:
                file_path = base_dir + f'/{file}'
                if file[-4:-1] == '.tx':
                    f = open(file_path)
                    text= f.read()
                    text_len = check_words(text)
                    mystring = f'{file}: {text_len}'
                    mylist.append(mystring)
                else:
                    pass
            break
        except:
            print('Oops, looks like the path you entered is invalid.')
            continue

    mylist.sort()
    for item in mylist:
        print(item)

def check_again():

    while True:

        print()
        again = input('Would you like to check more text (y/n) ? ')

        if again =='y':
            break
        elif again== 'n':
            print()
            print('Thank you for using TextLen!')
            return 'n'
        else:
            print("Please enter 'y' or 'n'.")

# MAIN

print()
print('Welcome to TextLen!')

while True:

    print()
    print('Here you can check the length of some text.')
    print('You can enter the text manually, connect a file with text and check that, or get a summary of the files in a folder.')
    print('If connecting a file or getting a summary, it is best for the file/files to be .txt file(s).')

    while True:
        print()
        choice = input('Would you like to manually enter text, enter a file with text, or recieve a summary of a folder (manually(m)/file(f)/summary(s)) ? ')

        if choice.lower() == 'manually' or choice.lower() == 'm':
            text = input('Enter the text here: ')
            text_len = check_words(text)
            print(f'The text contains {text_len} word(s).')
            break
        elif choice.lower() == 'file' or choice.lower() == 'f':
            text_len = file_txt()
            print(f'The text contains {text_len} word(s).')
            break
        elif choice.lower() == 'summary' or choice.lower() == 's':
            mydir = input('Enter the directory to the folder here: ')
            text_len = summary(mydir)

            break
        else:
            print("Please enter 'manually'/'m', 'file'/'m', or 'summary'/'s'.")

    choice = check_again()

    if choice == 'n':
        break
    else:
        continue
