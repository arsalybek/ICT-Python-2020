def round_two_dec_places(num):
    return format(round(num, 2))


billAmount = int(input("Please, enter your restaurant bill amount: "))
tax = billAmount*0.15
tip = billAmount*0.18
overall = tax + tip + billAmount
print("Tax: " + round_two_dec_places(tax))
print("Tip: " + round_two_dec_places(tip))
print("Overall: " + round_two_dec_places(overall))



