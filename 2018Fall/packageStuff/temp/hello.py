#! /usr/bin/env python3

def gc_content(dna=None):
        """calculates gc content
        >>> gc_content("ATGC")
        0.5
        
        >>> gc_content("TTTT")
        9
        """
        if not dna:
            dna = "ATCGATTTTTT".upper()
        else:
            dna = dna.upper()

        g = dna.count("G")
        c = dna.count("C")
#        print(g, c, len(dna))
        return( (g+c) / len(dna)) # PEMDAS

if __name__ == "__main__":
    import doctest
    doctest.testmod()
