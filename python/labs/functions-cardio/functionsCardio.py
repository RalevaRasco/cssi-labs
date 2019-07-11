print("Welcome to Functions Cardio!")

# num1 = int(raw_input("Give me side 1 length: "))
# num2 = int(raw_input("Give me side 2 length: "))
# num3 = int(raw_input("Give me side 3 length: "))
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2
#     sum2 = s2 + s3
#     sum3 = s3 + s1
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("You gotta triangle!")
#         return True #I have traingle!
#     else:
#         print("No triangle!")
#         return False #Not a triangle!
#
# (is_triangle(num1, num2, num3))

usersWord = raw_input("Give me a word: ")
def reverse_string(x):
    return x[::-1]

print("Here's your word backwords: " + reverse_string(usersWord))
