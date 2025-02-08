year=input("enter the year:")

if not (year.isdigit() and len(year)== 4):
    print("enter the valid four digiit number")
else:
    year=int(year)
    if (year % 4 == 0 and year% 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year") 