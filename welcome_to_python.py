"""
Lecture 1

Welcome to Python

Kyle Levi
"""



## Declaring variables

 # Pointers?
##x = 10
##y = x
##x = 'hello'
##
##print(x)
##print(y)


# # but what about objects? Here we use lists (arrays)
##x = [1, 2, 3]
##y = x
##x.append(4)
##
##print(x)
##print(y)


# # commas in declarations
##x, y = False, True
##
##print(x)
##print(y)


# # multiple assignments
##x = y = None
##
##print(x)
##print(y)



## String formating

### this is the best way, use .format()
##x = True
##y = 'The value of x is: {}'.format(x)
##
##print(y)


### # python 3.6 supports fstrings, which are better... but you can't use this on your exam! and this will crash older versions of python
##x = False
##y = f'The value of x is: {x}'
##
##print(y)
#
#
# # the old-school and ugly way, you may see this, but don't write it
##x = 'Tuesday'
##y = 'The value of x is: %s'%(x)
##
##print(y)



# # Functions are objects and can be assigned!
def triple(i):
    return i*3
##
##x = triple
##
##print(triple(10))
##print(x(10))


# # Don't overwrite built in functions! Python will let you
##x = y = 10.09
##
##x = int(x)
##print(x)
##
##int = triple
##y = int(y)
##print(y)



## Conditional Statements: IF, ASSERT

## #if, elif, else
##x = 10
##
##if x > 100:
##    print('x is large')
##elif x == 10 :
##    print('x is exactly 10')
##else:
##    print('x is small')


# # not everything needs a comparison (>, <, ==)
##x = None
##
##if x:
##    print('x is not None')
##else:
##    print('x is None')


# # DANGER! 0 == false! This could be a debugging nightmare if you don't know!
##x = 0
##if x:
##    print('x is not None')
##else:
##    print('x is None')


### # ASSERT is used mostly for testing
##x = 0
####assert x == 1, 'x is not 1'
##
##
### # this is similar to
##if x != 1:
##    raise AssertionError('x is not 1')

# try/except work similar to if/else statements
##x = 'yes'
##try:
##    x = int(x)
##except:
##    print('cannot convert to int')
##    exit(1)



## Loops: FOR, WHILE

# # use the range(10) function, instead of: i=0, i<10, i++
##for i in range(10):
##    print(i)


# # range(start, stop, step)
##for i in range(20, 30, 2):
##    print(i)


# # while loops
##i = 0
##while i < 10:
##    print(i)
##    i += 1  # not i++


# skip to the next iteration of a loop with CONTINUE
##for i in range(100):
##    if i%2 == 0:
##        continue
##    print(i)


# exit a loop entierly with BREAK
##for i in range(5):
##    for j in range(1000000000000000000000000000000000000):
##        if j > 3:
##            break
##        print(i,j)


# # looping over arrays is easy
##x = [1, 2, 3, 4, 5]
##for i in x:
##    print(i)


# # use enumerate to loop over an iterable and count each loop
##x = ['one', 'two', 'three', 'four']
##for i, word in enumerate(x):
##    print(i, word)


# # use zip() to loop over two iterables, it will always stop at the shorter of the two
##x = [2, 3, 4, 5, 6, 7, 8, 9]
##y = ['even', 'odd']
##
##for a, b in zip(x, y):
##    print(a, b)



## Definitions: we will discuss generators, *args, and **kwargs after exam 2
def dbl(x):
    return x*2
print(dbl(3))


# some defs are built in
# help()




