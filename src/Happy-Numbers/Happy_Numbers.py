import yaml
import re

# GLOBALS
TEST = False      # True for testing, False for input prompts
CONF = yaml.safe_load(open('Happy_Numbers.yml'))

# FUNCTIONS
def square_and_add_nums(num):
    num_list = list(str(num))
    sqr_num_list = []
    for item in num_list:
        sqr_num_list.append(int(item)**2)
    sqr_added_num = sum(sqr_num_list)
    return sqr_added_num

def check_happy(num):
    # FALSE = NOT Happy Num
    # TRUE = Happy Num

    if num == 1:
        return True

    nums_list = []
    while True:
        num = square_and_add_nums(num)
        if num ==1:
            return True
        if num in nums_list:
            return False
        nums_list.append(num)

def make_nums_only(list):
    nums_only_list = []
    for item in list:
        try:
            int(item)
        except:
            pass
        else:
            nums_only_list.append(int(item))
    return nums_only_list

def input_range():
    if TEST == True:
        return CONF['check_happy_range']  # Change according to what you want!
    while True:
        try:
            range = input('Enter the range you would like check for happy numbers (N1 N2) (NOTE: N1 should be less than N2): ')
            split_range = range.split()
            if re.search(r'\d{1,3} \d{1,3}', range):
                break
            elif int(split_range[0]) >= int(split_range[1]):
                print('The first number must be less than the second number.')
                continue
            else:
                print('Please enter two numbers separated by a space.')
        except:
            print('Enter two numbers separated by a space.')
    return range

def make_range(range):
    split_range = range.split()
    nums_only_list = make_nums_only(split_range)
    return nums_only_list

def print_happy_nums(list):
    print(f'Found {len(list)} Happy Number(s)!')
    for num in list:
        print(num)

def range_check_happy(range_nums_list):   # gets the range_nums_list from the range() function
    happy_nums = []
    for n in range(range_nums_list[0], range_nums_list[1]+1):
        maybe_happy_num = check_happy(n)
        if maybe_happy_num:
            happy_nums.append(n)
    print_happy_nums(happy_nums)
    

def input_up_to_num():
    if TEST == True:
        return CONF['check_happy_from_1']  # Change according to what you want!
    while True:
        number = input('Enter a number (NOTE: Will check for Happy Numbers from 2 to this number): ')
        try:
            int_number = int(number)
        except:
            print('Enter one number and nothing else.')
        else:
            break
    return number

def up_to_num_check_happy(number):
    happy_nums = []
    for n in range(2,int(number)+1):
        if check_happy(n):
            happy_nums.append(n)
    print_happy_nums(happy_nums)

def repeat():
    if TEST == True:
        return CONF['no_repeat']
    while True:
        print()
        choice = input('Would you like to check for more Happy Numbers (y/n) ? ')
        if choice == 'y':
            return True
        elif choice =='n':
            return False
        else:
            print("Please enter 'y' or 'n'.")
            print()

def main_stuff():
    while True:
        choice = input('Would you like to enter a range and check for Happy Numbers within the range, or enter a number where it will check from 2 up to that number (r/n)? ')
        if choice == 'r':
            range = input_range()
            nums_only_list = make_range(range)
            range_check_happy(nums_only_list)
            break
        elif choice == 'n':
            number = input_up_to_num()
            up_to_num_check_happy(number)
            break
        else:
            print("Please enter 'r' or 'n'.")
            print()
# MAIN

while True:
    print()
    print('Welcome to the Happy Number Check!')
    print('Here, you can check for Happy Numbers!')
    print()
    main_stuff()

    choice = repeat()
    if choice:
        continue
    else:
        print()
        print('Thanks for using Happy Number Check!')
        break
