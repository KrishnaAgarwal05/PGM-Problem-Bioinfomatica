"""
Lecture 2

Data Structures

"""

## Lists

# lists hold objects, they grow and shrink intelligently
##x = [0, 1, 2, 3]
##x.append(4)
##
##print(x)


# the following example does exactly the same thing as the one above it
##x = [0, 1, 2, 3]
##x += [4]
##
##print(x)


# you can combine/concatenate two lists with addition  Note: lists can store different types of objects concurrently
##x = [1, 2, 3]
##y = ['red', 'blue', True]
##z = x + y
##
##print(z)


# you can accidentally erase your list with the following syntax - .APPEND() RETURNS NONE
##x = [0, 1, 2, 3]
##x = x.append(4)
##
##print(x)


# you can insert into lists with   .insert(position, object)
##x = ['tuesday', 'wednesday', 'thursday']
##x.insert(0, 'monday')
##
##print(x)


# you can remove items with .pop(position)  Note: this also returns the item removed, you don't need to store it
##x = ['zero', 'one', 'two']
##y = x.pop(2)
##
##print(x, y)


# you can also get the position of an item in a list, but keep in mind this is a O(n) operation (if the list is unordered)
##x = ['red', 'blue', 'green']
##y = x.index('green')
##
##print(y)



# VERY IMPORTANT! subsections of iterables (lists, strings, sets ...) can be sliced out, with slice indices. You will see this frequently
# the syntax is my_iterable[start : stop : step]
##x = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
##
##y = x[0]
##print(y)  # 'sunday'
##
##y = x[0:1]
##print(y)  # ['sunday']
##
##y = x[0:7:2]
##print(y)  # ['sunday', 'tuesday', 'thursday', 'saturday']


# you can also use negative numbers, these function the same, but start from the end of the array
##y = x[-1]
##print(y)  # ['saturday']

##y = x[-3:]  # start at -3 from end, and go to the end, taking the last 3 elements
##print(y)  # ['thursday', 'friday', 'saturday']

##y = x[::-1]  # traverse over the entire list, step backwards every time, thus reversing the array
##print(y)  # ['saturday', 'friday', 'thursday', 'wednesday', 'tuesday', 'monday', 'sunday']

# Loop over specific elements in a list
##x = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
##for y in x[1:6]:
##    print(y[:3])



## Dictionaries

# declare and access
##x = {'apple': 1, 'banana': 2, 'orange': 3}
##y = x['apple']
##
##print(y)


# add to dictionaries
##x = {'banana': 2, 'orange': 3}
##x['apple'] = 1
##
##print(x)


# remove from dictionaries
##x = {'apple': 1, 'banana': 2, 'orange': 3}
##del x['apple']
##
##print(x)


# what if our key doesn't exist?
##x = {'apple': 1, 'banana': 2, 'orange': 3}
##
## # y = x['beef']  # KeyError!
## # y = x.get('beef')  # returns None
##y = x.get('beef', 0)  # returns 0, this is the safest way to access a dictionary
##
##print(y)


# Here is the best way to increment a value used as a counter(one of the most common uses of a dictionary is counting something)
##my_string = "AAAABBBAAAAABAAAABAAAABBBBBAAABBBBCBBBAABAAAABBAAABABAB"
##x = {}
##for letter in my_string:
##    x[letter] = x.get(letter, 0) + 1  # This is a very important line! memorize it if you have to
##
##print(x)


### Looping over dictionaries
##x = {'red': True, 'blue': False, 'green': True, 'cyan': True}
####
#####loop over values in a dictionary
####for value in x.values():
####    print("A value in x is: {}".format(value))
##
##
###loop over keys in a dictionary
##for key in x.keys():
##    if x[key]:  # instead of comparing "if x[key] == True" we can simplify to "if x[key]" because all values are booleans
##        print("True key is: {}".format(key))
##
###loop over both keys and values in a dictionary with .items()
##for key, value in x.items():
##    print("Key is: {}.\tValue is: {}.".format(key, value))



## Sets
# sets are like dictionaries without keys
##x = {'red', 'blue', 'green', 'cyan'}
##x.add('purple')
##
##print(x)


# remove from set
##x = {'red', 'blue', 'green', 'cyan'}
##x.remove('cyan')
##
##print(x)


# NO DUPLICATES! this is a feature of sets
##x = {'red', 'blue', 'green', 'cyan'}
##x.add('red')
##
##print(x)


# looping over sets
##x = {'red', 'blue', 'green', 'cyan'}
##for color in x:
##    print('Color {} is in set "x"'.format(color))  # escape characters "\" aren't always required to print quotes



## Important time comparisons for list and set!  These will not be exam questions, but you will be expected to use each
## data structure where it is appropriate to do so. For example: don't do multiple lookups in large lists!

# we are just using this import to generate random numbers, you wont be tested on generating random elements
##import random
##def random_numbers(low, high, n):
##    """
##    Returns n random numbers between low and high
##    """
##    x = []
##    for i in range(n):
##        x.append(random.randint(low, high))
##    return x
##
##print(random_numbers(0,10,1000))

# here we generate our our two lists of random numbers
import time
##t0 = time.time()
##
##student_body = random_numbers(100000000, 999999999, 700000)
##my_class = random_numbers(100000000, 999999999, 100)
##
##t1 = time.time()
##print("Generating random numbers took {} seconds".format(t1-t0))


# now lets see how long it takes to check if every RedID in my_class is in student_body
##t0 = time.time()
##for student in my_class:
##    if student not in student_body:
##        pass # or print('oh no, student not found!')
##
##t1 = time.time()
##print("looking for students took {} seconds".format(t1-t0))


# Why not always use sets?
##import sys
##print(sys.getsizeof(student_body))
##print(sys.getsizeof(set(student_body)))


"""
    Reference Sheet
Lists:  ['apple', 'grape']
add - x.append(y)  # appends object y to list x
remove - x.pop(i)  # removes the element at position i
insert - x.insert(i, y)  # inserts object y into list x at position i (this does not overwrite the element at i)
slice - x[start : stop : step]  # evaluates to a list representing that sub list 
access - x[i]  # evaluates to the element at position i 

Dictionaries:  {'apple': 3, 'grape': 1}
add - x[key] = value  # adds the key/value pair to x
remove - del x[key]  # removes the key/value pair in x
access - x[key]  # evaluates to the value stored or throws error if the key is not found in x
access - x.get(key, default)  # returns the value stored or default if the key is not found in x
values - x.values()  # returns a list of values in x
keys - x.keys()  # returns a list of keys in x
keys and values - x.items()  # for looping over key/value pairs in a dictionary

Sets:  {'apple', 'grape'}
add - x.add(y)  # adds the object y to the set x
remove - x.remove(y)  # removes object y from set x

"""

