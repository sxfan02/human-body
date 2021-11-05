class DNA:
    def __init__(self, nucleotides=[]):
        self.sequence = nucleotides
        
    def add_nucleotide(self, nucleotide):
        self.sequence.append(nucleotide)

    def print_sequence(self):
        string = ""
        for nucleotide in self.sequence:
            string += str(nucleotide)[0].upper()
        print(string)

class Nucleotide:
    def is_valid(nucleotide):
        valid = ["cytosine", "guanine", "adenine", "thymine"]
        return nucleotide in valid

    def __init__(self, nucleotide):
        # copy constructor
        if type(nucleotide) == Nucleotide:
            self.name = nucleotide.name
            return
        # string constructor
        if Nucleotide.is_valid(nucleotide):
            self.name = nucleotide
        else:
            print("Invalid nucleotide!")

    # toString method
    def __str__(self):
        return self.name


