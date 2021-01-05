# NAConv
## a simple nucleic acid converter written in Python
---
<br>
<p>This code is a straightforward CLI where the user inputs a DNA strand.</p>
<p>The DNA sequence can be entered as an uninterrupted line, or as codons (triplets) - either upper- or lower-case:</p>
<code>> agctcaaagtcg</code><br>
<code>> AGC TCA AAG TCG</code>
<br><br>
<p>The output will show the DNA codons, the
mRNA translations, and the amino acids that would be mapped during protein biosynthesis.</p>

<code>$ python \__main\__.py</code><br>
<code>Input your DNA strand: agc taa agc tgg</code><br>
<code>DNA: ['AGC', 'TAA', 'AGC', 'TGG']</code><br>
<code>mRNA: ['UCG', 'AUU', 'UCG', 'ACC']</code><br>
<code>Protein: ['Ser', 'Ile', 'Ser', 'Thr']</code><br>