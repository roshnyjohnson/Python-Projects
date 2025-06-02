import os
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
op_dict={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}
def primary():

    a=float(input("enter the first number"))
    flag=True
    while flag:
        op = input("enter the operation\n+\n-\n*\n")
        b=float(input("enter the next number"))

        wanted=op_dict[op]
        result=wanted(a,b)

        print(result)
        ans=input(f"enter y if you want to continue with {result} \nenter n if you want to start new \n enter  x if you want to exit")
        if ans=="y":
            a = result
        elif ans=="n":
            os.system('cls')
            primary()
        else:
            exit(0)

primary()
