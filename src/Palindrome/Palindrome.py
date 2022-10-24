import re

# Functions

def check_palindrome(text):

    pattern = r'[\w]'
    text2 = re.findall(pattern, text)
    text3 = ''.join(text2)
    text4 = text3.lower()
    text5 = text4[::-1]

    if text4 == text5:
        return True
    else:
        return False

def repeat():

    flag = True
    while flag:

        print()
        do_again = input('Would you like to check more text (y/n) ?: ')

        if do_again == 'y':
            flag = False
        elif do_again == 'n':
            print('Thank you for using Palindrome Words!')
            flag = False
        else:
            print('Sorry, please enter y or n.')
            print()

    return do_again

# Main

print('Welcome to ---Palindrome Words---')
print('Here you can check if a word, phrase, or number is a palindrome. Check it out!')

while True:
    print()
    text = input('Enter a word, phrase, or number: ')

    pal_check = check_palindrome(text)

    if pal_check == True:
        print('Your text is a palindrome!')
    else:
        print('Your text is not a palindrome.')

    do_again = repeat()

    if do_again == 'y':
        continue
    elif do_again =='n':
        break