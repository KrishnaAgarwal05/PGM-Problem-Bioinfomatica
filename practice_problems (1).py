"""
These problems are representative of questions that will be on exam 1.

YOU WILL NOT HAVE INTERNET ACCESS OR REFERENCE MATERIALS FOR THE EXAM! This means,
if you find yourself using the lecture notes or stack overflow when solving these problems,
you are not prepared for the exam. Remember, it is not enough to 'understand' the solution,
you must also be able to produce it without aid.

FAQ:

Q: Will you accept _____ as correct output? or do you prefer _______?
A: These are ungraded questions, the important skill is being capable of doing both solutions.

Q: I solved these problems, do you have any more?
A: There is much to be gained from solving these questions multiple times. But yes, there will be more practice problems with the next lecture.

Q: Are you planning on posting any solutions?
A: No, but you are free to get feedback on your code during class time from myself or your peers.

Q: My solution is 'similar' to one commonly found online...
A: Ok

"""

##def print_even(my_list):
##    """
##    Given a list of integers, print only the even numbers
##    """
##    for x in my_list:
##        if (x%2==0):
##            print(x)
##    return

# # Test case
##print_even([1, 2, 3, 4, 6, 9])


def square(my_object):
    """
    Use assert or try/except to check if the input can be squared
    """
    try:
        if(type(my_object)):
           return my_object**2 
    except:
        print("Can't be squared")
    

# # Test cases
#square(3)
#square('hello')


##def madlib(adjective_1, adjective_2, adjective_3, noun_1):
##    """
##    This definition should take in 4 strings, format them into the string below, and print the final string.
##    The (adjective_1) man entered the (adjective_2) building to visit a very (adjective_3) man. "Sit down, Mr. Smith, can I interest you in any good (noun_1)?
##    """
##    print('The {0} man entered the {1} building to visit a very {2} man. "Sit down, Mr. Smith, can I interest you in any good {3}?'.format(adjective_1, adjective_2, adjective_3, noun_1))
##    return
##
### # Test case
##print(madlib('tall', 'nice', 'tall', 'cat food'))  # should print:  The tall man entered the nice building to visit a very tall man. "Sit down, Mr. Smith, can I interest you in any good cat food?


##def stop_at_x(my_list, x):
##    """
##    This definition should sequentially print every item in my_list until the item x is reached
##    """
##    for i in my_list:
##        if (i==x):
##            break
##        print(i)
##    return
##
### # Test cases
##stop_at_x([1, 2, 3, 9, 1, 2, 3], 9)  # should print 1, and then 2, then 3, then stop before 9 is printed


