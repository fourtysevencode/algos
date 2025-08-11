def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ''
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')
            p = (c - k) % 26              # <<== here we subtract!
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char
    return plaintext
