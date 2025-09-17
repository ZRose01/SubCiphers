def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    if a < 1 or a > 25 or a % 2 == 0 or a == 1:
        print('Unable to encrypt.')
        return
    encrypted = ''
    for char in alpha:
        encrypted += alpha[(a * alpha.index(char.upper()) + b) % 26]
    return encrypted

def affine_decrypt(plaintext_file, ciphertext_file, a, b):
    if a < 1 or a > 25 or a % 2 == 0 or a == 1:
        print('Unable to decrypt.')
        return
    encrypted = ''
    for char in alpha:
        encrypted += alpha[(pow(a, -1 , 26)*(alpha.index(char.upper())-b) % 26)]
    return encrypted