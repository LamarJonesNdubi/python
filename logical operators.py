# logical operators = used on conditional statements

#               and = checks two or more conditions if True
#               or = checks if at least one condition is True
#               not = True if condition is False, and vice versa


temp = float(input("Enter current Temperature: "))
sunny = bool(input("Is it sunny?: "))

if temp > 0 and temp <30:
    print("The temperature is good:)")
else:
    print("The temperature is bad:( ")

if sunny:
    print("it is sunny")
else:
    print("It is cloudy")


