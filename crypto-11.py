from math import factorial

def playfair_key_count():
    unique_keys = factorial(25)
    key_pairs = unique_keys // 2
    return unique_keys, key_pairs

unique_keys, key_pairs = playfair_key_count()
print(f"Possible unique keys: {unique_keys} (approximately 2^{unique_keys.bit_length()})")
print(f"Effectively unique keys considering pairs: {key_pairs} (approximately 2^{key_pairs.bit_length()})")
