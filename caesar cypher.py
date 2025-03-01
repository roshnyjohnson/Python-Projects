import string
ch='y'
while(ch=='y'or ch=='Y'):
    choice=int(input("enter 1 for encription and 0 for decryption"))
    n=int(input("enter the shift value"))
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    str1=list(input("enter the string"))
    '''for i in range(len(str1)):
        str1[i]=chr(str1[i])'''

    print(str1)
    str2=[]
    for i in str1:
         if i not in alphabets:
               str2.append(i)
         else:

            x=alphabets.index(i)
            if choice==1:

                j=(x+n)% 26
                str2.append(alphabets[j])
            elif choice==0:
                if (x-n)>=0:

                    j=(x-n)%26
                    str2.append(alphabets[j])
                else:
                    j=((x-n)+26)%26
                    str2.append(alphabets[j])
            else:
                print("wrong choice")


    print("".join(str2))
    ch=input("do you want to proceed y/n")
