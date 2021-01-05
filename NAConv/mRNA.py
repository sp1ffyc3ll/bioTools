from __future__ import absolute_import
from __future__ import division


class mRNA():
    def __init__(self, codon):
        self.codon = codon

    def convert(self):
        codon = ""

        for i in self.codon:
            if (i == "A"):
                codon += "U"
            elif (i == "T"):
                codon += "A"
            elif (i == "C"):
                codon += "G"
            elif (i == "G"):
                codon += "C"
        return codon