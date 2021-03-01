# Ezequiel Zapata PSID: 001863257

# We will take input from the user and return date if input is in correct format, else it will ignore string.
def extract_date(date):
    correct_date = 0
    n_date = ""

    if date.find(",") != -1:
        month_day, year = date.split(',')

        if month_day.find(" ") != -1:
            month, day = month_day.split(" ")

            correct_date = 1

            day = day.strip()
            month = month.strip()
            year = year.strip()

            if month == "January":
                n_date = "1" + "/"
            elif month == "February":
                n_date = "2" + "/"
            elif month == "March":
                n_date = "3" + "/"
            elif month == "April":
                n_date = "4" + "/"
            elif month == "May":
                n_date = "5" + "/"
            elif month == "June":
                n_date = "6" + "/"
            elif month == "July":
                n_date = "7" + "/"
            elif month == "August":
                n_date = "8" + "/"
            elif month == "September":
                n_date = "9" + "/"
            elif month == "October":
                n_date = "10" + "/"
            elif month == "November":
                n_date = "11" + "/"
            elif month == "December":
                n_date = "12" + "/"
            else:
                correct_date = 0

            n_date += day + "/"

            n_date += year

    if correct_date == 1:
        return n_date
    else:
        return ""


# opening, reading, and closing the .txt file.
file = open('inputDates.txt', 'r')
file_dates = file.readlines()
file.close()

for i in range(len(file_dates) - 1):
    file_dates[i] = file_dates[i][:-1]

# main program that outputs formatted dates after the program opens and reads the inputDates.txt file.
print("inputDates.txt content:\n")
for i in file_dates:
    print(i)

print("\nOutput\n")
for i in file_dates:
    if i == '-1':
        break

    new_date = extract_date(i)

    if new_date != '':
        print(new_date)
