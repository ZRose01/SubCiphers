import cipherTools

def atbash_encrypt(plaintext_file, ciphertext_file):
    cipher_alpha = ''
    for char in cipherTools.ALPHABET:
        cipher_alpha += cipherTools.ALPHABET[-(cipherTools.ALPHABET.index(char)+1)]
    cipherTools.encode(plaintext_file, ciphertext_file, cipher_alpha)

def atbash_decrypt(plaintext_file, ciphertext_file):
    cipher_alpha = ''
    for char in cipherTools.ALPHABET[::-1]:
        cipher_alpha += cipherTools.ALPHABET[-(cipherTools.ALPHABET.index(char)+1)]
    cipherTools.decode(ciphertext_file, plaintext_file, cipher_alpha)

#atbash_encrypt('liquid.txt','ciphertext.txt')

atbash_decrypt('ciphertext.txt', 'liquid.txt')