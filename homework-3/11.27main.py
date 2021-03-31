# Ezequiel Zapata PSID: 001863257

# part 1 this program will store roster and rating info for soccer teams. It will prompt the user to input jersey
# numbers from 0-99 and the players rating from 1-9. Storing them in a dictionary and it will output in ascending
# order.

# first we create the menu
def menu():
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    return input("\nChoose an option:")

# now we create the roster and their jersey numbers and output them in ascending order


def printRoster(roster, numbers):
    print('ROSTER')

    for num in numbers:
        print("Jersey number: %d, Rating: %d" %(num, roster[num]))


if __name__ == "__main__":
    roster = dict()
    numbers = list()

    for i in range(1, 6):
        print("Enter player {}'s jersey number:".format(i))
        number = int(input())
        print("Enter player {}'s rating:".format(i))
        roster[number] = int(input())
        print()

    numbers = sorted(roster.keys())
    printRoster(roster, numbers)

    while True:
        op = menu()
        print()
        if op == 'a':
            print("Enter a new player's jersey number:")
            number = int(input())
            print("Enter the player's rating:")
            roster[number] = int(input())
            numbers = sorted(roster.keys())

        elif op == 'd':
            print("Enter a jersey number:")
            number = int(input())
            if number in numbers:
                del roster[number]
                numbers.remove(number)

        elif op == 'u':
            print("Enter a jersey number:")
            number = int(input())
            if number in numbers:
                print("Enter a new rating for player:")
                roster[number] = int(input())
            else:
                print("Jersey Not Found")

        elif op == 'r':
            print("Enter a rating:")
            rating = int(input())
            print("\nABOVE", rating)
            for number in numbers:
                if roster[number] > rating:
                    print("Jersey number: %d, Rating: %d" %(number, roster[number]))

        elif op == 'o':
            printRoster(roster, numbers)

        elif op == 'q':
            break