# Ezequiel Zapata PSID: 001863257

# part 1 a program that detects whether the user input is a palindrome or not.
user_input = input()
forward = 0
backward = len(user_input)-1
result = True
while forward < backward:
    if user_input[forward] == ' ':
        forward += 1
    elif user_input[backward] == ' ':
        backward -= 1
    elif user_input[forward] != user_input[backward]:
        result = False
        break
    else:
        forward += 1
        backward -= 1
if result:
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")