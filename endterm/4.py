n, val = input().split(" ")
a = []
for i in range(int(n)):
    a.append([])
    for j in range(int(n)):
        a[i].append((i+1)*(j+1))

print(sum([i.count(int(val)) for i in a]))
