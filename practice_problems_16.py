"""
For exam 3, assume each of these problems has a base difficulty of "$"
"""
import sys,time
def size_decorator():
    """
    When applied to a definition, this decorator should print the size (using sys.getsizeof) of the return value
    $ Instead of printing write the return value to a file called 'size_decorator.txt'
        $ Ensure multiple calls to size_decorator will be captured in the same file, each on a new line
    $ Also log the type() of the return value and current time
    """
    def internal(*args, **kwargs):
        print('LOG: args={}, kwargs={}'.format(args, kwargs))
        result = sys.getsizeof(*args, **kwargs)
        with open('size_decorator.txt','a') as outfile:
            outfile.write(str(result)+"\n")
        

    return internal

x = size_decorator()
x('decorators.py')


def time_decorator():
    """
    This decorator should print the real world time taken to run the definition
    $ print the process time as well
    $ Instead of printing write the return value to a file called 'time_decorator.txt'
        $ Ensure multiple calls to size_decorator will be captured in the same file, each on a new line
    """
    def internal(*args,**kwargs):
        result = time.time()
        with open('time_decorator.txt','a') as outfile:
            outfile.write(str(result)+"\n")

    return internal

x = time_decorator()
x()

import pickle
import os
def pickle_decorator(my_def):
    """
    When applied to a definition, this decorator should save a pickle file of the return object.
    $ The name for the pickle file should be "{}_{}.pickle".format(my_def.__name__, args)
    $$ This definition should check if the pickle file exists before writing, if it does,
        load the pickle and return the object without of running the definition.
    """
    def internal(*args,**kwargs):
        if os.path.isfile("{}_{}.pickle".format(my_def.__name__, args)):
            return pickle.load(open("{}_{}.pickle".format(my_def.__name__, args),"rb"))
        else:
            pickle.dump(args,open("{}_{}.pickle".format(my_def.__name__, args),"wb"))
    
    return internal

def hello():
    return 'hello'

x = pickle_decorator(hello)
print(x('Krishna','SDSU'))

def super_decorator_challenge():
    """
    When applied to a definition, this decorator should perform the same tasks as all 3 previous decorators
    $$$ Do this without copy/paste-ing the previous lines into this def, instead, call the other three decorator functions
         from within this decorator.  hint: see the section "## Without the shortcut @decorator syntax"
    """





def small_def(x):
    return x+2

def big_def(x):
    return [[0 for _ in range(x)] for _ in range(x)]
