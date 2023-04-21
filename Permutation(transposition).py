alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))
if method == 1 or method == 2:
    m = int(input("Enter your keystream's lengths: "))
    list_for_saving = [""] * m
    keystream = input(f"Enter your keystream that contains {m} letters: ")
    new_keystream = []
    for letter in keystream:
        if letter in new_keystream:
            pass
        else:
            new_keystream.append(letter)
    l = len(new_keystream)
    sequence = list(new_keystream)
    sequence.sort()
    new_sequence = [new_keystream.index(letter) for letter in sequence]
    if method == 1:
        plaintext = input("Enter your plaintext: ")
        j = 0
        encrypted_text = []
        for i in plaintext:
            list_for_saving[j] += i
            j += 1
            if j == l:
                j = 0
        for i in range(l):
            encrypted_text.append(list_for_saving[new_sequence[i]])
        print(''.join(encrypted_text))
    elif method == 2:
        encrypted_text = input("Enter your plaintext: ")
        j = 0
        plaintext = ""
        for i in encrypted_text:
            list_for_saving[j] += i
            j += 1
            if j == l:
                j = 0
        new_list_for_saving = [list_for_saving[letters] for letters in new_sequence]
        lengths = [len(amount) for amount in new_list_for_saving]

        text = []
        x = 0
        for i in lengths:
            text.append(encrypted_text[x:x + i])
            x += i

        order = [sequence.index(letter) for letter in list(new_keystream)]
        new_text = [text[item] for item in order]
        new_text.extend([''] * 5)

        new_lengths = [len(amount) for amount in text]
        for i in range(l):
            for j in range(l):
                if i < len(new_text[j]):
                    a = new_text[j][i]
                    plaintext += a
        print(plaintext)
