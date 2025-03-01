import os
data={}
ch='y'
def  winner(data_input):
    high = max(data_input.values())
    for i in data_input:
        if data_input[i] == high:
            wanted = i
    print(f"the highest bid is {high} and was called by {wanted}")
while ch=='y'or ch=='Y':
    os.system('cls')
    n=input("enter a name")
    b=int(input('enter  a bid value'))
    def auction(name,bid):
        data[name]=bid
    auction(n,b)
    ch=input("do anyone want to bid again(y/n)")

if ch=='n' or ch=='N':
    print(data.values())
    winner(data)


else:
    print("wrong choice")
