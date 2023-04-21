alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))

if method == 1 or method == 2:
    keystream = int(input("What is your shift amount?: "))
    if keystream > 26:
        keystream %= 26
    if method == 1:
        plaintext = input("Which word?: ")
        plaintext_list = list(plaintext)
        encrypted_text = []
        for i in plaintext_list:
            x = alphabet.index(i) + keystream
            if x > 26:
                encrypted_text.append(alphabet[x % 26])
            else:
                encrypted_text.append(alphabet[x])

        print(''.join(encrypted_text))

    elif method == 2:
        encrypted_text = input("Which word?: ")
        encrypted_text_list = list(encrypted_text)
        plaintext = []
        for i in encrypted_text_list:
            x = alphabet.index(i) - keystream
            if x > 26:
                plaintext.append(alphabet[x % 26])
            else:
                plaintext.append(alphabet[x])

        print(''.join(plaintext))
elif method == 3:
    pass
