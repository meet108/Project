lst = input("Enter heights: ")
height_list = lst.split(",")
# length = len(height_list)
count = 0
for height in height_list:
    count += 1
for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total += person
average = total / count
print("Average Height is:", round(average))
