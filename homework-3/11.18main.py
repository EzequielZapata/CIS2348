# Ezequiel Zapata PSID: 001863257

# part 1 a program that filter and sorts a list of numbers from lowest to highest
integers = input().split()
non_neg_int = []

for num in integers:
    num = int(num)

    if num >= 0:
        non_neg_int.append(num)

non_neg_int.sort()

for i in non_neg_int:
    print(i, end=' ')