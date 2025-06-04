water=1500
milk=1000
coffe=500
money=0
espresso={
        "w":300,
        "m":200,
        "c":100,
        "mo":75
    }
latte={
    "w":300,
    "m":250,
    "c":200,
    "mo":100
    }
cappuccino={
    "w":400,
    "m":300,
    "c":100,
    "mo":50
    }
recipes = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino
    }
while True:
    continue_flag=True
    choice=input("what do you want espresso/latte/cappuccino").lower()


    flag=0
    if choice == "report":
        print(f"water {water}\n milk {milk}\ncoffe{coffe}\ntotal money{money}")
        continue
    selected = recipes[choice]
    def check(w,m,c):
        global flag
        if selected["w"]>water or selected["m"]>milk or selected["c"]>coffe:
            flag=1
            print("not enough resources")



    check(selected["w"],selected["m"],selected["c"])

    while flag==0 and continue_flag:

        coin_5=int(input("enter no of coin 5"))
        coin_10=int(input("enter no of coin 10"))
        coin_20=int(input("enter no of coin 20"))
        tot=(5*coin_5)+(10*coin_10)+(20*coin_20)

    #    global money
        if tot>selected["mo"] or tot==selected["mo"]:
            return_cash=tot-selected["mo"]
            money+=selected["mo"]
            print(f"balance you recieve is {return_cash}")
        else:
            print(f"not enough money refunding {tot}")
            continue
        print(f"here is your {choice}")
        water-=selected["w"]
        coffe-=selected["c"]
        milk-=selected["m"]
        continue_flag=False

