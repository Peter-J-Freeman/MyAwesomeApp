def complement_dna(dna_strand):

    codon = {'A' or 'T' or 'G' or 'C' or 'a' or 't' or 'g' or 't'}
    if not isinstance(dna_strand, codon):
        return "Error: Input must include letters a,t,g,c only."

    complement = ""
    complement_codon = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

    for codon in dna_strand:
        complement +=complement_codon[codon]
    return complement

print("your complement dna strand is:", complement)

