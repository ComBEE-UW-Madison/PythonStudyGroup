class DNARecord(object):

    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    def complement(self):
        replacement1 = self.sequence.replace('A', 't')
        replacement2 = replacement1.replace('T', 'a')
        replacement3 = replacement2.replace('C', 'g')
        replacement4 = replacement3.replace('G', 'c')
        return replacement4.upper()

    def get_AT_content(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content

    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n'

d1 = DNARecord('ATATATTATTATTAATATATA', 'COX1', 'Homo sapiens')
print(d1.complement())
print(d1.get_fasta())

# If have a list of DNARecord objects, generate a FASTA file with sequences at high AT content

output = open("high_at.fasta", "w")
for d in my_dna_records:
    if d.get_AT()> 0.6:
        output.write(d.get_fasta())

