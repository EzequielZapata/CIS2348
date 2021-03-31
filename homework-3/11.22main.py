# Ezequiel Zapata PSID: 001863257

# part 1 a program that reads words in a list and outputs the word and its frequency. Caps sensitive.
words = input().split()

for word in words:
    count = 0

    for w in words:
        if w == word:
            count += 1
    print(word, count)