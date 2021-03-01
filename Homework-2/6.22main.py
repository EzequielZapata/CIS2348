# Ezequiel Zapata PSID: 001863257

# part 1 Creating a brute force linear equation solver for every value of x and y in the range -10 to 10.
def main():
    x1 = int(input())
    y1 = int(input())
    ans1 = int(input())

    x2 = int(input())
    y2 = int(input())
    ans2 = int(input())

    solution_found = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if (x1 * x) + (y1 * y) == ans1 and (x2 * x) + (y2 * y) == ans2:
                print(x, y)
                solution_found = True
    if not solution_found:
        print('No solution')


if __name__ == '__main__':
    main()