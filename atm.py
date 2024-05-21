def passcheck(x):
    u=[0,0,0,0]
    for i in x:
        if(i.isupper()):
            u[0]=1
        elif(i.islower()):
            u[1]=1
        elif(i.isdigit()):
            u[2]=1
        else:
            u[3]=1
    z=4-sum(u)
    k=max(z,8-len(x))
    if(k==0):
        print("pasword updated")
    else:
        print("please update your password it is too weak")
        print("add the number of chareccters to make it stronger")
        print(k)
name=['divya','jash','mahesh','ish']
pas=['D','J','M','I']
pin=[8055,1703,7788,2233]
balance=[2025,2022,2033,2000]
a=input("enter your username:")
if(a not in name):
    print("invalid username")
    exit()
else:
    c=input("enter your password:")
    f=0
    if(c==pas[name.index(a)]):
        f=1
    else:
        print("incorrect password","more 2 Attempts")
        c=input()
        if(c==pas[name.index(a)]):
            f=1
        else:
            print("incorrect password","more 1 Attempts")
            c=input()
            if(c==pas[name.index(a)]):
                f=1
            else:
                print("incorrect password,Account Blocked!!!")
                exit()
b=int(input("enter your pin:"))
if(b==pin[name.index(a)]):
    print("choose one")
    print("1.withdrawal")
    print("2.deposite")
    print("3.balance")
    print("4.change password")
else:
    print("invalid pin")
k=int(input())
if(k==1):#withdrawal
    x=int(input("enter your pin"))
    if(x==pin[name.index(a)]):
        s=int(input("enter amount to withdraw"))
        if(s<balance[name.index(a)]):
            s=balance[name.index(a)]-s
            print("available balance:",end=' ')
            print(s)
        else:
            print("insufficient balance")
    else:
        print("incorrect pin")
        exit()
elif(k==2):#deposite
    s=int(input("enter amount to deposite"))
    x=int(input("enter your pin"))
    if(x==pin[name.index(a)]):
        s=balance[name.index(a)]+s
        print("available balance:",end=' ')
        print(s)
    else:
        print("incorrect pin")
        exit()
elif(k==3):#Balance
    print("available balance:",end=' ')
    print(balance[name.index(a)])
elif(k==4):#change password
    l=input("enter your current password")
    if(l==pas[name.index(a)]):
        while(1):
            w=input("enter your new password")
            z=input("Re-enter your new password")
            if(w==z):#password check
                passcheck(w)
                break
            else:
                print("passwords not matched, RE-enter the passwords")
else:
    print("please enter choice from 1-4 only")