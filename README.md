# Hybrid Cipher Encryption
## Overview
This project implements a Hybrid Cipher that combines two classical encryption techniques:

- Hill Cipher (Substitution Technique): Uses linear algebra (matrix multiplication) to encrypt blocks of text.
- Single Columnar Transposition (Transposition Technique): Rearranges the encrypted text by reading it column-wise based on a key.
The hybrid approach first encrypts the plaintext using the Hill cipher and then applies a columnar transposition on the result.Decryption reverses these steps.

## Features
### Hill Cipher Encryption & Decryption:
- Converts text to numerical form (A=0, B=1, …, Z=25).
- Handles padding if the text length isn’t a multiple of the key matrix size.
- Uses a key matrix (which must be invertible modulo 26) to encrypt and decrypt text.
### Single Columnar Transposition Encryption & Decryption:
- Rearranges characters into a grid based on the length of the transposition key.
- Reads the grid columns in a sorted order defined by the key.
- Applies necessary padding to the text.
### Hybrid Encryption & Decryption:
- Encrypts the plaintext with the Hill cipher.
- Applies a columnar transposition to the Hill cipher text.
- For decryption, reverses the transposition followed by the Hill decryption.
- Trims any extra padding from the final output.

## How It Works
### Hill Cipher:
- Encryption: Converts the plaintext to numbers, groups them into blocks matching the key matrix size, and encrypts each block using matrix multiplication modulo 26.
- Decryption: Computes the modular inverse of the key matrix and applies it to the ciphertext blocks to retrieve the original numerical values before converting back to text.
### Columnar Transposition:
- Encryption: The text is arranged into a grid (rows × columns), and then columns are read based on the sorted order of the key.
- Decryption: The process is reversed by filling the grid column-wise according to the key order and then reading row-wise.
### Hybrid Process:
- Encryption: The plaintext is first encrypted with the Hill cipher. The resulting ciphertext is then encrypted using the columnar transposition method.
- Decryption: The ciphertext is first decrypted with the columnar transposition method to recover the Hill cipher text, which is then decrypted using the Hill cipher decryption.

## Prerequisites
1) Python 3.x
2) NumPy Library
Install the required library using pip:
```ssh
pip install numpy
```

## How to use the code
1) Clone the Repository (if hosted on GitHub):
```ssh
git clone https://github.com/yourusername/hybrid-cipher.git
cd hybrid-cipher
```
2) Run the Script:
```ssh
python hybrid_cipher.py
```
## Example output
![alt text](image.png)

## Link to Codespaces
You can run this code in the codespaces ide using the below link:
https://organic-computing-machine-977j7xw4pv49397xg.github.dev/
