"""Data_Analysis.py
will do many thing with ten random numbers
JK
July 25, 2019"""

### Imports Section
import random
import math
import operator

### Constants Section
NUMBS_NEEDED = 10
LOWER = 11
UPPER = 50


### Functions Section
def get_numbers():
    temp_numbers_list = []
    for i in range(NUMBS_NEEDED):
        k = random.randint(LOWER, UPPER)
        temp_numbers_list.append(k)

    return temp_numbers_list


def get_smallest_numb(data):
    smallest_numb = data[0]
    for i in data:
        if smallest_numb > i:
            smallest_numb = i
    return smallest_numb


def get_biggest_numb(data):
    biggest_numb = data[0]
    for i in data:
        if biggest_numb < i:
            biggest_numb = i

    return biggest_numb


def get_average(data):
    sum_numbers = 0
    for i in data:
        sum_numbers = sum_numbers + i

    mean = sum_numbers / len(data)
    return mean


def get_median(data):
    data.sort()
    number_of_numbers = len(data)
    if number_of_numbers % 2 == 0:
        second_index = math.ceil(number_of_numbers/2)
        first_index = second_index-1
        numerator = data[first_index] + data[second_index]
        median = numerator / 2
    else:
        index = math.floor((number_of_numbers/2))
        median = data[index]

    return median


def get_mode(data):
    mode_list = []
    value_dict = {}
    # value_dict[2] = 6
    for i in data:
        k = i
        v = 1
        if k in value_dict:
            value_dict[k] = value_dict[k] + v
        else:
            value_dict[k] = v
    sorted_value = sorted(value_dict.items(), key = lambda kv: kv [1], reverse= True)

    (a,b) = sorted_value[0]

    for (p,q) in sorted_value:
        if q == b and q > 1:
            mode_list.append(p)
        #print(i)
    return mode_list


def prime_number_finder(data):
    prime_dict = {}
    for i in data:
        prime_dict[i] = is_prime(i)
    return prime_dict

def is_prime(k):
    flag = True
    for i in range(k-2):
        if k % (i + 2) == 0:
            flag = False
            break

    return flag




### Main Section
numbers_list = get_numbers()
smallest_numb_function = get_smallest_numb(numbers_list)
biggest_numb_function = get_biggest_numb(numbers_list)
average_function = get_average(numbers_list)
median_function = get_median(numbers_list)
mode_function = get_mode(numbers_list)
prime_stuff_funct = prime_number_finder(numbers_list)
print(numbers_list)
print("The smallest number: " + str(smallest_numb_function))
print("The biggest number: " + str(biggest_numb_function))
print("The average: " + str(average_function))
print("The median: " + str(median_function))
print("The mode: " + str(mode_function))
print("Is it a prime number?   " + str(prime_stuff_funct))

