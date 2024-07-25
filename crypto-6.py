def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def decrypt_affine_cipher(ciphertext, a, b, m):
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        print(f"Inverse of {a} under modulo {m} doesn't exist.")
        return ""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b + m)) % m
            decrypted_text += chr(x + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text
ciphertext = "BUNCBUNCBUNC..."
m = 26
for a in range(1, m):
    if mod_inverse(a, m) is not None:
        for b in range(m):
            decrypted_text = decrypt_affine_cipher(ciphertext, a, b, m)
            print(f"Trying with a={a}, b={b}: {decrypted_text}")
