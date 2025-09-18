import cipherTools

def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    if a < 2 or a > 25 or a % 2 == 0:
        print('Unable to encrypt.')
        return
    cipher_alpha = ''
    for char in cipherTools.ALPHABET:
        cipher_alpha += cipherTools.ALPHABET[(a * cipherTools.ALPHABET.index(char) + b) % 26]
    cipherTools.encode(plaintext_file, ciphertext_file, cipher_alpha)

def affine_decrypt(plaintext_file, ciphertext_file, a, b):
    if a < 2 or a > 25 or a % 2 == 0:
        print('Unable to decrypt.')
        return
    cipher_alpha = ''
    for char in cipherTools.ALPHABET:
        cipher_alpha += cipherTools.ALPHABET[(pow(a, -1 , 26)*(cipherTools.ALPHABET.index(char)-b) % 26)]
    cipherTools.decode(ciphertext_file, plaintext_file, cipher_alpha)

affine_encrypt('liquid.txt', 'ciphertext.txt', 5, 3)

affine_decrypt('ciphertext.txt', 'liquid.txt', 5, 3)