d = int(input("Enter the number of DAYS: "))
h = int(input("Enter the number of HOURS: "))
m = int(input("Enter the number of MINUTES: "))
s = int(input("Enter the number of SECONDS: "))
totalSec = d*24*60*60 + h*60*60 + m*60 + s
print("Total seconds: ", totalSec)