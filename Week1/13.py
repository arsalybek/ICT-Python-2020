penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

cents = int(input('Money in cents = '))

toonies = cents // toonie
cents = cents % toonie

loonies = cents // loonie
cents = cents % loonie

quarters = cents // quarter
cents = cents % quarter

dimes = cents // dime
cents = cents % dime

nickels = cents // nickel
cents = cents % nickel

print(str(nickels) + "nickels")
print(str(dimes) + "dimes")
print(str(quarters) + "quarters")
print(str(loonies) + "loonies")
print(str(toonies) + "toonies")