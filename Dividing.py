number1 = float(input("1:"))
number2 = float(input("2:"))

c = number1/number2

if number1 and number2 <10:
    print("Small number(s), huh?")
    input('Click enter to continue:')
else:
    input('Click enter to continue.')


print("your answer is,", c)

if c < 5:
    print("Can this number run doom?")
else:
    input(':o')




input('Click enter to exit')