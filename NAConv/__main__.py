from __future__ import absolute_import
from __future__ import division

import sys
from aminoAcid import aminoAcid
from mRNA import mRNA

CODON_SIZE = 3

def init():
    inputStrand = str(input("Input your DNA strand: ").replace(' ', '').upper())
    dnaOutputStrand = []
    mRNAOutputStrand = []
    proteinOutputStrand = []

    for i in range(0, len(inputStrand)):
        if (i % CODON_SIZE == 0):
            codon = inputStrand[i] + inputStrand[i + 1] + inputStrand[i + 2]
            dnaOutputStrand.append(codon)

            mrna = mRNA(codon)
            mRNACodon = mrna.convert()
            mRNAOutputStrand.append(mRNACodon)

            amino = aminoAcid(mRNACodon)
            proteinOutput = amino.match()
            proteinOutputStrand.append(proteinOutput)

    print("DNA: {}".format(dnaOutputStrand))
    print("mRNA: {}".format(mRNAOutputStrand))
    print("Protein: {}".format(proteinOutputStrand))


if __name__ == "__main__":
    init()
