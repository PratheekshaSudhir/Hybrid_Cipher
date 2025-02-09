import numpy as np

# --- Hill Cipher (Substitution Technique) ---
def text_to_numbers(text, size):
    """ Convert text to numerical representation """
    text = text.upper().replace(" ", "")  # Remove spaces
    while len(text) % size != 0:
        text += "X"  # Padding if needed
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    """ Convert numbers back to text """
    return "".join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key_matrix):
    """ Encrypt using Hill Cipher """
    size = len(key_matrix)
    plaintext_nums = text_to_numbers(plaintext, size)
    
    # Split into blocks of 'size'
    encrypted_nums = []
    for i in range(0, len(plaintext_nums), size):
        block = np.array(plaintext_nums[i:i+size]).reshape(size, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_nums.extend(encrypted_block.flatten().tolist())

    return numbers_to_text(encrypted_nums)

def hill_decrypt(ciphertext, key_matrix):
    """ Decrypt using Hill Cipher """
    size = len(key_matrix)
    ciphertext_nums = text_to_numbers(ciphertext, size)

    # Compute modular inverse of key matrix
    determinant = int(round(np.linalg.det(key_matrix)))
    determinant_inv = pow(determinant, -1, 26)
    key_inv = determinant_inv * np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % 26

    decrypted_nums = []
    for i in range(0, len(ciphertext_nums), size):
        block = np.array(ciphertext_nums[i:i+size]).reshape(size, 1)
        decrypted_block = np.dot(key_inv, block) % 26
        decrypted_nums.extend(decrypted_block.flatten().tolist())

    return numbers_to_text(decrypted_nums)

# --- Single Columnar Transposition (Transposition Technique) ---
def columnar_encrypt(text, key):
    """ Columnar Transposition Encryption """
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    columns = len(key)

    # Pad text if needed
    while len(text) % columns != 0:
        text += "X"

    rows = len(text) // columns
    grid = [list(text[i * columns:(i + 1) * columns]) for i in range(rows)]

    encrypted_text = ""
    for index, _ in key_order:
        for row in grid:
            encrypted_text += row[index]

    return encrypted_text

def columnar_decrypt(text, key):
    """ Columnar Transposition Decryption """
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    columns = len(key)
    rows = len(text) // columns

    grid = [[''] * columns for _ in range(rows)]
    idx = 0

    for index, _ in key_order:
        for row in range(rows):
            grid[row][index] = text[idx]
            idx += 1

    decrypted_text = "".join(["".join(row) for row in grid])
    return decrypted_text

# --- Hybrid Cipher Execution ---
def hybrid_encrypt(plaintext, hill_key, transposition_key):
    """ Encrypt using Hill Cipher + single Columnar Transposition """
    original_length = len(plaintext.replace(" ", ""))  # Store the actual length
    
    hill_cipher_text = hill_encrypt(plaintext, hill_key)
    final_cipher_text = columnar_encrypt(hill_cipher_text, transposition_key)
    
    return final_cipher_text, original_length  # Return ciphertext with original length

def hybrid_decrypt(ciphertext, hill_key, transposition_key, original_length):
    """ Decrypt in reverse order: Columnar Transposition -> Hill Cipher """
    columnar_cipher_text = columnar_decrypt(ciphertext, transposition_key)
    plaintext = hill_decrypt(columnar_cipher_text, hill_key)
    
    return plaintext[:original_length]  # Trim extra padding

# --- Example Usage ---
hill_key = np.array([[3, 3], [2, 5]])  # 2x2 Hill Cipher Key (Must be invertible mod 26)
transposition_key = "431256"  # Key for single Columnar Transposition

plaintext = input("enter a plain text to encrypt: ")
ciphertext,original_length = hybrid_encrypt(plaintext, hill_key, transposition_key)
decrypted_text = hybrid_decrypt(ciphertext, hill_key, transposition_key,original_length)

print(f"Original Text: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
