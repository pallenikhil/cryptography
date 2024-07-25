def frequency_analysis(ciphertext):
    freq = [0] * 26
    for char in ciphertext:
        if char.isalpha():
            freq[ord(char.upper()) - ord('A')] += 1
    return freq

def print_frequency(freq):
    for i in range(26):
        print(f"{chr(i + ord('A'))}: {freq[i]}")

def decrypt_substitution_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += key[ord(char.upper()) - ord('A')]
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
freq = frequency_analysis(ciphertext)
print_frequency(freq)

# Define key based on frequency analysis
key = [
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D',
    'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
    'V', 'K', 'J', 'X', 'Q', 'Z'
]

decrypted_text = decrypt_substitution_cipher(ciphertext, key)
print(f"Decrypted: {decrypted_text}")
