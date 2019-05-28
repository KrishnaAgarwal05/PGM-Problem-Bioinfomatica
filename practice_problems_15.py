"""
practice problems 14

"""
from functools import reduce

def new_docstring_format_example():
    """
    This line is the basic problem description
    $ doing this line makes the problem a bit harder
        $ this sub-item means that it is meant to be done in addition to the above line
    $$ this line suggests something that makes the problem noticably harder
    $$$ this is a difficult challenge
        $ this is a small add-on to the difficult challenge ($$$$ total)
        $$ this is a significant add-on to the difficult challenge ($$$$$ total)
    $$$$ I most likely wouldn't put this on the exam, but it never hurts to over prepare
    $$$$$ test yourself for mastery, I promise this will not be on exam
    """



def my_sum(*args):
    """
    return the sum of all args without using sum()
    $ be sure every argument is an int
    $$ only use a single line of generator comprehension
    $$$ use argparse to run this def from the command line. These two lines will help:
            parser.add_argument('my_args', help='', nargs=argparse.REMAINDER)
            https://docs.python.org/3/library/argparse.html#nargs
    """
    sum = 0
    for x in args:
        sum += x

    yield sum
    #return (lambda x,y : int(x)+int(y), args)

##print(my_sum(1,2,3))
##for x in my_sum(1,2,3):
##    print(x)

##def mult_args(my_number, *args):
##    """
##    return a list of all *args multiplied by my_number
##    EX: (2, 1, 5, 20) -> [2, 5, 20]
##    $ check that every input is an int
##    $ write this as a generator function that yields results instead of returning a list
##        $ do it using comprehension
##    $ allow a string as my_number, provided every *arg is an int or vice versa
##    """
##    for x in args:
##        yield int(my_number) * int(x)
##
##for x in mult_args('2', 1, 5, 20):
##    print(x)


def all_options(arg1,arg2,arg3,*args,**kwargs):
    """
    This definition should accept *args, **kwargs, and three additional arguments with one of them defaulting to 10
    $ it should return a list where each position in the list is one of the 5 inputs above (list should be length 5)
        $$ return a list where each arg gets its own element in the list
        $$ return a list where each kwarg value is its own element in the list
    """
    my_list = []
    my_list.append(arg1)
    my_list.append(arg2)
    my_list.append(arg3)
    my_list.append(list(args))
    my_list.append(list(kwargs))

    yield my_list

##for x in all_options('in1','in2','in3','in4','in5',in6=6,in7=7):
##    print(x)

# Use these next two lines to write a CSV file for testing
# with open('example.csv', 'w') as outfile:
#     outfile.write('fruit,flavor,convenience,durability\nbanana,5,5,2\napple,3,4,5\ngrapes,4,4,2\nlemon,1,3,4\norange,3,3,3\nwatermelon,4,1,5\ntomato,2,2,1')

def read_columns(filename, *args, **kwargs):
    """
    The goal of this definition is to read a CSV file and process each line before yielding. By accepting *args,
    this definition should be able to return only data from the column names specified. By using **kwargs, this
    definition will be able to handle a wider variety of cases. The following example will read 'example.csv',
    and one line at a time, starting with the header line, write a new file, 'new_example.csv'

    read_columns('example.csv', 'fruit', 'flavor', write_file='new_example.csv', yield_header=True)
                  filename       args     args     kwargs                        kwargs



    $ Detect whether or not the file uses tabs or commas and split the line accordingly

    $ If no *args are specified, return every column

        $ If 1 or more *Args are specified, yield only values from those columns in any order when yielding lines

            $$ Yield the list of values in the order they were provided to *args
                EX: ('example.csv', flavor, fruit) -> ['5', 'banana']

    $ To return only values from the correct columns, this def will need to know where the header line is and
      should not return any values from the header line - to do this you will need to find the header line.
      for the easy '$' case of this problem, assume the header line is always the first line.

        $$ For an increased challenge, assume the header line will not always be the first line, but that the user
           will specify how many lines to skip to read the header line. Add a key word argument 'skip_lines' which
           is set to an integer and skips that many lines from the top of the file.
           EX: skip_lines=5, should skip the first 5 lines in the file

        $$$ Given that *args has been provided, search for the first line that contains every arg - use this as the header
            EX: get_columns('example.csv', fruit, flavor) will search for the first line containing fruit and flavor
            and use that line as the header line (and not yielding any lines prior to the header line)

    $ Accept the kwarg 'write_file' which will write a file of the lines yielded instead of yielding them.
      EX: ('example.csv', 'fruit', write_file='fruit_names_only.csv') -> writes a file of only fruit names (no header)

    $ Accept the kwarg 'min_len' which checks if the line being yielded is at least that long, if it fails this check,
      print a warning to the user that contains the line being skipped and do not yield the line.
      EX: ('example.csv', min_len=7) will yield every line in example.csv, as long as its split length is 7 or more

    $ Accept the kwarg 'yield_header'; if this is set to True, yield the header of the file

        $ yield the header of the file, but only for the columns specified

    $ If only a single element is specified by *args, return it as a string and not a list of 1 string

    $ If all ints are provided to *args, yield those columns regardless of header
      EX: ('example.csv', 1, 3) --> ['flavor', 'durability']

        $$ Accept a mix of ints and strings, it is ok to return duplicate columns
           EX: ('example.csv', 0, fruit, 3) --> ['fruit', 'fruit', 'durability']
    """
    test = ""
    with open(filename,'r') as infile:
        if 'skip_lines' in kwargs:
            for x in range(int(kwargs.get('skip_lines'))):
                infile.readline()
        test = infile.readline()

    if ',' in test:
        seperator = ','
    elif '\t' in test:
        seperator = '\t'
        
    with open(filename,'r') as infile:
        if 'yield_header' in kwargs:
            if kwargs.get('skip_lines'):
                for x in range(int(kwargs.get('skip_lines'))):
                    infile.readline()
            if not kwargs.get('yield_header') == True:
                infile.readline()
        else:
            infile.readline()

        
        #To check if args and kwargs are passed
        if args and kwargs:
            my_list = []
            if not 'min_len' in kwargs:
                kwargs['min_len']=0
            for x in args:
                if type(x)==str:
                    for i,y in enumerate(test.strip().split()):
                        if x ==y:
                            my_list.append(i)
                else:
                    my_list.append(x)

            for line in infile:
                if len(line) > int(kwargs.get('min_len')):
                    new_list = []
                    if len(args) >1:
                        for x in my_list:
                            new_list.append(line.strip().split(seperator)[x])
                    else:
                        new_list = ''.join(line.strip().split(seperator)[my_list[0]])
                    if kwargs.get('write_file'):
                        with open(kwargs.get('write_file'),'a') as outfile:
                            outfile.write(','.join(new_list))
                            outfile.write('\n')
                    else:
                        yield(new_list) 
            
        #To check if only args is passed
        elif args:
            my_list = []
            for x in args:
                if type(x)==str:
                    for i,y in enumerate(test.strip().split()):
                        if x ==y:
                            my_list.append(i)
                else:
                    my_list.append(x)

            for line in infile:
                new_list = []
                if len(args) >1:
                    for x in my_list:
                        new_list.append(line.strip().split(seperator)[x])
                else:
                    new_list = ''.join(line.strip().split(seperator)[my_list[0]])
                yield new_list
                
        #To check if only kwargs is passed    
        elif kwargs:
            if not 'min_len' in kwargs:
                kwargs['min_len']=0
            for line in infile:
                if len(line) > int(kwargs.get('min_len')):
                    new_list = line.strip().split(seperator)
                    if kwargs.get('write_file'):
                        with open(kwargs.get('write_file'),'a') as outfile:
                            outfile.write(','.join(new_list))
                            outfile.write('\n')
                    else:
                        yield(new_list) 
            
        #To check if both args and kwargs are not passed
        else:
            for line in infile:
                new_list =  line.strip().split(seperator)
                yield(new_list) 

    
        
for x in read_columns('data/tsv_example.tsv',0,1,write_file='test.txt',min_len=15):
    print(x)
