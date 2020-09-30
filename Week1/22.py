import math
print("Enter the length of three sides of triangle")
a = int(input())
b = int(input())
c = int(input())
halfPer = (a+b+c)/2
area = math.sqrt(halfPer*(halfPer-a)*(halfPer-b)*(halfPer-c))
print("Area =", format(round(area, 2)))