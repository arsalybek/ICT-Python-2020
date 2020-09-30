l = []
for i in range(3):
    l.append(int(input()))
s = [min(l), sum(l) - max(l) - min(l), max(l)]
print(s)
