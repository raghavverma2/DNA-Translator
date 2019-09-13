# DNA-Translator

A simple Python bioinformatics script to translate DNA nucleotides into RNA or proteins.

## Usage:

<code>python translate.py [dna source file] [option]</code>

* <code>[dna source file]</code> : The text file containing the DNA nucleotides sequence (adenine, guanine, cytosine, thymine). All line breaks and numbers are ignored.

* <code>[option]</code> : <code>--rna</code> for translation to RNA, <code>--protein</code> for translation to protein.

## Sample:

Try <code> python translate.py src.txt --rna</code> and <code>python translate.py src.txt --protein</code>.
