print("Welcome to Pluralizer!")
num1 = int(raw_input("Please Enter a number: "))

word1 = (raw_input("Please Enter a word: "))
if num1>1 or num1 <= 0:
    print(str(num1) + " " + word1 + "s")

else: print(str(num1) + " " + word1)
