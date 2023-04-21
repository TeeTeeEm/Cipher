true = True
while true:

    key = int(input("Enter a number: "))
    if key > 0 and key % 2 != 0:
        true = False

y = 27
while y % key != 0:
    y += 26
answer = y // key

print(answer)
