start_year = int(input("Enter current year: "))
final_year = int(input("Enter final year: "))

for year in range(start_year, final_year + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
