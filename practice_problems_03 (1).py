"""
Practice problems 3:

Reading File Types

NOTE: if this is your first time working with file paths, you may get a
 FileNotFoundError: [Errno 2] No such file or directory: 'my_folder/myfile.txt'
If you are sure the file exists, then you are entering the wrong path to your file.

For example: data/example_1.fasta will look for a folder called 'data' in the same directory as your python script,
once it has found the folder 'data' it will look inside for a file called 'example_1.fasta'
If you do not have a folder called 'data' next to your python script, you will get an error
If you do not have a file called 'example_1.fasta' in that folder, you will get an error
"""


##def rev_compliment(dna):
##    """
##    for a string of DNA (Only A, T, C  and G), return its reverse compliment  (A <--> T) and  (G <--> C)
##    """
##    my_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G' }
##    my_str = ""
##    for letter in dna:
##        my_str = my_str + my_dict[letter]
##
##    print(my_str[::-1])
##    return
##
##rev_compliment('AAACCCGGGTTT')

##def transcribe(dna):
##    """
##    DNA is converted to RNA through transcription, transcribe the string of DNA to RNA
##    (the string is given 5' -> 3' and your result should be read 5' -> 3')
##    EX: transcribe('CTGATCAG') returns 'CUGAUCAG'
##    """
##    my_dict = {'A':'U', 'T':'A', 'G':'C', 'C':'G' }
##    my_str = ""
##    for letter in dna:
##        my_str = my_str + my_dict[letter]
##
##    print(my_str[::-1])
##    return
##
##transcribe('CTGATCAG')

##def possible_proteins(amino_acids):
##    """
##    for a string of amino acids (using one letter codes), return a list of possible proteins
##    (proteins can start at any Methionine (M) and end at the first stop codon (*) )
##    EX: AYKPMVVVYYYMP*MAA  will have only two possible proteins:
##    MVVVTTTMP*   and    MP*
##    """
##    my_dict = amino_acids.split('*')
##    word = my_dict[0]
##    for i,letter in enumerate(word):
##        if letter == 'M':
##            print(word[i:]+"*")
##            
##    return
##
##possible_proteins('AYKPMVVVYYYMP*MAA')

##def first_n_lines(file_name, n):
##    """
##    prints the first n lines from a file AND returns them as a list
##    """
##    with open(file_name,'r') as infile:
##        for i in range(n):
##            print(infile.readline().strip())
##    return
##
##first_n_lines('data/test.txt', 5)

##def lines_m_to_n(file_name, m, n):
##    """
##    prints the lines m through n from a file AND returns them as a list
##    """
##    with open(file_name, 'r') as infile:
##        for i in range(m-1):
##            infile.readline()
##        for i in range(n-m+1):
##            print(infile.readline().strip())
##    return
##
##lines_m_to_n('data/test.txt', 2,5)

##def first_column(file_name):
##    """
##    Reads in a CSV file and returns a list of all entries in column 1
##    """
##    with open(file_name, 'r') as infile:
##        for line in infile:
##            data = line.split(',')
##            print(data[0])
##    return
##
##first_column('data/csv_example.csv')

##def check_delimiter(file_name):
##    """
##    Reads in a file, and determines if the first line is splittable by commas, tabs, or None,
##    and returns either  ','   '\t'   or   None
##    """
##    with open(file_name,'r') as infile:
##        data = infile.readline()
##        if ',' in data:
##            return ','
##        elif '\t' in data:
##            return 'Tab'
##        elif None in data:
##            return None
##
##print(check_delimiter('data/tsv_example.tsv'))


##def get_rows_by_name(file_name, name):
##    """
##    Reads the CSV file, file_name, and returns a list of every row where the first item in that row is 'name'
##    for example, return a list of every row from csv_example.csv where the first column is 'banana'
##    """
##    with open(file_name,'r') as infile:
##        for file in infile:
##            if file.startswith(name):
##                print(file.strip())
##    return
##
##get_rows_by_name('data/csv_example.csv', 'apple')

##def columns_to_dictionary(file_name, m, n):
##    """
##    Reads the CSV file, file_name, and return a dictionary where each row is an entry,
##    the key should be the item in the m column, and the value should be the item in the n column
##    For example, return a dictionary of the form {fruit_name: taste, ...} for each fruit in csv_example.csv
##    """
##    my_dict = {}
##    with open(file_name,'r') as infile:
##        for line in infile:
##            data = line.split(',')
##            my_dict[data[m].strip()] = data[n].strip()
##    print(my_dict)
##    return
##
##columns_to_dictionary('data/csv_example.csv', 0, 3)

##def fasta_headers(file_name):
##    """
##    return a list of headers for the FASTA file
##    """
##    with open(file_name,'r') as infile:
##        for line in infile:
##            if line.startswith('>'):
##                data = line.split(' ')
##                print(data[0][1:])
##    return
##
##fasta_headers('data/fasta_example.fasta')

##def fastq_headers(file_name):
##    """
##    prints a list of headers for reads in the FASTQ file
##    """
##    with open(file_name,'r') as infile:
##        for line in infile:
##            if line.startswith('@'):
##                data = line.split(' ')
##                print(data[0][1:].strip())
##    return
##
##fastq_headers('data/fastq_example.fastq')

##def fasta_sequences(file_name):
##    """
##    returns a list of sequences in a fasta file
##    """
##    with open(file_name,'r') as infile:
##        for line in infile:
##            if not line.startswith('>'):
##                print(line.strip())
##    return
##
##fasta_sequences('data/fasta_example.fasta')

##def fasta_overlap(fasta_one, fasta_two):
##    """
##    returns a list of headers that are present in both fasta files
##    """
##    with open(fasta_one,'r') as infile1, open(fasta_two,'r') as infile2:
##        my_dict1 = []
##        my_dict2 = []
##        final_list = []
##        for line1 in infile1:
##            if line1.startswith('>'):
##                data = line1.split(' ')
##                my_dict1.append(data[0][1:])
##
##        for line2 in infile2:
##            if line2.startswith('>'):
##                data = line2.split(' ')
##                my_dict2.append(data[0][1:])
##
##        for x in my_dict1:
##            if x in my_dict2:
##                final_list.append(x)
##        print(final_list)
##    return
##
##fasta_overlap('data/fasta_example.fasta','data/fasta_example2.fasta')

def fasta_dictionary(fasta_file):
    """
    returns a dictionary where each key/value pair is a header/sequence in the fasta file
    {">human": "AAACCCGGGTTT", ...}
    """
    num_lines = 0
    with open(fasta_file, 'r') as f:
        for line in f:
            num_lines += 1
    my_list = {}
    with open(fasta_file,'r') as infile:
        for line in infile:
            if (line.startswith('>')):
                data = line.split(' ')
                data = data[0][1:]
            else:
                if data in my_list:
                    my_list[data] = my_list[data]+line.strip()
                else:
                    my_list[data] = line.strip()                
    return my_list

print(fasta_dictionary('data/fasta_example.fasta'))

##def check_duplicates(fasta_file):
##    """
##    returns a list of headers that are present multiple times within a file
##    """
##    my_dict = {}
##    with open(fasta_file,'r') as infile:
##        for line in infile:
##            if line.startswith('>'):
##                data = line.split(' ')
##                my_dict[data[0][1:]] = my_dict.get(data[0][1:],0) + 1
##        
##        for keys,val in my_dict.items():
##            if val > 1:
##                print(keys)
##    return
##
##check_duplicates('data/fasta_example2.fasta')

##def vcf_header(vcf_file):
##    """
##    return the entire header sequence of a VCF file (the header region is the section where every line starts with ##)
##    """
##    with open(vcf_file,'r') as infile:
##        for line in infile:
##            if line.startswith('##'):
##                print(line[2:].strip())
##    return
##
##vcf_header('data/vcf_example.vcf')

##def vcf_region(vcf_file, m, n):
##    """
##    return a list of every row in the VCF file where POS (position) is between m and n
##    EX: m=10000, n=200000 and the example VCF file will return a list of the elements:
##    20     14370   rs6054257 G      A       29   PASS   NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
##    20     17330   .         T      A       3    q10    NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3   0/0:41:3
##    """
##    with open(vcf_file,'r') as infile:
##        for line in infile:
##            if not line.startswith('#'):
##                data = line.strip().split()
##                if int(data[1]) > m and int(data[1]) < n:
##                    print(line)
##                
##    return

##vcf_region('data/vcf_example.vcf',10000, 20000)

##def no_compliments(fasta_file):
##    """
##    check every sequence in the FASTA file to see if it's reverse compliment is already in the file
##    return True if no compliments are present, return False otherwise
##    """
##    with open(fasta_file,'r') as infile:
##        my_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
##        line_dict = {}
##        for line in infile:
##            if not line.startswith('>'):
##                my_str = ""
##                line_dict[line.strip()] = line_dict.get(line.strip(),0) + 1
##                for letter in line.strip():
##                    my_str = my_str + my_dict[letter]
##                line_dict[my_str] = line_dict.get(my_str,0) + 1
##
##        for keys, val in line_dict.items():
##            if val > 1:
##                return False
##            
##    return True
##
##print(no_compliments('data/fasta_example.fasta'))

##def no_compliments(fastq_file):
##    """
##    check every sequence in the FASTQ file to see if its reverse compliment is already in the file
##    **FASTQ files are typically much larger than FASTA files, be sure to use the correct data structures
##    return True if no duplicates exist, return False otherwise
##    """
##    with open(fastq_file,'r') as infile:
##        my_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
##        line_dict = {}
##        for line in infile:
##            if not line.startswith('@') and not line.startswith('+') and not line.startswith('!'):
##                my_str = ""
##                line_dict[line.strip()] = line_dict.get(line.strip(),0) + 1
##                for letter in line.strip():
##                    my_str = my_str + my_dict[letter]
##                line_dict[my_str] = line_dict.get(my_str,0) + 1
##
##        for keys, val in line_dict.items():
##            if val > 1:
##                return False
##    return True
##
##print(no_compliments('data/fastq_example.fastq'))




