alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))
if method == 3:
    pass
elif method == 1 or method == 2:
    keystream = input("What is your keystream (enter word)?: ").lower()
    new_keystream = []
    new_alphabet = []
    # we make it to get rid of repeating letters
    for letter in keystream:
        if letter in new_keystream:
            pass
        else:
            new_keystream.append(letter)
            new_alphabet.append(letter)
    new_keystream = ''.join(new_keystream)
    print(new_keystream)

    for letter in alphabet:
        if letter not in new_alphabet:
            new_alphabet.append(letter)
    # print(new_alphabet)
    # print(len(new_alphabet))

    if method == 1:
        plaintext = input("What is your plaintext?: ").lower()
        encrypted_text = []
        for letter in plaintext:
            encrypted_text.append(new_alphabet[alphabet.index(letter)])

        print(''.join(encrypted_text))

    elif method == 2:
        encrypted_text = input("What is your encrypted text?: ").lower()
        plaintext = []
        for letter in encrypted_text:
            plaintext.append(alphabet[new_alphabet.index(letter)])
        print(''.join(plaintext))
