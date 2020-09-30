n = int(input("Enter the number of loaves of day-old bread: "))
reg = n * 3.49
discount = reg * 0.6
total = reg - discount
print("Regular price:", format(round(reg, 2)))
print("Discount:", format(round(discount, 2)))
print("Total price:", format(round(total, 2)))
