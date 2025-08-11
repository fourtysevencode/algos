def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += char
    return ciphertext
