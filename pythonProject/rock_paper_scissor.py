import random
user_choice = int(input("Enter choice from 0,1,2: "))
computer_choice = random.randint(0,2)
rock = 0
paper = 1
scissor = 2
print(computer_choice)

if user_choice == 0 and computer_choice == 1:
    print("computer win")
elif user_choice == 1 and computer_choice == 2:
    print("computer wins")
elif user_choice == 0 and computer_choice == 2:
    print("user win")
elif user_choice == 2 and computer_choice == 0:
    print("computer wins")
elif user_choice == 1 and computer_choice == 0:
    print("user wins")
elif user_choice == 2 and computer_choice == 1:
    print("user win")
else:
    print("Game Tie")