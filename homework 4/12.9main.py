# Ezequiel Zapata PSID: 001863257

# part 1 program reads a list of first names and ages and outputs that list with the age incremented.
result = []

while 1:
    string = input()
    if string == "-1":
        break
    try:
        result.append([string.split(' ')[0], int(string.split(' ')[1])+1])
    except ValueError:
        result.append([string.split(' ')[0], 0])
for name, age in result:
    print(name, age)
