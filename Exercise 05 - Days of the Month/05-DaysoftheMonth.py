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

month = int(input("Enter month number (1-12): "))

if month >= 1 and month <= 12:
    if month == 2:
        
        leap_year = input("Is it a leap year? (yes/no): ")
        if leap_year.lower() == "yes":
            print("29 days")
        else:
            print("28 days")
    else:
        print(f"{month_days[month]} days")
else:
    print("Invalid month number")