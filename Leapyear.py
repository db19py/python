year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year, "Leap year")
else:
    print(year,"Not a Leap year")
