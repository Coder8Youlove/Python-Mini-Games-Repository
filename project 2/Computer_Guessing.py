import random
n = random.randint(1 , 100)
a = -1
guesses = 0
while(a!=n):
    guesses +=1
    a = int(input("Enter a number :"))
    if(a>n):
        print("Please enter a lower number ")
    else:
        print("Please enter a higher number")

print(f"You have guessed the number {n} correctly in {guesses} attempts")       