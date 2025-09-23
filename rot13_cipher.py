import cipherTools, caesar_cipher

shift = 13

def rot13_encrypt(plaintext_file, ciphertext_file):
    encode_alpha = caesar_cipher.caesar_helper(shift)
    cipherTools.encode(plaintext_file, ciphertext_file, encode_alpha)

def rot13_decrypt(plaintext_file, ciphertext_file):
    decode_alpha = caesar_cipher.caesar_helper(shift)
    cipherTools.decode(plaintext_file, ciphertext_file, decode_alpha)

rot13_encrypt('liquid.txt', 'ciphertext.txt')

rot13_decrypt('ciphertext.txt', 'decoded.txt')