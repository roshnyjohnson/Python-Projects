import random
while True:
    flag=0
    print("let me think of a number between 1 and 50")
    ans=random.randint(1,50)
    mode=input("do you want 'easy' or 'difficult'?").lower()
    if mode == 'easy':
        n = 10
    elif mode == 'difficult':
        n = 5
    def guess():
        global flag
        num = int(input("Enter your guess"))
        if num==ans:
            print("you win")
            flag=1
        elif num<ans:
            print("You are thinking too low")
        elif num>ans:
            print("You are thinking too high")
    while n>0 and flag==0:
        guess()
        n=n-1
    if n==0:
        print("you loose")
        print(f"answer is {ans}")
