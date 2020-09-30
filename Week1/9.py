def round_two_dec_places(num):
    return format(round(num, 2))


amount = int(input("Please, enter amount of money you put in deposit: "))
firstYear = amount*1.04
secondYear = firstYear*1.04
thirdYear = secondYear*1.04
print("First year: " + round_two_dec_places(firstYear))
print("Second year: " + round_two_dec_places(secondYear))
print("Third year: " + round_two_dec_places(thirdYear))