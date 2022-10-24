import smtplib
import string

# GLOBALS
ALPHABET = list(string.ascii_letters) + list(string.digits) + ['!', '.', ',', "'", '"', '(', ')', ' ', ';', '?', '-',
                                                               '=']
# Dict of alphabet to number (starting at 0)
ALPHA_NUMS = {}

n = 0
for item in ALPHABET:
    ALPHA_NUMS[item] = n
    n += 1


NUMS_ALPHA = {}

n = 0
for item in ALPHABET:
    NUMS_ALPHA[n] = item
    n += 1

NUMS_ALPHA2 = {}

n = 0
for item in ALPHABET:
    NUMS_ALPHA2[n] = item
    n += 1


# FUNCTIONS
def make_new_alpha(shift):
    s = int(shift)
    i = 0
    for item in ALPHABET:
        if s >= len(ALPHABET):
            s = 0
        NUMS_ALPHA[i] = ALPHABET[s]
        i+= 1
        s+= 1

    return NUMS_ALPHA

def encrypt_text(plain_text,shift):

    NUMS_ALPHA = make_new_alpha(shift)

    encrypted_list = []

    for letter in plain_text:
        a_n = ALPHA_NUMS[letter]
        encrypted_letter = NUMS_ALPHA[a_n]
        encrypted_list.append(encrypted_letter)
        encrypted_txt = ''.join(encrypted_list)

    return encrypted_txt


def decrypt_text(c_text, shift):

    NUMS_ALPHA = make_new_alpha(shift)

    # Reverses keys and values in NUMS_ALPHA and puts the reversed stuff in a new dict
    rev_nums_alpha = {v: k for k, v in NUMS_ALPHA.items()}

    decrypted_list = []
    for letter in c_text:
        r_n_a = rev_nums_alpha[letter]
        decrypted_letter = NUMS_ALPHA2[r_n_a]
        decrypted_list.append(decrypted_letter)
        decrypted_txt = ''.join(decrypted_list)

    return decrypted_txt

def send_email(new_text, shift):

    try_counter = 0

    while True:
        try:
            try_counter += 1
            print('NOTE: Can only send emails with the Gmail provider. You will need and App Password to do so.')
            print()

            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

            smtp_object.ehlo()

            smtp_object.starttls()
            email_address = input('Enter the email you wish to log into: ')
            print(email_address)
            password = input('Enter the password: ')

            smtp_object.login(email_address, password)
        except:
            print("Looks like there's something wrong with your email and/or password.")
            print('Make sure your password is an App Password, and the email is spelled correctly.')
            if try_counter == 1:
                print()
                print('Email login was not successful!')
                print()
                break
        else:
            print()
            print('Email login successful!')
            print()
            return

    while True:
        try:
            from_address = email_address
            to_address = input("Enter the email of your recipient: ")
            while True:
                subject = input('Enter the subject: ')
                choice = input('Would you like to send the encrypted/decrypted text you have received along with the shift (y/n) ? ')
                if choice == 'y':
                    choice2 = input('Would you like to send the encrypted/decrypted text and the shift along with an unencrypted message (y/n) ? ')
                    if choice2 == 'y':
                        message = input('Enter the message you would like to attach: ')
                        msg = 'Subject: ' + subject + '\n\n' + message + '\n' + new_text + '\n' + 'Shift: '+ shift
                        print()
                        print('Here is the message: \n')
                        print()
                        print(msg)
                        print()
                        choice3 = input('Send message (y/n) ? ')
                        if choice3 == 'y':
                            smtp_object.sendmail(from_address,to_address,msg)
                            break
                        elif choice3 == 'n':
                            continue
                    elif choice2 == 'n':
                        msg = 'Subject: ' + subject + '\n\n' + new_text + '\n' + 'Shift: '+ shift
                        print()
                        print('Here is the message: ')
                        print()
                        print(msg)
                        print()
                        choice3 = input('Send message (y/n) ? ')
                        if choice3 == 'y':
                            smtp_object.sendmail(from_address, to_address, msg)
                            break
                        elif choice3 == 'n':
                            continue
                elif choice == 'n':
                    choice2 = input('Would you like to send the encrypted/decrypted text along with an unencrypted message (y/n) ? ')
                    if choice2 == 'y':
                        message = input('Enter the message you would like to attach: ')
                        msg = 'Subject: ' + subject + '\n\n' + message + '\n' + new_text
                        print()
                        print('Here is the message: \n\n')
                        print(msg)
                        print()
                        choice3 = input('Send message (y/n) ? ')
                        if choice3 == 'y':
                            smtp_object.sendmail(from_address, to_address, msg)
                            break
                        elif choice3 == 'n':
                            continue
                    elif choice2 == 'n':
                        msg = msg = 'Subject: ' + subject + '\n\n' + new_text
                        print()
                        print('Here is the message:')
                        print()
                        print(msg)
                        print()
                        choice3 = input('Send message (y/n) ? ')
                        if choice3 == 'y':
                            smtp_object.sendmail(from_address, to_address, msg)
                            break
                        elif choice3 == 'n':
                            continue
        except:
            print("Looks like there's something wrong. Please make sure everything is spelled correctly.")
        else:
            break

    smtp_object.quit()

def repeat():
    while True:

        print()
        print()
        choice5 = input("Would you like to encrypt or decrypt more text (y/n) ? ")
        if choice5 == 'y':
            return True
        elif choice5 == 'n':
            return False
        else:
            print('That is invalid.')


# MAIN
print()
print()
print("Welcome to Caesar's Ciphers!----------------------------------------------------------------------------------------------")

while True:

    NUMS_ALPHA = {}

    n = 0
    for item in ALPHABET:
        NUMS_ALPHA[n] = item
        n += 1

    print('Here, you can encrypt and decrypt text using an online Caesar Cipher!')
    print()

    while True:
        choice4 = input("Would you like to encrypt or decrypt text (encrypt(e)/decrypt(d)) ? ")
        if choice4 == 'e':
            print()
            text = input('Enter in the text you would like to encrypt: ')
            shift = input('Enter the shift you would like to impose (number ONLY): ')
            encrypted_text = encrypt_text(text,shift)
            print()
            print(f"Here is your encrypted text: {encrypted_text}")

            while True:
                email = input('Would you like to send an email with the encryption (y/n) ? ')
                print()
                if email == 'y':
                    send_email(encrypted_text,shift)
                    break
                elif email == 'n':
                    break
                else:
                    print()
                    print('That is invalid.')
                    print()
            break
        elif choice4 == 'd':
            print()
            text = input('Enter in the text you would like to decrypt: ')
            shift = input('Enter the shift (number ONLY): ')
            print()
            decrypted_text = decrypt_text(text, shift)
            print(f"Here is your decrypted text: {decrypted_text}")

            while True:
                print()
                email = input('Would you like to send an email with the decryption (y/n) ? ')
                print()
                if email == 'y':
                    send_email(decrypted_text,shift)
                    break
                elif email == 'n':
                    break
                else:
                    print()
                    print('That is invalid.')
                    print()
            break
        else:
            print()
            print('That is invalid.')
            print()

    choice6 = repeat()

    if choice6:
        continue
    else:
        print()
        print("Thank you for using Caesar's Ciphers!")
        break
