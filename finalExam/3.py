n = int(input())
arr = []
for x in range(n):
    arr.append([int(i) for i in input().split()])
for x in arr:
    if x[0] % x[1] == 0:
        print("YES")
    else:
        print("NO")  