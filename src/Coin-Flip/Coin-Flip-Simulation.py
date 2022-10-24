import random  # To chose whether heads or tails
# import PIL import Image        # to show the heads/tails image
# from IPython.display import clear_output  # to clear the screen of previous flips


# # Coin Images
# both_sides = Image.open('/home/bkallich/Downloads/Dime_Both_Sides.png')
# W, H = both_sides.size
#
# ## Heads
# heads = both_sides.crop((0,0,W/2,H))
#
# h_width, h_height = heads.size
#
# new_Hheight = int(h_height/3)
# new_Hwidth = int(h_width/3)
#
# head = heads.resize((new_Hheight,new_Hwidth))
#
# ## Tails
# tails = both_sides.crop((W/2,0,W,H))
#
# t_width, t_height = tails.size
#
# new_Theight = int(t_height/3)
# new_Twidth = int(t_width/3)
#
# tail = tails.resize((new_Theight,new_Twidth))

# FUNCTIONS
def welcome():
    print('Welcome to Coin Crazy!')
    print('Here, you can flip a coin as many times as you wish!')

def display_heads():
    print()
    print('HEADS!!!')
    print()

def display_tails():
    print()
    print('TAILS!!!')
    print()

def flipping():
    choice = random.randint(1, 2)
    return choice

def repeat():
    flag = True
    while flag:

        print()
        do_again = input('Would you like to flip again (y/n) ?: ')

        if do_again == 'y':
            flag = False
        elif do_again == 'n':
            print('Thank you for using Coin Crazy!')
            flag = False
        else:
            print('Sorry, please enter y or n.')
            print()

    return do_again


# MAIN


welcome()

while True:

    print()
    input("Type something and hit enter to begin! ")

    print()
    print()
    print('Flipping coin.....')
    print('.')
    print('.')
    print('.')
    print()
    print()

    choice = flipping()

    if choice == 1:
        display_heads()
    else:
        display_tails()

    do_again = repeat()

    if do_again == 'y':
        continue
    elif do_again == 'n':
        break
