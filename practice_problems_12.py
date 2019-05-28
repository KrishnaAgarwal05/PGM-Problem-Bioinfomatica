"""
Regular Expressions 2

These are only 3 problems, but for each pattern you should be able to:
    1. find the start and stop positions of one or all matches
    2. use capture groups to extract variable regions within regex matches
    3. use re.sub to replace a regular expression pattern


"""
test_protein = """MHMWSFMMRFRKGGKPYHTVADARGPYDNGHLHKTYYLKNLMYYTVGMWVKEQLCCRHEP
RSFLLAFIWSWCLAGVYRLTHRGSGPEMNRVVMFQYQDECSYLLQVTDVAYCNEQAWYAR
FWSCIASSFEMSSHELHTQHYYTLTGSVDWNMYVQNGVWAHGIACSMTDNQDGSCRQPIM
DTDYVDTHDHEKRYRQRGLCSTPCNDQFPGYEFPTVHGTMAWISGEMMCASGYKPYNFKH
GEFSPKSIWEWQLFACCCCGKTEWSNVMIFMVVEIEIFASKSNEENWSGMNIIEDDDPQH
HFKNIYRKYLDFQFYLIYGGYRMGFLHHRDSMINALVCKTGRWQQMHSFLKCDRRCKYLI
NIYADGKWYDNWSKVEDKVLDRGIRFLQSWNATEMVNSSMYRKPFYQSQYAPRFCWETFC
QHEIYFHQEYASNCKARCGSYQSSAQSATLAIKYSELYQGFWGTSEWGHHQLFIHRWGVQ
IYQVKLHDSIMRPWIDWSRKCKWLLHRLHCDIELVPIHWEHKPQRVSFYYFKAMTDVLRE
ICWSAQYHVVIQKFAFITMAWICTFYVHMYPSLDRHGSVTGIAWKLSGQWTGQEAYSKLN
TEKETITEHNCPRVANIIVDCLEHEQVEMRMKRCHTWMVEVMKYPEQKFLWQCEHFRALY
GLVGHNCPIKAWVRWIPHMEQKVCSYFRRAYFMMLKNPMSRDSVCRREMEYDMAISRMPY
GDCHAVGKWLPYFLNRYTPWWVWIWMAPFQGNRFFYHYKKDWRHCGNYLGGLCVLMTFWH
HPIYVPCPKTKADFKQACCYCGKTRQACTDENMDTQRQKFQALHQARICQPYTVRNMSIQ
CGKNPIKANHNNNVRRPTMHICNLPAMTRRFVYTPFMKLKQSLGHDKWHIPEIQPYMDFT
YHSVWIHQPHMNSCAACTGTVALALALALHYYTHPIQGEYIIYTSCDARYKSQKQEDIYQ
ITSTCLEFSSKFKAQMMGTTWEIAGMNFCKVIETSCRQKI""".replace('\n', '')


import re

def kinase2(string):
    """
    Return a list of matched motifs to the VARIABLE REGION in the Casein Kinase II phosphorylation motif:
    a single S
    followed by any 2 Amino Acids   <-- variable region
    followed by a D or E
    :param string: the protein sequence to be searched
    :return: a list of strings
    """
    return re.findall(r'S.{2}[DE]',string)

print(kinase2(test_protein))

def atp_variable_region(string):
    """
    Return the 4 variable amino acids within
    the first matched ATP binding motif.  EX:
    If the matched motif is ACCCCGKS, this definition should return "CCCC"
    the ATP binding motif is:
    An "A" or "G"
    followed by any 4 Amino Acids
    followed by a "G"
    followed by a "K"
    followed by a "S" or "T"
    :param string: the protein sequence to be searched
    :return: a strings
    """
    return re.search(r'[AG](.{4})GK[ST]',string).group(1)

print(atp_variable_region(test_protein))
# #CCCC

def atp_start_pos(string):
    """
    Find the start position of the first match to the ATP binding site motif.
    the ATP binding motif is:
    An "A" or "G"
    followed by any 4 Amino Acids
    followed by a "G"
    followed by a "K"
    followed by a "S" or "T"
    :param string: the protein sequence to be searched
    :return: int
    """
    return re.search(r'[AG].{4}GK[ST]',string).span(0)[0]

print(atp_start_pos(test_protein))
# # 254

