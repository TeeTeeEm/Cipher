alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key_a_numbers = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
key_a_numbers_inverse = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]
method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))
if method == 1 or method == 2:
    print(
        "You need to enter 2 numbers for keystream with space.")
    print("1st number shouldn't be divisible for 2 or 13.\n2nd number can be any integer number.")
    key = input("Enter here: ").split()
    key_a = int(key[0])
    while key_a not in key_a_numbers:
        key_a = int(input("Your keystream value for 'a' is incorrect, enter again: "))
    key_b = int(key[1])
    print(key_a, key_b)
    if method == 1:
        plaintext = input("Please enter your word/sentence that you wish to encrypt.\nEnter without spaces: ")
        plaintext_list = list(plaintext)
        encrypted_text = [alphabet[(key_a * alphabet.index(letter) + key_b) % 26] for letter in plaintext_list]
        print(''.join(encrypted_text))
    elif method == 2:
        encrypted_text = input("Please enter your word/sentence that you wish to decrypt.\nEnter without spaces: ")
        encrypted_text_list = list(encrypted_text)
        plain_text = [
            alphabet[(key_a_numbers_inverse[key_a_numbers.index(key_a)] * (alphabet.index(letter) - key_b)) % 26] for
            letter in encrypted_text_list]
        print(''.join(plain_text))
