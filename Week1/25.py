def count_digit(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

s = int(input("Enter a time in seconds: "))
d = 0
h = 0
m = 0
if s > 60:
    m = int(s / 60)
    s = s % 60
    if m > 60:
        h = int(m / 60)
        m = m % 60
    if h > 24:
        d = int(h / 24)
        h = h % 24
if count_digit(s) == 1 or s == 0:
    s = "0"+str(s)
if count_digit(m) == 1 or m == 0:
    m = "0"+str(m)
if count_digit(d) == 1 or d == 0:
    d = "0"+str(d)
if count_digit(h) == 1 or h == 0:
    h = "0"+str(h)

print(str(d) + ":" + str(h) + ":" + str(m) + ":" + str(s))