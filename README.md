# DNA-Translator

A Python script for translating DNA nucleotides sequence into RNA or proteins. First steps into bioinformatics.

## Usage:

<code>python translate.py [dna source file] [option]</code>

* <code>[dna source file]</code> : The text file containing the DNA nucleotides sequence (adenine, guanine, cytosine, thymine). All line breaks and numbers are ignored.

* <code>[option]</code> : <code>--rna</code> for translation to RNA, <code>--protein</code> for translation to protein.

## Sample:

src.txt contains a sample DNA sequence of E. Coli (<i>Escherichia coli</i>) K12, nucleotides 0 to 10,000, a non-pathogenic strain that cannot survive in your digestive tract.

Try <code> python translate.py src.txt --rna</code> or <code>python translate.py src.txt --protein</code>, or check out the <code>/sample outputs</code> directory which contains the results.
