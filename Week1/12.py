import math

t1, g1 = input("Enter a latitude values: ").split()
t2, g2 = input("Enter a longitude values: ").split()
t1 = math.radians(int(t1))
t2 = math.radians(int(t2))
g1 = math.radians(int(g1))
g2 = math.radians(int(g2))
distance = 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("Distance between the points: ", distance)