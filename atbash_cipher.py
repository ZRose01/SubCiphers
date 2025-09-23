import cipherTools

def atbash_encrypt(plaintext_file, ciphertext_file):
    '''
    generates an alphabet used to encrypt a message with the atbash cipher

    param plaintext_file: string of the location of file with message to be encoded
    param ciphertext_file: string of the location of file that will have encrypted message written to it
    '''
    cipher_alpha = cipherTools.ALPHABET[::-1]
    cipherTools.encode(plaintext_file, ciphertext_file, cipher_alpha)

def atbash_decrypt(ciphertext_file, plaintext_file):
    '''
    generates an alphabet used to decrypt a message with the atbash cipher

    param ciphertext_file: string of the location of file with encrypted message to be decoded
    param plaintext_file: string of the location of file in which the decoded message will be written
    '''
    cipher_alpha = cipherTools.ALPHABET[::-1]
    cipherTools.decode(ciphertext_file, plaintext_file, cipher_alpha)

#atbash_encrypt('liquid.txt','ciphertext.txt')

atbash_decrypt('ciphertext.txt', 'liquid.txt')