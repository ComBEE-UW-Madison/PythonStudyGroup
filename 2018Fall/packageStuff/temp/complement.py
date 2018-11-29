class Complement:
    """takes a string of ATGC
    """
    def __init__(self, dna_string):
        """Takes a dna string"""
        self.dna = dna_string
    
    def complement(self):
        return(self.dna.translate(str.maketrans('ACGT', 'TGCA')))
    
    def rev_complement(self):
        return(self.dna[::-1].translate(str.maketrans('ACGT', 'TGCA')))
