alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))
if method == 1 or method == 2:
    m = int(input("Enter your keystream's lengths: "))
    keystream = input(f"Enter your keystream that contains {m} letters: ")
    if method == 1:
        plaintext = input("Enter your plaintext: ")
        plaintext_list = list(plaintext)
        encrypted_text = []
        j = 0
        for letter in plaintext_list:
            new_letter = alphabet.index(letter) + alphabet.index(keystream[j])
            if new_letter > 25:
                new_letter %= 26
            encrypted_text.append(alphabet[new_letter])
            j += 1
            if j == m:
                j = 0
        print(''.join(encrypted_text))
    elif method == 2:
        encrypted_text = input("Enter your encrypted text: ")
        encrypted_text_list = list(encrypted_text)
        plaintext = []
        j = 0
        for letter in encrypted_text_list:
            new_letter = alphabet.index(letter) - alphabet.index(keystream[j])
            if new_letter < 0:
                new_letter += 26
            plaintext.append(alphabet[new_letter])
            j += 1
            if j == m:
                j = 0
        print(''.join(plaintext))
