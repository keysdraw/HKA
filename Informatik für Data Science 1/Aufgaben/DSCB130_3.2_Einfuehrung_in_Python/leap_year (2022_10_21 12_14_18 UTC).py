# Python program to check if the input year is a leap year or not
# Beispielprogramm, ob ein bestimmtes Jahr, ein Schaltjahr ist oder nicht

year = 2022

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
           # if block of 400
           print("{0} is a leap year".format(year))
        else:
           # else block of 400
           print("{0} is not a leap year".format(year))
    else:
       # else block of 100
       print("{0} is a leap year".format(year))
else:
   # else block of 4
   print("{0} is not a leap year".format(year))
    