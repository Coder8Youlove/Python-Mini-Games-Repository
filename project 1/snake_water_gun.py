import random
'''
1 = snake
2 = water 
3 = gun
'''

computer = random.choice([1 , 2 , 3])
youstr = input("Enter your choice :")
youdict = {"s": 1 , "w":2 , "g": 3 }
reversedict = {1 : "Snake" , 2 :" Water" , 3 : "Gun"}

you = youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")


if(computer == you):
    print("This is a Draw!")
else:
    if(computer == 1 and you == 2):
        print("You lose ")
    elif(computer == 2 and you == 1):
        print("You win!")
    elif(computer ==1 and you == 3):
        print("You win!")
    elif(computer == 3 and you == 1):
        print("You lose!")
    elif(computer == 2 and you == 3):
        print("You lose!")
    elif(computer == 3 and you == 2):
        print("You win!")
    else:
        print("There is something wrong")


