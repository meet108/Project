# import random
# lst = []
# n = int(input("Enter a number for names: "))
# for i in range(0,n):
#     name = input("enter name: ")
#     lst.append(name)
#     random.random(lst)
#     if name in random:
#         print(f"{name} have to pay bill")
# print(lst)

import random

names = input("ENter names: ")
names_list = names.split(",")
length = len(names_list)
# random_choice = random.randint(0, length-1)
person_selected = (random.choice(names_list))
print(f"{person_selected} will pay the bill")
