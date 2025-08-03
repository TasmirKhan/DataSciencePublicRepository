from datetime import date
print("Program to count no. of days from the current date to the given date")
print("Enter the date you want to find no. of days from today in ddmmyy format")
day = int(input("Enter day in integer format"))
month = int(input("Enter month in integer format"))
year = int(input("Enter year in integer format"))

try:
    end_date = date(year,month,day)
except ValueError as e:
    print("invalid data entered!, ",e)
    exit(1)

today = date.today()
noofdays = end_date-today
print(noofdays)
