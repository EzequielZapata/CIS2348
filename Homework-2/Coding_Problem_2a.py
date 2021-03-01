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


# Main program that will output a date when an input is plugged in.
date = input()

while date != "-1":
    new_date = extract_date(date)

    if new_date != "":
        print(new_date)

    print()
    date = input()