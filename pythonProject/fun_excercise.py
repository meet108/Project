# import math
# def paint_calculation(height, width, cover):
#     area = height * width
#     #no_of_cans = round(area/cover)
#     no_of_cans = math.ceil(area / cover)
#     print(f"You will need {no_of_cans} cans of paint")
# h = int(input("Enter height: "))
# w = int(input("Enter width: "))
# coverage = 7
# paint_calculation(width=w, height=h, cover=coverage)


import math
def check_prime(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, math.ceil(number/2)+1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("Its a prime number")
    else:
        print("Not a prime number")

n = int(input("Enter a number: "))
check_prime(n)
