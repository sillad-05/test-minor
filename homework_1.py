'''def length(name):
    print(len(name))
    

name=input("enter name:")
length(name)'''#1

'''def high(lst):
    print(max(lst))

lst=eval(input("enter list:"))
high(lst)'''#2

'''def s(lst):
    print(sum(lst))

lst=[12,45,23,67]
s(lst)'''#3

'''def sot(lst):
    print(sorted(lst))

lst=["venom","kevin","john","harry"]
sot(lst)'''#4

'''def tp(item):
    print(type(item))

item=eval(input("enter item:"))
tp(item)'''#5

'''def greet():
    print("good morning\n"*3)

greet()'''#6

'''def eo(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")

it=int(input("enter number:"))
eo(it)'''#7

'''def grt(a,b):
    return max(a,b)

a=int(input("enter number1: "))
b=int(input("enter number2: "))


print(f"{grt(a,b)} is greater")'''#8

'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("enter a number:"))
print(f"factorial of {num} is {fact(num)}")'''#9

'''def reve(lst):
    lst1=[]
    for x in range(-1,-len(lst)-1,-1):
        lst1.append(lst[x])
    return lst1

lste=eval(input("enter list:"))
print(reve(lste))'''#10


'''def pal(str1):
    lst=list(st1)

    tsl=lst[::-1]
    #st2=str(tsl)
    if (lst==tsl):
        print("Palindrome")
    else:
        print("Not Palindrome")
st1=input("enter string:")
pal(st1)'''#11

'''def vow(str):
    counter=0
    for x in range(len(str)):
        if 'a' in str[x]:
            counter+=1
        elif 'e' in str[x]:
            counter+=1
        elif 'i' in str[x]:
            counter+=1
        elif 'o' in str[x]:
            counter+=1

        elif 'u' in str[x]:
            counter+=1
    return counter

st=input('entre string:')
print(vow(st))'''#12

''''def even(lst):
    le=[]
    for x in range(len(lst)):
        if lst[x]%2==0:
            le.append(lst[x])
    return le
lst=eval(input("enter list:")) 
print(even(lst))'''#13

'''def mma(lst):
    print(f"max:{max(lst)}")
    print(f"min:{min(lst)}")
    print(f"average:{sum(lst)/len(lst)}")
lst=eval(input("enter a list"))
mma(lst)'''#14

'''def greet(lst):
    for x in range(len(lst)):
        print(f"Hello!! {lst[x]}")

lst=["ben",'harry','john','kevin','tyson']
greet(lst)'''#15

    
    









        


        




        
    
