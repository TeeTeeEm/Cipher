alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))

if method == 3:
    pass
elif method == 2 or method == 1:
    keystream = input("What is your keystream (enter word)?: ").lower()
    new_keystream = []
    new_alphabet = []
    for letter in keystream:
        if letter in new_keystream:
            pass
        else:
            new_keystream.append(letter)
            new_alphabet.append(letter)
    new_keystream = ''.join(new_keystream)
    print(new_keystream)
    print(new_alphabet)
    for letter in range(26):
        if alphabet[26 - letter] not in new_alphabet:
            new_alphabet.append(alphabet[26 - letter])
        letter += 1

    print(new_alphabet)
    print(len(new_alphabet))
    if method == 1:
        word = input("Which word?: ")
        encrypted_word = []
        for j in word:
            encrypted_word.append(new_alphabet[alphabet.index(j)])

        print(''.join(encrypted_word))

    elif method == 2:
        word = input("Which word?: ")
        encrypted_word = []
        for j in word:
            encrypted_word.append(alphabet[new_alphabet.index(j)])
        print(''.join(encrypted_word))
