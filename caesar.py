def brute(word):
    for shift in range(1,26):
        ans= []
        for char in word:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                ans.append(chr((ord(char) - base + shift)%26 + base))
            elif char =="":
                ans.append(" ")
            else:
                continue
        print(f"shift {shift} | {"".join(ans)} ")

brute("bcd")