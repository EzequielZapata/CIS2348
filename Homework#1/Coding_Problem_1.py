# Ezequiel Zapata PSID: 001863257

# Coding problem 1

from datetime import date


def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


print("Birthday Calculator")
print('current Day')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
print('Birthday')
birthmonth = int(input('Month: '))
birthday = int(input('Day: '))
birthyear = int(input('Year: '))
print("You are ", calculateAge(date(year, month, day), date(birthyear, birthmonth, birthday)), "years old.")
if day == birthday:
    print("Happy Birthday!")
