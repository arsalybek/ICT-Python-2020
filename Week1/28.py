t = float(11)
while t > 10:
    print("Enter valid temperature(<10): ")
    t = float(input())
s = float(4.7)
while s < 4.8:
    print("Enter valid speed(>4.8): ")
    s = float(input())
wci = 13.12 + 0.6215 * t - 11.37 * pow(s, 0.16) + 0.3965 * t * pow(s, 0.16)
print("WCI =", format(round(wci)))