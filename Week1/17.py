mass = int(input("Mass: "))
temp = int(input("Temperature: "))
energy = mass*temp*4186
bill = energy*8.9*1/3600000
print("Energy(J): ", energy)
print("Bill amount(cents): ", format(round(bill, 2)))