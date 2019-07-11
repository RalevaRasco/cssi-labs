print("Welcome to Casio Calculator!")

num1 = int(raw_input("Give me a whole number: "))
num2 = int(raw_input("Give me another whole number: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

print("Here is the sum: " + str(myAddFunction(num1, num2)))
