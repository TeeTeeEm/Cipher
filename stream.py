method = int(input("Do you want to encrypt(1), Decrypt(2) or Exit (3)?: "))
if method == 1 or method == 2:
    true = True
    keystream = 5
    while true:
        keystream = int(input("Enter your keystream which contains combination of 1 and 0 only: "))
        if '1' not in str(keystream) or '0' not in str(keystream):
            pass
        else:
            true = False
    new_keystream = list(str(keystream))
    a = 0
    if method == 1:
        true = True
        plaintext = 0
        while '1' not in str(plaintext) or '0' not in str(plaintext) or len(str(plaintext)) != len(new_keystream):
            plaintext = input(
                f"Enter your plaintext that contains {len(new_keystream)} digits with combination of 1 and 0 only: ")
        new_plaintext = list(plaintext)
        encrypted_text = []
        for i in range(len(new_keystream)):
            a += int(new_plaintext[i]) + int(new_keystream[i])
            b = 9
            if a == 2:
                b = 0
            elif a == 1:
                b = 1
            elif a == 0:
                b = 0

            encrypted_text.append(str(b))
            a = 0
        print(f"Your encrypted text is: {''.join(encrypted_text)}")
    elif method == 2:
        true = True
        encrypted_text = 0
        while '1' not in str(encrypted_text) or '0' not in str(encrypted_text) or len(str(encrypted_text)) != len(new_keystream):
            encrypted_text = input(
                f"Enter your encrypted text that contains {len(new_keystream)} digits with combination of 1 and 0 only: ")
        new_encrypted_text = list(encrypted_text)
        plaintext = []
        for i in range(len(new_keystream)):
            a += int(new_encrypted_text[i]) + int(new_keystream[i])
            b = 9
            if a == 2:
                b = 0
            elif a == 1:
                b = 1
            elif a == 0:
                b = 0

            plaintext.append(str(b))
            a = 0
        print(f"Your plaintext is: {''.join(plaintext)}")
    elif method == 3:
        pass
