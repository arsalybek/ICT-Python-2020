littleCnt = int(input("Enter the number of containers holding 1 litres or less: "))
largeCnt = int(input("Enter the number of containers holding more than 1 litres:"))
amount = littleCnt*0.1 + largeCnt*0.25
print("You get " + format(round(amount, 2)) + "$ deposit back")
