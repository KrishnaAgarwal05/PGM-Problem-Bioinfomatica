
### Practice questions for using slices
##def first_ten(my_list):
##    """
##    return a list of the first 10 elements in my_list
##    """
##    return my_list[:10]
##
##print(first_ten([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


##def last_ten(my_list):
##    """
##    return a list of the last 10 elements in my_list
##    """
##    return my_list[-10:]
##
##print(last_ten([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

##def every_second(my_list):
##    """
##    return a list of the every second element
##    """
##    return my_list[1::2]
##print(every_second([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

####
##def split_three_nine():
##    """
##    return numbers 3 through 9 from the provided list
##    """
##    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
##    return x[3:10]
##
##print(split_three_nine())
##
##
##def split_x_y(mylist, x, y):
##    """
##    return all elements between the occurrences of element x and element y in my_list
##    """
##    return mylist[x+1:y]
##
##print(split_x_y([0,1,2,3,4,5,6],2,6))

##
#### Practice questions for using dictionaries
##
##def count_letters(my_string):
##    """
##    return a dictionary where keys are letters in my_string, and values are the number of times that letter has occurred
##    """
##    new_str = {}
##    for x in my_string:
##        new_str[x] = new_str.get(x,0) + 1
##    return new_str
##
##print(count_letters("KRISHNAAGARWAL"))
##
##
##def add_words(my_list, my_dict):
##    """
##    add each object in my_list to my_dict, where the key is the object, and the value is the number of times that object has occurred
##    """
##    for x in my_list:
##        my_dict[x] = my_dict.get(x,0) +1
##    return my_dict
##
##print(add_words(['one','two','three','one'],{}))


##def remove_words(my_list, my_dict):
##    """
##    remove each key in my_list from my_dict and return the dictionary
##    """
##    for x in my_list:
##        if (x in my_dict):
##            my_dict.pop(x)
##    return my_dict
##
##print(remove_words(['one','two'],{'one': 2, 'two': 1, 'three': 1}))

##
##def print_true_keys(my_dict):
##    """
##    assume my_dict is of the form {'grapes': True, 'apples': False, ...}
##    print all keys whose value is True
##    """
##    for x in my_dict:
##        if my_dict[x]:
##            print(x)
##    return
##
##print_true_keys({'grapes': True, 'apples': False, 'mangoes': True})
##
##def safe_insert(key, value, my_dict):
##    """
##    check that the key is a string and the value is an int, then insert object x into my_dict
##    returns True if the element was inserted and False if it was not
##    """
##    if (type(key) is str and type(value) is int):
##        my_dict[key] = value
##        return True
##    else:
##        return False
##
##print(safe_insert('Krishna','123',{}))
##
##def dangerous_insert(x, i, my_list):
##    """
##    insert x into my_list at position i without doing any checks
##    can you cause this definition to thrown an error?
##    what happens when you try to insert at a position longer than the list?
##    """
##    my_list.insert(i,x)
##    return my_list
##
##print(dangerous_insert(4,5,['one','two']))

##
### Practice questions for Sets
def overlap(x, y):
    """
    Given two lists, x and y, return a new list of all elements that are in both lists
    """
    z = set(x).intersection(set(y))
    return z

print(overlap({1,2,3,4}, {3,4,5,6}))

####
##def only_x(x, y):
##    """
##    Given two lists, x and y, return a new list of all elements that are ONLY found in x
##    """
##    z = x - y
##    return z
##
##print(only_x({1,2,3,4}, {3,4,5,6}))


##def check_duplicate_insert(x, my_set):
##    """
##    Add the element x to my_set, if it is already present, print a warning to the user and return True,
##    if the element was not in the list return False
##    """
##    if x in my_set:
##        print("The Element is already present")
##        return True
##    else:
##        return False
##
##print(check_duplicate_insert('one',{'two','three'}))
#
