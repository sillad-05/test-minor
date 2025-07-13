
# n1=float(input("enter num1: "))
# n2=float(input("enter num2: "))
# s=input("enter operator(+,-,/,*,%): ")

# if(s=="+"):
#     print(n1+n2)
# elif(s=="-"):
#     print(n1-n2)
# elif(s=="*"):
#     print(n1*n2)
# elif(s=="/"):
#     print(n1/n2)
# elif(s=="%"):
#     print(n1%n2)
# else:
#     print("error")

'''num=50
attempt=0
while(True):
    a=int(input("enter a no: "))
    attempt+=1
    if(a==num):
        print("correct ,you took",attempt,"attempts")
        break
    else:
        diff=a-num
        if(diff>0):
            if(diff>10):
                print("too far")
            else:
                print("too close")
        elif(diff<0):
            if(num-a>10):
                print("too far")
            else:
                print("too close")'''

num=50
while(True):
    a=int(input("enter a no: "))
    if(a==num):
        print("correct")
        break
    else:
        dif=a-num
        if(dif>num+10 or dif<num-10):
            print("too close")

        elif(dif>num+40 or dif<num-40):
            print("too far")








