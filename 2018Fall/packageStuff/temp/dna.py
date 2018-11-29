class DNA:
    """takes a string of ATGC
    """
    def __init__(self, dna_string):
        """Takes a dna string"""
        self.dna = dna_string
    
    def gc_content(self, dna=None):
        """calculates gc content
        >>> gc_content("ATGC")
        0.5
        
        >>> gc_content("TTTT")
        9
        """
        if not dna:
            self.dna = self.dna.upper()
        else:
            self.dna = dna.upper()

        g = self.dna.count("G")
        c = self.dna.count("C")
        print(g, c, len(self.dna))
        return( (g+c) / len(self.dna)) # PEMDAS
