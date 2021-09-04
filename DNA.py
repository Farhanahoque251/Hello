def get_length(dna):
    """  (str) -> int
    Return the length of the dna sequene dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    >>> get_length('')
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str,str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA sequence dna2.
    >>> is_longer('ATCG','AT')
    True
    >>> is_longer('ATCG','ATCGGA')
    False
    """
    return len(dna1)>len(dna2)

def count_nucleotides(dna,nucleotide):
    """ (str,str)-> int
    Return the number of occurence of nucleotide in the DNA sequence dna.
    
    >>> count_nucleotides('ATGGC','G')
    2
    >>> count_nucleotides('ATCTA','G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    return True if and only if DNA sequence dna2 occurs in DNA sequence dna1.
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC','GT')
    False
    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str)-> bool
    Return True if DNA sequence dna contain 'A' 'T' 'C' or 'G'. 
    >>> is_valid_sequence('AATGC')
    True
    >>> is_valid_sequence('TTCHA')
    False
    """
    is_valid_sequence=0
    for char in dna:
        if not char in 'AGTC':
            is_valid_sequence = is_valid_sequence+1
        else:
            is_valid_sequence = is_valid_sequence           
    return is_valid_sequence == 0

def insert_sequence(dna1,dna2,index):
    """ (str,str,int)-> str
    Return the dna sequence obtained by inserting the first DNA sequence dna1 in second DNA sequence dna2.
    >>> insert_sequence('CCTTG','AT',2)
    'CCATTTG'
    >>> insert_sequence('AGCTA','GC',4)
    'AGCTGCA'
    """
    return dna1[:index]+dna2+dna1[index:]

def get_complement(nucleotide):
    """ (str)->str
    Return the complement of the nucleotide.
    >>> get_complement('A')
    'G'
    >>> get_complement('T')
    'C'
    >>> get_complement('G')
    'A'
    >>> get_complement('C')
    'T'
    """
    if nucleotide=='A':
        return 'G'
    if nucleotide=='T':
        return 'C'
    if nucleotide=='G':
        return 'A'
    if nucleotide=='C':
        return 'T'
    
def get_complementary_sequence(dna):
    """ (str)->str
    Return the complementary sequence of dna.
    >>> get_complementary_sequence('AGTCCG')
    'GACTTA'
    >>> get_complementary_sequence('AGTC')
    'GACT'
    >>> get_complementary_sequence('TA')
    'CG'
    >>> get_complementary_sequence('AGTCCG')
    'GACTTA'
    >>> get_complementary_sequence('')
    ''
    >>> get_complementary_sequence('GCTAGCTA')

    >>> get_complementary_sequence('TAGCTAGC')
    """
    complementary_sequence=''
    for char in dna:
        complementary_sequence=complementary_sequence+get_complement(char)
    return(complementary_sequence)    
    
