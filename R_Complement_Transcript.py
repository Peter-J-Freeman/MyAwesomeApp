def complement_seq(strand):
    base_code = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}
    for codon in strand:
        if codon not in base_code:
            return "Error: Input must include letters a, t/u, g, c only."
        if (seq == "d") and ("U" or "u" in strand):
            return "Error: DNA strand cannot contain U/u."
        if (seq == "r") and ("T" or "t" in strand):
            return "Error: RNA strand cannot contain T/t."

    complement = ""
    complement_codon = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }
    if input == "r":
        complement_codon["U"] = "A"
        complement_codon["u"] = "a"
        complement_codon["A"] = "U"
        complement_codon["a"] = "u"

    for codon in strand:
        complement += complement_codon[codon]
    return complement


def reverse_string_slicing(cdna_to_reverse):
    return cdna_to_reverse[::-1]


def reverse_complement_dna(rcdna):
    return complement_seq(reverse_string_slicing(rcdna))


def print_rcdna(rcdna):
    result = reverse_complement_dna(rcdna)
    print("your reversed cDNA strand is:", result)


def seq():
    return input("what is your sequence type (d for DNA - r for RNA)")


def input_seq():
    return input("Enter your sequence: ")


seq_type = seq()
query_seq = input_seq()
print_rcdna(query_seq)
