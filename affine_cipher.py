affine = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
spec_char = [' ', '\'', ',', '\n']

def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    if (a > 1) and (a < 26) and (a % 2 == 1):
        with open('liquid.txt', 'r') as plaintext:
            with open('affine_cipher.txt', 'w') as ciphertext:
                encrypted = ''
                for line in plaintext:
                    for char in line:
                        if char in spec_char:
                            encrypted += char
                        else:
                            encrypted += affine[(a * affine.index(char.upper()) + b) % 26]
                ciphertext.writelines(encrypted)
        ciphertext.close(), plaintext.close()
    else:
        print('Unable to encrypt.')

def affine_decrypt(ciphertext_file, plaintext_file, a, b):
    if (a > 1) and (a < 26) and (a % 2 == 1):
        with open('liquid.txt', 'r') as ciphertext:
            with open('affine_cipher.txt', 'w') as plaintext:
                decrypted = ''
                for line in ciphertext:
                    for char in line:
                        if char in spec_char:
                            decrypted += char
                        else:
                            decrypted += affine[(pow(a, -1 , 26)*(affine.index(char.upper())-b) % 26)]
                plaintext.writelines(decrypted)
        plaintext.close(), ciphertext.close()
    else:
        print('Unable to decrypt.')

affine_encrypt('liquid.txt', 'affine_cipher.txt', 5, 3)