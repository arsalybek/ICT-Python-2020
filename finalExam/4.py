n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0
res = ""
if n != 1:
    i = arr[1]
for i in range(1, n):
    if arr[i] == 1:
        cnt += 1
        res += str(arr[i-1]) + " "
res += str(arr[n - 1])
print(cnt + 1)
print(res)
    
    