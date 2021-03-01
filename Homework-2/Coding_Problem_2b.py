# Ezequiel Zapata PSID: 001863257

# We will take input from the user and return date if input date is in correct format, else will return empty string
def extract_date(date):
    correct_date = 0
    new_date = ""
    if date.find(",") != -1:
        month_day, year = date.split(',')
        if month_day.find(" ") != -1:
            month, day = month_day.split(" ")

            correct_date = 1

            day = day.strip()
            month = month.strip()
            year = year.strip()

            # We'll start new date format from here
            # Adding month to the new_date
            if month == "January":
                new_date = "1" + "/"
            elif month == "February":
                new_date = "2" + "/"
            elif month == "March":
                new_date = "3" + "/"
            elif month == "April":
                new_date = "4" + "/"
            elif month == "May":
                new_date = "5" + "/"
            elif month == "June":
                new_date = "6" + "/"
            elif month == "July":
                new_date = "7" + "/"
            elif month == "August":
                new_date = "8" + "/"
            elif month == "September":
                new_date = "9" + "/"
            elif month == "October":
                new_date = "10" + "/"
            elif month == "November":
                new_date = "11" + "/"
            elif month == "December":
                new_date = "12" + "/"
            else:
                correct_date = 0

            new_date += day + "/"

            new_date += year

    if correct_date == 1:
        return new_date
    else:
        return ""


# opening, reading, and closing the .txt document.
file = open('inputDates.txt', 'r')
file_dates = []
file_dates = file.readlines()
file.close()

for i in range(len(file_dates)-1):
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