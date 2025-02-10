def reverse_string_slicing(strand):
    print(f"call reverce_string_slicing({strand})")
    return strand[::-1]

strand = "atgcatgc"
generate = reverse_string_slicing(strand)
print(generate)

