n = int(input())
a = []
summa = 0
cnt = 0
for i in range(0, n):
    a.append([int(j) for j in input().split(" ")])
for i in range(3):
    for j in range(n):
        summa += a[j][i]
    if summa == 0:
        cnt += 1
if cnt == 3:
    print("YES")
else:
    print("NO")
