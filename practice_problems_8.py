"""
Write your own class that will match the usage cases at the bottom of the file
"""

class FastaReader:
    def __init__(self,fasta_file):
        self.file_name = fasta_file
        self.lines = [x.strip() for x in open(fasta_file,'r')]
        self.headers = [x.split()[0] for x in self.lines if x.startswith('>')]
        self.seqs = [x.split()[0] for x in self.lines if not x.startswith('>')]

    def __str__(self):
        return self.file_name
    
    def __len__(self):
        return len(self.headers)

    def get_headers(self,n):
        return [self.headers[x] for x in range(n)]

    def get_seqs(self,n):
        return [self.seqs[x] for x in range(n)]

    def to_dict(self):
        return {h:s for h,s in zip(self.headers,self.seqs)}

# --------- Usage cases, with assert statements ------------
# Uncomment the next 2 lines to generate example.fasta:
with open('example.fasta', 'w') as outfile:
    outfile.write('\n'.join(['>header1', 'seq1', '>header2', 'seq2', '>header3', 'seq3', '>header4', 'seq4']))



ff = FastaReader('example.fasta')

x = ff.to_dict()
assert x == {'>header1': 'seq1', '>header2': 'seq2', '>header3': 'seq3', '>header4': 'seq4'}

x = ff.headers
assert x == ['>header1', '>header2', '>header3', '>header4']

x = ff.get_headers(2)  # returns the first n headers
assert x == ['>header1', '>header2']

x = ff.seqs
assert x == ['seq1', 'seq2', 'seq3', 'seq4']

x = ff.get_seqs(3)
assert x == ['seq1', 'seq2', 'seq3']

x = len(ff)
assert x == 4

x = str(ff)
assert x == 'example.fasta'




