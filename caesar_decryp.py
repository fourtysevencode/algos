def bruteforce(text):
    for shift in range(1,26):
        final = ""
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord('a')
                final += chr((ord(char) - base + shift)%26 + base)
            else:
                continue
        print(f"{shift}. {final}")

bruteforce(input("> "))
