def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=key.index)).upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def decrypt_digraph(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair_cipher(ciphertext, matrix):
    ciphertext = ciphertext.replace(" ", "").upper()
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        decrypted_text += decrypt_digraph(matrix, digraph)
    return decrypted_text

key = "MFHIKUNOPQZVWXEYLABRDSG"
ciphertext = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUSRWRGDSONSXBOUYWRHEBAAHYUEDQ"
matrix = create_playfair_matrix(key)
print("Playfair Matrix:")
for row in matrix:
    print(row)

decrypted_text = decrypt_playfair_cipher(ciphertext, matrix)
print(f"Decrypted: {decrypted_text}")
