# Ezequiel Zapata PSID: 001863257

# part 1 we must define exact change for whatever the user inputs to return in dollars, quarters, dimes, nickels, and pennies.
def exact_change(user_input):
    dollars = user_input // 100
    user_input %= 100

    quarters = user_input // 25
    user_input %= 25

    dimes = user_input // 10
    user_input %= 10

    nickels = user_input // 5
    user_input %= 5

    pennies = user_input
    return dollars, quarters, dimes, nickels, pennies


# part 2 Now we define main() to execute the program to display the user integer in the proper coin types.


def main():
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies, = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if num_dollars > 1:
            print(num_dollars, 'dollars')
        elif num_dollars == 1:
            print('1 dollar')

        if num_quarters > 1:
            print(num_quarters, 'quarters')
        elif num_quarters == 1:
            print('1 quarter')

        if num_dimes > 1:
            print(num_dimes, 'dimes')
        elif num_dimes == 1:
            print('1 dime')

        if num_nickels > 1:
            print(num_nickels, 'nickels')
        elif num_nickels == 1:
            print('1 nickel')

        if num_pennies > 1:
            print(num_pennies, 'pennies')
        elif num_pennies == 1:
            print('1 penny')


if __name__ == '__main__':
    main()    