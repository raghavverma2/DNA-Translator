from sys import argv
import os
import re

# Translation from DNA to RNA is easy - just replacing the thymine ('T') with uracil ('U')
def rna(dna):
	rna = dna.replace("T", "U")
	print("RNA Sequence:\n" + rna)

def protein(dna):
	# The DNA codon for translation to protein, where each nucleotide triplet corresponds to an amino acid
	protein = {
				"TTT" : "F", "CTT" : "L",
				"ATT" : "I", "GTT" : "V",
				"TTC" : "F", "CTC" : "L", 
				"ATC" : "I", "GTC" : "V",
				"TTA" : "L", "CTA" : "L", 
				"ATA" : "I", "GTA" : "V",
				"TTG" : "L", "CTG" : "L", 
				"ATG" : "M", "GTG" : "V",
				"TCT" : "S", "CCT" : "P", 
				"ACT" : "T", "GCT" : "A",
				"TCC" : "S", "CCC" : "P", 
				"ACC" : "T", "GCC" : "A",
				"TCA" : "S", "CCA" : "P", 
				"ACA" : "T", "GCA" : "A",
				"TCG" : "S", "CCG" : "P", 
				"ACG" : "T", "GCG" : "A",
				"TAT" : "Y", "CAT" : "H", 
				"AAT" : "N", "GAT" : "D",
				"TAC" : "Y", "CAC" : "H", 
				"AAC" : "N", "GAC" : "D",
				"TAA" : "STOP", "CAA" : "Q", 
				"AAA" : "K", "GAA" : "E",
				"TAG" : "STOP", "CAG" : "Q", 
				"AAG" : "K", "GAG" : "E",
				"TGT" : "C", "CGT" : "R", 
				"AGT" : "S", "GGT" : "G",
				"TGC" : "C", "CGC" : "R", 
				"AGC" : "S", "GGC" : "G",
				"TGA" : "STOP", "CGA" : "R", 
				"AGA" : "R", "GGA" : "G",
				"TGG" : "W", "CGG" : "R", 
				"AGG" : "R", "GGG" : "G" 
	}

	# Delete all spaces, newlines and carriage returns
	dna = dna.replace(" ", "")
	dna = dna.replace("\n", "")
	dna = dna.replace("\r", "")
	dna = re.sub(r'\d+', '', dna)

	counter = 0
	# Generate protein sequence
	protein_sequence = ""
	for i in range(0, len(dna) -  + len(dna) % 3, 3):
		counter = i
		# If a STOP codon is reached, this signals the end of the polypeptide chain and translation is concluded
		if protein[dna[i:i+3]] == "STOP" :
			break

		protein_sequence += protein[dna[i:i+3]]
		if (i > 0) and ((i + 3) % 180 == 0):
			protein_sequence += " " + str(int(i / 3) + 1) + "\n"
	protein_sequence += " " + str(int(counter / 3) + 1)

	print("Protein Sequence:\n" + protein_sequence)

if __name__ == "__main__":
	filename = argv[1]
	option = argv[2]
	print("\nDNA Translator")

	if not os.path.isfile(filename):
		print("\nERROR: DNA source file not found")
		exit(1)

	file = open(filename, 'r')
	dna = file.read()

	print("\nDNA Sequence:\t\n" + dna + "\n")

	if option == "--rna":
		rna(dna)
	elif option == "--protein":
		protein(dna)