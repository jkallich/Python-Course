from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
import shutil
import smtplib
import string

# GLOBALS
ALPHABET = list(string.ascii_letters) + list(string.digits) + ['!', '.', ',', "'", '"', '(', ')', ' ', ';', '?', '-', '=', ' ']

ALPHA2NUM = {}

#CIPHER_ROOT_DIR = "/home/user/Documents/Vernam_Cipher_Key_Folders"
CIPHER_ROOT_DIR = os.getcwd() + "/tmp"
if not os.path.exists(CIPHER_ROOT_DIR):
    os.mkdir(CIPHER_ROOT_DIR)

n = 0
for item in ALPHABET:
    ALPHA2NUM[item] = n
    n+= 1

NUM2ALPHA = {}

n = 0
for item in ALPHABET:
    NUM2ALPHA[n] = item
    n+= 1

# FUNCTIONS
def make_zip(key_folder):
    """
    Makes a .zip file that contains all of the key files
    """
    print('To send files, a .zip file will be created to attach to emails.')
    rootdir = f'{CIPHER_ROOT_DIR}/{key_folder}'
    output_filename = f'{CIPHER_ROOT_DIR}/{key_folder}'
    file_path = shutil.make_archive(base_name=output_filename, format='zip', root_dir=rootdir)

    print('.zip file created.')
    print(f'Zip File Path: {file_path}')
    return rootdir

def send_keys2(from_address,to_address, password, subject, body, filepath,filename):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filepath, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address, password)
    text = msg.as_string()
    s.sendmail(from_address, to_address, text)

    s.quit()
    attachment.close()

def send_keys(key_folder):
    """
    Emails generated keys to address of user's choice
    """

    while True:
        choice = input('Would you like to email your keys (y/n) (NOTE: Can only use the Gmail provider, which requires an App Password) ? ')
        if choice == 'y':
            print()
            from_address = input('Enter your email: ')
            password = input('Enter the password (NOTE: SHould be an App Password) : ')
            to_address = input("Enter the recipient's address: ")
            subject = input('Enter the subject of the email: ')

            while True:
                choice2 = input('Would you like to send an unencrypted message with the keys (y/n) (NOTE: There will be nothing but the attached file if you do not send a message) ? ')
                if choice2 == 'y':
                    body = input('Enter the message you would like to send: ')
                    break
                elif choice2 =='n':
                    body = ''
                    break
                else:
                    print('That is not valid.')
                    print()
            filename = f'{key_folder}.zip'
            filepath = f'{CIPHER_ROOT_DIR}/{filename}'
            mydir = make_zip(key_folder)
            send_keys2(from_address, to_address, password, subject, body, filepath, filename)

            break
        elif choice == 'n':
            break
        else:
            print('That is not valid.')
            print()


def generate_keys():
    """
    Generates as many keys as the user wants, puts each key in a text file,
    and stores them in a folder with a name of the user's choice.
    """

    print('NOTE: Key(s) will be generated and entered into files. Each keys will have its own text file and all the these files will be stored in a folder.')
    while True:
        folder_name = input('Enter the name of the folder the key(s) will be stored in: ')
        keys_dir = f'{CIPHER_ROOT_DIR}/{folder_name}'
        if os.path.isdir(keys_dir):
            print('Sorry, this folder already exists.')
        else:
            break
    while True:
        try:
            key_num = input('Enter how many keys you would like to generate: ')
            key_num_int = int(key_num)
        except:
            print('Please enter a number.')
        else:
            break
    while True:
        try:
            key_len = input('Enter the number of characters in each key: ')
            key_len_int = int(key_len)
        except:
            print('Please enter a number.')
        else:
            break

    k_num = 1

    os.mkdir(keys_dir)
    for key in range(1, key_num_int+1):
        key_list = []
        for number in range(1, key_len_int+1):
            num = random.randint(0, len(ALPHABET)-1)
            num = str(num)
            key_list.append(num)

        key_text = ' '.join(key_list)
        with open(f'{keys_dir}/key{k_num}.txt', 'w') as f:
            f.write(key_text)
        k_num+= 1
    print('Keys generated')

    send_keys(folder_name)
    return folder_name

def delete_file():
    while True:
        folder = input('If the file you are looking for is in a folder within Vernam_Cipher_Key_Folders, then enter the folder name here. Else, just hit enter: ')
        filename = input('Enter the name of the file you would like to delete (e.g. ./tmp/keys/key1.txt): ')
        base_dir = f'{CIPHER_ROOT_DIR}/Vernam_Cipher_Key_Folders'
        if folder == '':
            mydir = f'{base_dir}/{filename}'
            if os.path.isfile(mydir):
                os.remove(mydir)
                print('File successfully deleted')
                break
            else:
                print('File not found')
                print()
        else:
            mydir = f'{base_dir}/{folder}/{filename}'
            if os.path.isfile(mydir):
                os.remove(mydir)
                print('File successfully deleted')
                break
            else:
                print('File not found') 
                print()

def delete_folder():
    while True:
        fol_name = input('Enter name of the folder you would like to delete (NOTE: The folder and everything it contains will be deleted. The folder should be in Vernam_Cipher_Key_Folders.) : ')
        base_dir = CIPHER_ROOT_DIR
        path = f'{base_dir}/{fol_name}'
        if os.path.isdir(path):
            shutil.rmtree(path)
            print('Folder successfully deleted')
            break
        else:
            print('Folder not found')
            print()

def delete_keys():
    while True:
        choice4 = input('Would you like to delete a key, or a whole folder of keys (key/fol) : ')
        if choice4 == 'key' or choice4 =='k':
            delete_file()
            break
        elif choice4 =='fol' or choice4 == 'f':
            delete_folder()
            break
        else:
            print('That is not valid.')
            print()

def encrypt_text():
    keyfile = input('Enter the full name of the key file you would like to use to encrypt your plaintext (e.g. keys/key1.txt): ')
    extra_folder = input('If the key file is in the default foler (e.g. ./tmp/keys/key1.txt), then hit enter. Else enter the folder name here.')
    base_dir = CIPHER_ROOT_DIR
    if extra_folder == '':
        mydir = f'{base_dir}/{keyfile}'
        with open(mydir, 'r') as f:
            keytext = f.read()
            keylen = len(keytext.split())
            plaintext = input(f'Enter the text you would like to encrypt (NOTE: Can only be {keylen} character(s) long) : ')
            plaintext2nums = []
            for character in plaintext:
                num = ALPHA2NUM[character]
                plaintext2nums.append(num)
            keycroplen = len(plaintext2nums)
            keylist = keytext.split()
            key = keylist[:keycroplen]
            encrypted_numslist = []
            x = 0
            for thing in plaintext2nums:
                mysum = thing + int(key[x])
                encrypted_numslist.append(mysum)
                x+=1

            for num in encrypted_numslist:
                if num > len(ALPHABET):
                    num = num - len(ALPHABET)

            ciphertextlist = []
            for number in encrypted_numslist:
                letter = NUM2ALPHA[number]
                ciphertextlist.append(letter)
            cipher_text = ''.join(ciphertextlist)
    else:
        mydir = f'{base_dir}{extra_folder}/{keyfile}'
        with open(mydir, 'r') as f:
            keytext = f.read()
            keylen = len(keytext.split())
            plaintext = input(
                f'Enter the text you would like to encrypt (NOTE: Can only be {keylen} character(s) long) : ')
            plaintext2nums = []
            for character in plaintext:
                num = ALPHA2NUM[character]
                plaintext2nums.append(num)
            keycroplen = len(plaintext2nums)
            keylist = keytext.split()
            key = keylist[:keycroplen]

            encrypted_numslist = []
            x = 0
            for thing in plaintext2nums:
                mysum = thing + int(key[x])
                encrypted_numslist.append(mysum)
                x += 1

            for i in range(len(encrypted_numslist)):
                if encrypted_numslist[i] >= len(ALPHABET):
                    encrypted_numslist[i] -= len(ALPHABET)
            ciphertextlist = []
            for number in encrypted_numslist:
                letter = NUM2ALPHA[number]
                ciphertextlist.append(letter)
            cipher_text = ''.join(ciphertextlist)
    print(f'ENCRYPTED TEXT: {cipher_text}')
    return cipher_text

def decrypt_text():
    encrypted_text = input('Enter the encrypted text you would like to decrypt.')
    while True:
        keyfile = input('Enter the full name of the key file that contains the key that encrypted the code: ')
        keyfolder = input('If the file you are looking for is in a folder within Vernam_Cipher_Key_Folders, then enter the folder name here. Else, just hit enter: ')
        base_dir = CIPHER_ROOT_DIR
        if keyfolder == '':
            mydir = f'{base_dir}/{keyfile}'
            if os.path.isfile(mydir):
                break
            else:
                print('File name not valid.')
        else:
            mydir = f'{base_dir}/{keyfolder}/{keyfile}'
            if os.path.isfile(mydir):
                break
            else:
                print('File name or folder name not valid.')



    with open(mydir,'r') as f:
        keytext = f.read()

        keylist = keytext.split()

        encryptedtext_list = []
        for item in encrypted_text:
            encryptedtext_list.append(item)

        keycroplen = len(encryptedtext_list)
        key = keylist[:keycroplen]

        encryptedtext2nums_list = []
        for item in encryptedtext_list:
            new_num = ALPHA2NUM[item]
            encryptedtext2nums_list.append(new_num)

        n = 0
        encodedtextnums_list = []
        for number in encryptedtext2nums_list:
            difference = number - int(key[n])
            if difference < 0:
                new_number = number + len(ALPHABET)
                difference = new_number - int(key[n])
            encodedtextnums_list.append(difference)
            n+= 1

        decryptedtext_list = []
        for number in encodedtextnums_list:
            letter = NUM2ALPHA[number]
            decryptedtext_list.append(letter)

    decrypted_text = ''.join(decryptedtext_list)

    print(f'DECRYPTED TEXT: {decrypted_text}')
    return decrypted_text

def send_text(text):
    while True:
        yes_or_no = input('Would you like to send the encryption/decryption (NOTE: Can only send using the Gmail provider. You must have an App Password to do so.) (y/n)? ')
        if yes_or_no =='y':
            email = input('Enter your email address: ')
            to_address = input('Enter the recipient of the message: ')
            subject = input('Enter the subject of the email: ')
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = to_address
            msg['Subject'] = subject
            while True:
                choice2 = input('Would you like to include the key along with the encrypted/decrypted text (y/n) ? ')
                if choice2 == 'y':
                    basedir = CIPHER_ROOT_DIR
                    key_folder = input(
                        'If the key you want is in a folder in Vernam_Cipher_Key_Folders then enter the folder name here. Else, just hit enter: ')
                    if key_folder == '':
                        while True:
                            filename = input('Enter the full name of the key file you would like to attach: ')
                            if os.path.isfile(f'{basedir}/{filename}'):
                                mydir = f'{basedir}/{filename}'
                                break
                            else:
                                print('The file name is not valid.')
                        break
                    elif os.path.isdir(f'{basedir}/{key_folder}'):
                        filename = input('Enter the name of the key file you would like to attach: ')
                        if os.path.isfile(f'{basedir}/{key_folder}/{filename}'):
                            mydir = f'{basedir}/{key_folder}/{filename}'
                            break
                        else:
                            print('The file name is not valid.')
                        break
                    else:
                        print('The folder name is not valid.')
                elif choice2 == 'n':
                    break
                else:
                    print('That is not valid.')
                    print()

            while True:
                choice4 = input(
                    'Would you like to send an unencrypted message with the key (y/n) (NOTE: There will be nothing but the attached file and the key if you do not send a message) ? ')
                if choice4 == 'y':
                    body = input('Enter the message you would like to send: ')
                    body = f'{body}\n{text}'
                    msg.attach(MIMEText(body, 'plain'))
                    break
                elif choice4 == 'n':
                    body = ''
                    msg.attach(MIMEText(body, 'plain'))
                    break
                else:
                    print('That is not valid.')
                    print()

            attachment = open(mydir, "rb")

            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename= {filename}")
            msg.attach(p)

            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.starttls()

                password = input('Please enter your password (NOTE: Should be a Gmail App Password) : ')
                s.login(email, password)

                text = msg.as_string()
                s.sendmail(email, to_address, text)

            attachment.close()
            print()
            print('Email sent.')
            print()
            break
        elif yes_or_no == 'n':
            break
        else:
            print('That is not valid.')

def repeat():
    while True:
        choice = input("Would you like to use Vernam's Ciphers once more (y/n) ? ")
        if choice =='y':
            return True
        elif choice =='n':
            return False
        else:
            print('That is not valid.')
            print()


# MAIN

print("Welcome to Vernam's Ciphers!")

while True:

    print("Here, you can encrypt and decrypt text using a Vernam Cipher!")
    print('In order to use the Vernam Cipher, you must first have a key to encrypt or decrypt text. It is recommended to use a key only for one encryption and one decryption.')
    print("You can also create keys that will be saved as files on the computer and delete keys from the computer on Vernam's Ciphers.")
    print()
    while True:
        choice = input("Would you like to encrypt text, decrypt text, generate keys, or delete keys (e/dcrpt/g/del) ? ")
        if choice == 'e':
            encrypted_text = encrypt_text()
            print()
            send_text(encrypted_text)
            break
        elif choice == 'dcrpt':
            decrypted_text = decrypt_text()
            print()
            send_text(decrypted_text)
            print()
            break
        elif choice == 'g':
            generate_keys()
            print()
            break
        elif choice == 'del':
            delete_keys()
            print()
            break
        else:
            print("Whoops, seems like there's something wrong. Please enter 'e','dcrpt' , 'g', or 'del'.")
            print()

    choice2 = repeat()

    if choice2:
        continue
    else:
        print("Thanks for using Vernam's Ciphers!")
        break

