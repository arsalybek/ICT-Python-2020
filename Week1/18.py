import math

print("Cylinder dimensions")
r = int(input("Radius: "))
h = int(input("Height: "))
volume = math.pi*pow(r, 2)*h
print("Volume: ", format(round(volume, 1)))