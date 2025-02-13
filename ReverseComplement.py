def complement_dna(dna_strand):

    base_code = {'A', 'T', 'G', 'C', 'a', 't', 'g', 'c'}
    for codon in dna_strand:
        if codon not in base_code:
            return "Error: Input must include letters a,t,g,c only."
    
    complement = ""
    complement_codon = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

    for codon in dna_strand:
        complement +=complement_codon[codon]
    return complement

def reverse_string_slicing(cdna_to_reverse):
    return cdna_to_reverse[::-1]

def reverse_complement_dna(rcDNA):
    return complement_dna (reverse_string_slicing(rcDNA))

#Example
query_dna = "ATGCatgc"
result = reverse_complement_dna(query_dna)
print("your reversed cDNA strand is:", result)

#Example
query_dna = "FTTTTTTT"
print("your reversed cDNA strand is:",reverse_complement_dna(query_dna))