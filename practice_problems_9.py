"""
practice_problems_9.py
VERSION 0.1
CONTACT Klevi@sdsu.edu

This is an expansion to the previous homework's FastaReader class. For this practice you should:

    1. Write the clean_lines() function below this class. It should take in lines from FASTA files that
        have sequences on multiple lines between each header, like the bad_example.fasta for example:
            ['>header1', 'seq1', 'seq1.1', 'seq1.2', '>header2', 'seq2', 'seq2.1', 'seq2.2', '>header3', 'seq3', '>header4', 'seq4']))
        The sequences between each line should be concatenated to look like so:
            ['>header1', 'seq1seq1.1seq1.2', '>header2', 'seq2seq2.1seq2.2', '>header3', 'seq3', '>header4', 'seq4']))
        These new lines are then returned

    2. The __init__ function should also recognize if the input is a file or a directory using os.path.isfile()
         If the input is a Fasta file, it should be read and checked with clean_lines() normally
         If the input is not a file (and is a directory), then every Fasta file in the directory should
          be read and cleaned into self.lines

    3. Add Docstrings to the FastaReader class and class methods (you NEED to do the class Docstring)
        See: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#google-vs-numpy
         for a brief overview of Google and NumPy Docstrings by Sphinx

    4. Solve the missing code in the methods, get_complements(), get_amino_acids(), write_csv(), and duplicate_headers()
"""
import sys
import os
my_dict = {'A':'T','T':'A','C':'G','G':'C'}
class FastaReader:

    def __init__(self, fname):
        #Check if the input is file
        if os.path.isfile(fname):
            self.name = fname
            self.lines1 = [x.strip() for x in open(fname)]
        #Else if it is a folder do this
        else:
            fname = []
            for file in os.listdir("."):
                if file.endswith(".fasta"):
                    fname.append(file)
            self.lines1 = [y.strip() for x in fname for y in open(x)]
            self.name = ','.join([x for x in fname])
        # write your code here for #1
        self.lines = _clean_lines(self.lines1)
        print(self.lines)

        self.headers = [x for x in self.lines if x.startswith('>')]
        self.seqs = [x for x in self.lines if not x.startswith('>')]

    def to_dict(self):
        return {h:s for h,s in zip(self.headers, self.seqs)}

    def get_headers(self, n):
        return self.headers[:n]

    def get_seqs(self, n):
        return self.seqs[:n]

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.headers)


    def get_complements(self):
        """
        :return: a list of all complemented sequences in the FASTA file
        """
        return [''.join([my_dict[y] for y in x]) for x in self.seqs]


    def get_amino_acids(self):
        """
        :return: a list of all translated amino acid strings from self.seqs
        """
        DNA_TO_AA = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}
        return [''.join([DNA_TO_AA[x[y:y+3]] for y in range(0,len(x),3)]) for x in self.seqs]


    def duplicate_headers(self):
        """
        :return: True if duplicate headers exist, False otherwise
        """
        return [item for item,count in collections.Counter([x.split()[0] for x in self.lines1 if x.startswith('>')]).items() if count > 1]


    def write_csv(self, csv_filename):
        """
        Write the contents of the Fasta file to CSV format,
        where the first column is the header,
        and the second column is the sequence.
        :return: a string of the absolute path to csv_filename using os.path.abspath(csv_filename)
         (https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python)
        """
        with open("text.csv","w") as outfile:
            outfile.write(self.lines[0]+','+self.lines[1])
            for x in range(2,len(self.lines) -1,2):
                outfile.write('\n' + self.lines[x]+','+self.lines[x+1])
        return os.path.abspath(csv_filename)


def _clean_lines(lines):
    """
    if the lines of a FASTA file do not alternate sequence and header,
    then concatenate all sequences between each header and return a list of the new lines
    (Remember, the "_" Underscore at the beginning of a definition means it is intended to
      be 'private', but nothing is really 'private' in python -
      see https://mail.python.org/pipermail/tutor/2003-October/025932.html for a laugh)
    """
    my_dict = {}
    for line in lines:
        if line.startswith('>'):
            data = line.strip()
        else:
            if data in my_dict.keys():
                my_dict[data] = my_dict[data] + line.strip()
            else:
                my_dict[data] = line.strip()
    my_list = []
    for key,val in my_dict.items():
        my_list.append(key)
        my_list.append(val)
    return my_list






# --------- Usage cases, with assert statements ------------

if __name__ == '__main__':
    # Uncomment the next 2 lines to generate bad_example.fasta and example.fasta:

##    with open('bad_example.fasta', 'w') as outfile:
##        outfile.write('\n'.join(['>header1', 'seq1', 'seq1.1', 'seq1.2', '>header2', 'seq2', 'seq2.1', 'seq2.2', '>header3', 'seq3', '>header4', 'seq4']))

    # with open('example.fasta', 'w') as outfile:
    #     outfile.write('\n'.join(['>header1', 'seq1', '>header2', 'seq2', '>header3', 'seq3', '>header4', 'seq4']))

    ff = FastaReader('bad_example.fasta')

    x = ff.to_dict()
    assert x == {'>header1': 'seq1seq1.1seq1.2', '>header2': 'seq2seq2.1seq2.2', '>header3': 'seq3', '>header4': 'seq4'}

    x = ff.headers
    assert x == ['>header1', '>header2', '>header3', '>header4']

    x = ff.get_headers(2)
    assert x == ['>header1', '>header2']

    x = ff.seqs
    assert x == ['seq1seq1.1seq1.2', 'seq2seq2.1seq2.2', 'seq3', 'seq4']

    x = ff.get_seqs(3)
    assert x == ['seq1seq1.1seq1.2', 'seq2seq2.1seq2.2', 'seq3']

    x = len(ff)
    assert x == 4

    x = str(ff)
    assert x == 'bad_example.fasta'




