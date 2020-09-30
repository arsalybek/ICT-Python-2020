import math

radius = int(input("Enter the radius to further calculations: "))
area = math.pi*pow(radius, 2)
volume = 4/3*math.pi*pow(radius, 3)
print("Area of a circle: ", format(round(area)))
print("Volume of a sphere: ", format(round(volume)))

