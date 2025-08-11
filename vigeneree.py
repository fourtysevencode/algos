class solutuon:
    def vigenere(self, cipher: str, key: str):
        cipher = cipher.upper()
        key = key.upper()
        dec = ""
        for i, char in enumerate(cipher):
            if char.isalpha():
                p = ord(char) - ord('A')
                k = ord(key[i % len(key)]) - ord('A')
                c = (p-k) % 26
                dec += chr(c+ord('A'))
            elif char == " ":
                dec+= " "
            else:
                dec+=char
        return dec
    
solution = solutuon()

print(solution.vigenere("RIJVS UYVJN", "KEY"))