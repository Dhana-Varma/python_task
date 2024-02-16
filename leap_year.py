# Python program to check the leap year

def checkyear(year):
    return((( year % 4==0) and (year % 100 !=0)) or (year%400==0))
year = 2000
if (checkyear(year)):
    print('leap year')
else:
    print('not a leap year')
