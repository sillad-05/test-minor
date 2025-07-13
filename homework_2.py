'''lst=[3,1,4,1,5,9]
print(lst[::-1])'''

'''inp=input("enter string:")
print(len(inp))'''

'''for x in range(1,11):
    print(x)'''

'''inp=input("enter string:")
cout=0
for inx in inp:
    if 'a'==inx:
        cout+=1
print(cout)'''

'''def sqr(n):
    print(n*n)

print(sqr(5))'''

'''def eo(n):
    if n%2==0:
        print("even")

    else:
        print("odd")
print(eo(6))'''


'''lst=[]

x=0
while(x<5):
    name=input("Enter name:")
    lst.append(name)
    x+=1



print(lst)'''

'''lst=[1,2,3,4,5]
print(list(map(lambda x:x**2,lst)))'''


'''lst=[1,2,3,4,5]
def m(lst):
    return max(lst)
    
print(m(lst))'''

'''dict1={"name":"alok","marks":23}
dict2={"name":"john","marks":24}
dict3={"name":"harry","marks":25}

rec={"stu1":dict1,"stu2":dict2,"stu3":dict3}

print(rec["stu1"],rec["stu2"],rec["stu3"])'''


'''inp=input("enter string:")



inp=inp.replace('a',"")
inp=inp.replace('e',"")
inp=inp.replace('i',"")
inp=inp.replace('o',"")
inp=inp.replace('u',"")


print(inp)'''

'''inp=eval(input("enter list:"))


for x in range(len(inp)):
    if inp[x]%2==0:
        print(inp[x])'''

'''dict={"item1":300,"item2":400,"item3":500}

total=dict["item1"]+dict["item3"]+dict["item2"]
print(total)'''

'''def prime(n):
    flag=False
    if n==0 or n==1:
        print("not prime")
    elif(n>2):
        for i in range(2,n+1):
            if(n%2==0):
                flag=True
                break
    if flag:
        print("not prime")
    else:
        print("prime")
prime(8)'''

'''sen=input("enter sentence:")

print(len(sen.split()))'''

