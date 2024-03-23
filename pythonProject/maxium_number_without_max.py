# find maximum number from the list without using max
number = input("Enter number: ")
number_list = number.split()

count = 0
for n in number_list:
    count += 1
for i in range(count):
    number_list[i] = int(number_list[i])

maximum_number = number_list[0]
for number in number_list:
    if number > maximum_number:
        maximum_number = number
print(maximum_number)
