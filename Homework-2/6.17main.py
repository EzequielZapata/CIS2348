# Ezequiel Zapata PSID: 001863257

# part 1 taking a simple user created password and making it stronger by replacing some characters with the given characters.
password = input()
strong_password = ''

i = 0
while i < len(password):
    char = password[i]
    if char == 'i':
        strong_password += '!'
    elif char == 'a':
        strong_password += '@'
    elif char == 'm':
        strong_password += 'M'
    elif char == 'B':
        strong_password += '8'
    elif char == 'o':
        strong_password += '.'
    else:
        strong_password += char
    i += 1

strong_password += 'q*s'

print(strong_password)