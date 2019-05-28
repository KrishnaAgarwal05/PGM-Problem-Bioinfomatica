"""
Practice Problems 5

This is a collection of problems from the previous practice problems that can use Comprehension in some way.
In addition to this, it would be helpful to be able to solve all of exam 1 in list comprehension!


Using comprehension on all of these problems is possible, but may be less effective on some problems - especially those that return booleans
These problems do NOT need to be solved in one line. (but many of them can be!)
"""

my_dict = {'T':'A','A':'T','G':'C','C':'G'}
my_dict1 = {'T':'A','A':'U','G':'C','C':'G'}
##def first_ten(my_list):
##    """
##    return a list of the first 10 elements in my_list
##    """
##    return [x for x in my_list[:10]] 
##
##print(first_ten([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


##def last_ten(my_list):
##    """
##    return a list of the last 10 elements in my_list
##    """
##    return [my_list[x] for x in range(len(my_list)-1, len(my_list)-11,-1)]
##
##print(last_ten([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

##def every_second(my_list):
##    """
##    return a list of the every second element
##    """
##    return [my_list[x] for x in range(1,len(my_list)-1,2)]
##
##print(every_second([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

##def count_letters(my_string):
##    """
##    return a dictionary where keys are letters in my_string, and values are the number of times that letter has occurred
##    """
##    return {x:my_string.count(x) for x in my_string}
##
##print(count_letters('krishnaagarwal'))

##def add_words(my_list, my_dict):
##    """
##    add each object in my_list to my_dict, where the key is the object, and the value is the number of times that object has occurred
##    """
##    return {x: my_list.count(x) for x in my_list}
##
##print(add_words(['apple','banana','apple'],{}))

##def overlap(x, y):
##    """
##    Given two lists, x and y, return a new list of all elements that are in both lists
##    """
##    return list(set(x).intersection(set(y)))
##
##print(overlap([1,2,3,4],[3,4,5,6]))

##def only_x(x, y):
##    """
##    Given two lists, x and y, return a new list of all elements that are ONLY found in x
##    """
##
##    return list(set(x) - (set(y)))
##
##print(only_x([1,2,3,4],[3,4,5,6]))

##def rev_compliment(dna):
##    """
##    for a string of DNA (Only A, T, C  and G), return its reverse compliment  (A <--> T) and  (G <--> C)
##    """
##    return ''.join([my_dict[x] for x in dna[::-1]])
##
##print(rev_compliment('ATTAGCCG'))

##def transcribe(dna):
##    """
##    DNA is converted to RNA through transcription, transcribe the string of DNA to RNA
##    (the string is given 5' -> 3' and your result should be read 5' -> 3')
##    EX: transcribe('CTGATCAG') returns 'CUGAUCAG'
##    """
##    return ''.join([my_dict1[x] for x in dna[::-1]])
##
##print(transcribe('CTGATCAG'))

##def first_column(file_name):
##    """
##    Reads in a CSV file and returns a list of all entries in column 1
##    """
##    return [x.split(',')[0] for x in open(file_name,'r')]
##
##print(first_column('data/csv_example.csv'))

##def get_rows_by_name(file_name, name):
##    """
##    Reads the CSV file, file_name, and returns a list of every row where the first item in that row is 'name'
##    for example, return a list of every row from csv_example.csv where the first column is 'banana'
##    """
##    return [x.split() for x in open(file_name,'r') if x.startswith(name)]
##
##print(get_rows_by_name('data/csv_example.csv','banana'))

##def columns_to_dictionary(file_name, m, n):
##    """
##    Reads the CSV file, file_name, and return a dictionary where each row is an entry,
##    the key should be the item in the m column, and the value should be the item in the n column
##    For example, return a dictionary of the form {fruit_name: taste, ...} for each fruit in csv_example.csv
##    """
##    return {line.split(',')[m]: line.split(',')[n] for line in open(file_name,'r')}
##
##print(columns_to_dictionary('data/csv_example.csv',0,2))

##def fasta_headers(file_name):
##    """
##    return a list of headers for the FASTA file
##    """
##    return [line.split()[0] for line in open(file_name,'r') if line.startswith('>')]
##
##print(fasta_headers('data/fasta_example.fasta'))

##def fastq_headers(file_name):
##    """
##    prints a list of headers for reads in the FASTQ file
##    """
##    return [line.split()[0] for line in open(file_name,'r') if line.startswith('@')]
##
##print(fastq_headers('data/fastq_example.fastq'))

##def fasta_sequences(file_name):
##    """
##    returns a list of sequences in a fasta file
##    """
##    return [line.split()[0] for line in open(file_name,'r') if not line.startswith('>')]
##
##print(fasta_sequences('data/fasta_example.fasta'))

##def fasta_overlap(fasta_one, fasta_two):
##    """
##    returns a list of headers that are present in both fasta files
##    """
##    return list(set([x.split()[0] for x in open(fasta_one,'r') if x.startswith('>')]).intersection(set([x.split()[0] for x in open(fasta_two,'r') if x.startswith('>')])))
##
##print(fasta_overlap('data/fasta_example.fasta','data/fasta_example2.fasta'))

##def fasta_dictionary(fasta_file):
##    """
##    returns a dictionary where each key/value pair is a header/sequence in the fasta file
##    {">human": "AAACCCGGGTTT", ...}
##    """
##    return {h:s for h,s in zip([x.split()[0] for x in open(fasta_file,'r') if x.startswith('>')],[x.strip() for x in open(fasta_file,'r') if not x.startswith('>')])}
##
##print(fasta_dictionary('data/fasta_example.fasta'))

def check_duplicates(fasta_file):
    """
    returns a list of headers that are present multiple times within a file
    """
    return list(set([x.split()[0] for x in open(fasta_file,'r') if [x.split()[0] for x in open(fasta_file,'r') if x.startswith('>')].count(x.split()[0]) > 1]))

print(check_duplicates('data/fasta_example.fasta'))

##def vcf_header(vcf_file):
##    """
##    return the entire header sequence of a VCF file (the header region is the section where every line starts with ##)
##    """
##    return [x.strip() for x in open(vcf_file,'r') if x.startswith('##')]
##
##print(vcf_header('data/vcf_example.vcf'))

##def no_compliments(fasta_file):
##    """
##    check every sequence in the FASTA file to see if it's reverse compliment is already in the file
##    return True if no compliments are present, return False otherwise
##    """
##    return not len([x.strip() for x in open(fasta_file,'r') if x.strip() in [''.join([my_dict[y] for y in x.strip()[::-1]]) for x in open(fasta_file,'r') if not x.startswith('>')] ])>0
##
##print(no_compliments('data/fasta_example.fasta'))
