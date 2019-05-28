"""
Practice Problems 14
Generators

Generator comprehension is great for simple tasks, but may lack the versatility of a full generator def (using yield)
Complete each of these problems using generator comprehension (if possible) AND using "yield"
Remember: range() is not a generator, you should not yield or return a range() object, but you can use range()
"""


##def even_only_range(start, stop):
##    """
##    Yield all even numbers in the range start to stop (including the start number, and not the stop number)
##    """
##    return (x for x in range(start,stop) if x%2==0)
##
##for x in even_only_range(5,15):
##    print(x)

    
##def every_other_odd(start, stop):
##    """
##    Yield every other odd number in the range specified
##    EX: (5, 15) -> 5, 9, 13
##    """
##    x = start
##    while x<stop:
##        if x%2!=0:
##            yield(x)
##            x+=2
##        x += 1
##
##for x in every_other_odd(5,15):
##    print(x)

##def specific_rows(filename, first_char):
##    """
##    Assume filename is an 'infinitely' large file, yield one line at a time if that line startswith 'first_char'
##    EX: ('example.fasta', '>') -> '>header1', '>header2', '>header3', ...
##    """
##    return (line.strip() for line in open(filename,'r') if line.startswith(first_char))
##
##for x in specific_rows('data/example.fasta', '>'):
##    print(x)


##def multiple_chars(my_list):
##    """
##    Given a list of strings, yield each sequential character 3 times
##    EX: (["A", "Hello") -> "A", "A", "A", "H", "H", "H", "e", "e", "e", ...
##    """
##    for x in my_list:
##        for y in x:
##            yield y
##            yield y
##            yield y
##    #return (y for x in ([y]*3 for x in my_list for y in x ) for y in x)
##            
##for x in multiple_chars(["A", "Hello"]):
##    print(x,end=",")

##def incremet_to_20(my_list):
##    """
##    Given a list of integers, yield each number, followed by all numbers up to 20, for every number in my_list
##    EX: ([17, 15, 5]) -> 17, 18, 19, 20, 15, 16, 17, 18, 19, 20, 5, 6, 7, ... 20
##    """
##    # this can be done with nested generator comprehension,
##    # but it will be much easier to use a generator function with yield.
##    # here is one example of generator comprehension
##    return (i for x in (range(n, 21) for n in my_list) for i in x)
##
##for i in incremet_to_20([17, 15, 5]):
##    print(i)


def smoothing_intervals(my_list):
    """
    Given a list of integers yield each number, followed by all numbers between itself and the next number
    EX: ([1, 7, 4]) -> 1, 2, 3, 4, 5, 6, 7, 6, 5, 4
    *Don't try to do this with generator comprehension, unless you want an exceptional challenge (it is possible, ~330 characters)
    """
    for i in range(len(my_list)-1):
        if int(my_list[i]<my_list[i+1]) and i==0:
            for x in range(int(my_list[i]),int(my_list[i+1]+1)):
                yield x
        elif int(my_list[i]>my_list[i+1]):
            for x in range(int(my_list[i]-1),int(my_list[i+1])-1,-1):
                yield x
        else:
            for x in range(int(my_list[i]+1),int(my_list[i+1]+1)):
                yield x
            
##    return (i for x in (range(int(my_list[i]),int(my_list[i+1]+1)) if int(my_list[i]<my_list[i+1]) else range(int(my_list[i])-1,int(my_list[i+1]),-1) for i in range(len(my_list)-1)) for i in x)
# Rules:
#   1. Only 1 line
#   2. No lists, sets, or dictionaries; you may not cast any generators to lists, that breaks the generator aspect
#   3. No imported modules, everything should be run without any import statements (especially no itertools.chain)

my_list = [1, 7, 4,10,7]
for x in smoothing_intervals(my_list):
    print(x)

##final = (j for k in (range(x[0], x[1], 1) if x[0] < x[1] and not idx == len(my_list)-2 else range(x[0], x[1], -1) if x[0] > x[1] and not idx == len(my_list)-2 else range(x[0], x[1]-1, -1) if x[0] > x[1] else range(x[0], x[1]+1, 1) for idx, x in enumerate(((my_list[i-1], my_list[i]) for i in range(1,len(my_list))))) for j in k)
##for i in final:
##    print(i)
