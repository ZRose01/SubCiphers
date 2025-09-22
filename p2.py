import cipherTools

def encodeKeyword(cipher , toEncodeLoc = 'read.txt' , toWriteLoc = 'encoded.txt'):
    cipher = cipherTools.cleanKey(cipher + cipherTools.ALPHABET)
    print(cipher)
    cipherTools.encode(toEncodeLoc , toWriteLoc , cipher)

def decodeKeyword(cipher , toDecodeLoc = 'encoded.txt' , toWriteLoc = 'decoded.txt'):
    cipher = cipherTools.cleanKey(cipher + cipherTools.ALPHABET)
    print(cipher)
    cipherTools.decode(toDecodeLoc , toWriteLoc , cipher)

encodeKeyword('amongus')
decodeKeyword('amongus')