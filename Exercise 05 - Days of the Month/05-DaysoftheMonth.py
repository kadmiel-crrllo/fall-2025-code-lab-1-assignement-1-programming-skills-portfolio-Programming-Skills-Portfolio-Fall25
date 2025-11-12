# make a dictionary with month numbers and how many days each has
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# ask the user which month they want (1 to 12)
month = int(input("Enter month number (1-12): "))

# check if the month number is valid
if month >= 1 and month <= 12:
    # handle February separately since it can have 28 or 29 days
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ")
        if leap_year.lower() == "yes":
            print("29 days")
        else:
            print("28 days")
    # for all other months, just print days from the dictionary
    else:
        print(f"{month_days[month]} days")
# if user enters something out of range
else:
    print("Invalid month number")
