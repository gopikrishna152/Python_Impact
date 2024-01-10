# a=11
# flag=lambda a:a%2==0
# print(flag(a)) 
# print((lambda a,b:a+b)(2,3)) 
# import math  
# sqr=lambda a:math.sqrt(a)
# print(sqr(25))
# print(sqr(10)) 


# first=lambda s:s[-1]
# print(first("gopi")) 



# b=int(input("enter the number"))
# check=lambda a: a%2==0
# print(check(b)) 
# a=int(input("enter the number a ")) 
# b=int(input("enter the number b "))
# check=lambda a,b:a>b
# if(check(a,b)):
#     print("a is greater",a)
# else:
#     print("b is greater",b) 
# check =lambda a,b: a if a>b else b 
# print(f"max among {a} and {b} is",check(a,b))

# the first 

# a=list(map(int,input().split())) 
# print(a)  


# def square(x):
#     return x**2
# a=[1,2,3,4,5]
# list1=list(map(square,a)) 
# print(list1)
# for item in list:
#     print(item)


# def inspect(month):
#     if(len(month)%2==0):
#         return "EVEN"
#     else:
#         return month[0]
# inp=["january","february","march"]
# list1=list(map(inspect,inp)) 
# print(list1) 

# lis=[1,4,2,5,8,6] 


# def fun(num):
#     return num%2==0
# ans=list(filter(fun,lis)) 
# print(ans) 


# fun=lambda num:num**2
# lis=[1,2,3,4,5] 
# ans=list(map(fun,lis)) 
# print(ans)

# inp=["january","february","march"] 
# print(list(map(lambda x:x[0],["january","february","march"]))) 
# print(list(map(lambda x:"Even" if len(x)%2==0 else x[0],["january","february","march"]))) 
# print(list(filter(lambda x:True if len(x)%2==0 else False,["january","february","march"]))) 
# b=input("Enter the name")
# vowels=['a','e','i','o','u'] .
# gk=[]
# ans1=list(map(lambda a:gk.append(a) if a in vowels else None,b)) 

# # ans=list(filter(lambda x:  x in vowels,a))
# # if(len(ans)==0):
# #     print("No vowels in name") 
# # else:
# #     print(ans) 
# print(gk)


# a=[10,20,30,40] 
# i=len(a)
# n=0 
# for num in range(i-1,-1,-1):
#     print(a[num])  

# lis=[] 
# sum=0
# for i in range(5):
#     a=int(input(f"enter the {i+1} element")) 
#     sum+=a   
#     lis.append(a)
# print("The list is:")
# for ele in lis:
#     print(ele)
# print("The sum is",sum) 

lis1=[]  
i=0
while i<5:
    a=int(input("enter the number for list 1")) 
    if a in lis1:
        print("element already present")
    else:
        lis1.append(a) 
        i+=1
print("The integers inputted are  ",lis1) 

lis2=[]  
i=0
while i<5:
    a=int(input("enter the number for list 2")) 
    if a in lis2:
        print("element already present")
    else:
        lis2.append(a) 
        i+=1
print("the list 2 is",lis2)

count=0 
common=[]
for i in lis1:
    if i in lis2:
        common.append(i)

print("the elements common in the both list are",count)
