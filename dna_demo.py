from dna import *
from random import randint

c = Nucleotide("cytosine")
g = Nucleotide("guanine")
a = Nucleotide("adenine")
t = Nucleotide("thymine")
nucleotides = [c, g, a, t]

DNA = DNA()
for i in range(100):
    DNA.add_nucleotide(Nucleotide(nucleotides[randint(0, 3)]))

DNA.print_sequence()
