def generate_cipher(keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = []
    for char in keyword.upper():
        if char not in cipher:
            cipher.append(char)
    for char in alphabet:
        if char not in cipher:
            cipher.append(char)
    return ''.join(cipher)

def encrypt_monoalphabetic(plaintext, cipher):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            encrypted_text += cipher[alphabet.index(char.upper())]
        else:
            encrypted_text += char
    return encrypted_text

keyword = "CIPHER"
plaintext = "HELLO WORLD"
cipher = generate_cipher(keyword)
print(f"Cipher: {cipher}")

encrypted_text = encrypt_monoalphabetic(plaintext, cipher)
print(f"Encrypted: {encrypted_text}")

