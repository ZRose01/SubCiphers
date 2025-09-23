import cipherTools

def caesar_encrypt(plaintext_file, ciphertext_file, shift):
    encode_alpha = caesar_helper(shift)
    cipherTools.encode(plaintext_file, ciphertext_file, encode_alpha)

def caesar_decrypt(ciphertext_file, plaintext_file, shift):
    decode_alpha = caesar_helper(shift)
    cipherTools.decode(ciphertext_file, plaintext_file, decode_alpha)

def caesar_helper(shift):
    cipher_alpha = ''
    for letter in cipherTools.ALPHABET:
        cipher_alpha += cipherTools.ALPHABET[(cipherTools.ALPHABET.index(letter) + (shift % 26)) % 26]
    return cipher_alpha

caesar_encrypt('liquid.txt', 'ciphertext.txt', -1)

caesar_decrypt('ciphertext.txt', 'decoded.txt', -1)