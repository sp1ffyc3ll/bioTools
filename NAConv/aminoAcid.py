from __future__ import absolute_import
from __future__ import division


class aminoAcid():
    def __init__(self, codon):
        self.codon = codon

    def match(self):
        if (self.codon[0] == "U"):
            if (self.codon[1] == "U"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Phe"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "Leu"

            elif (self.codon[1] == "C"):
                amino = "Ser"

            elif (self.codon[1] == "A"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Tyr"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "STOP"

            elif (self.codon[1] == "G"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Cys"
                elif (self.codon[2] == "A"):
                    amino = "STOP"
                elif (self.codon[2] == "G"):
                    amino = "Trp"

        elif (self.codon[0] == "C"):
            if (self.codon[1] == "U"):
                amino = "Leu"
            elif (self.codon[1] == "C"):
                amino = "Pro"
            elif (self.codon[1] == "A"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "His"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "Gin"
            elif (self.codon[1] == "G"):
                amino = "Arg"

        elif (self.codon[0] == "A"):
            if (self.codon[1] == "U"):
                if (self.codon[2] == "G"):
                    amino = "Met"
                else:
                    amino = "Ile"

            elif (self.codon[1] == "C"):
                amino = "Thr"

            elif (self.codon[1] == "A"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Asn"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "Lys"

            elif (self.codon[1] == "G"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Ser"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "Arg"

        elif (self.codon[0] == "G"):
            if (self.codon[1] == "U"):
                amino = "Val"
            elif (self.codon[1] == "C"):
                amino = "Ala"
            elif (self.codon[1] == "A"):
                if (self.codon[2] == "U" or self.codon[2] == "C"):
                    amino = "Asp"
                elif (self.codon[2] == "A" or self.codon[2] == "G"):
                    amino = "Glu"

            elif (self.codon[1] == "G"):
                amino = "Gly"
       
        return amino
