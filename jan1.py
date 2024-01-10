# import random
# a=random.randint(1,10)   
# print(a)

# while(True): 
#     user=int(input("enter the number "))
#     if(user==a): 
#         print("congrats you guessed the answer ") 
#         break
#     elif user<a:
#         print("input is low please enter high") 
#     else: 
#         print("input is high please enter low") 
 


# a=input("enter the string  ")  
# b=len(a) 
# lis=['a','e','i','o','u','A','E','I','O','U']
# for i in a:
#     if i in lis:
#         continue
#     else:
#         print(i) 


# # lis=[]
# sum=0
# while(True):
#     a=int(input("enter an integer(press 0 to stop)")) 
#     if(a==0):
#         break 
#     elif a<0:
#         continue
#     else:
#         # lis.append(a)
#         sum+=a 
# # print("sum is ",sum(lis)) 
# print("sum is ",sum)

# a="gopikrishna" 
# for i in a:
#     print(i,end="  ")

# lis=["gopi",32,5.0]
# for i in lis:
#     print(i)

# for i in range(0,20,2):
#     print(i) 

# i=1
# while True:
#     if i%3==0:
#            break
#     print(i,end=" ")
#     i+=1


# x="abcd"  

# # print(x)
# for i in x:
#        print(i,end=" ")  
#        x=x.upper() 
#        print(x)
       


# a=range(5,10,0)
# b=list(a) 
# print(b)

#     a=range(5,10,0)
#       ^^^^^^^^^^^^^
# ValueError: rcange() arg 3 must not be zero

# a=int(input("enter the number")) 
# sum=0
# for i in range(1,a+1):
#        sum+=i 
# # print("sum of nos from 1 to {0} is {1}".format(a,sum))
# print(f"the sum of nos from 1 to {a} is {sum}") 

# import math
# a=int(input("enter the numebr")) 
# print(math.factorial(a)) 


# a=int(input("enter the rows")) 
# b=int(input("eneter the columns")) 
# for i in range(a):
       
#        for j in range(b):
#               print("*",end=" ")
#        print()

# for i in range(1,5):
#        print("*"*3)



# a=int(input("enter the rows")) 
# b=int(input("eneter the columns")) 
# for i in range(1,a+1):
#        for j in range(1,i+1):
#               print("*",end="") 
#        print() 


# for i in range(4,0,-1):
#        for j in range(1,i+1):
#               print("*",end=" ")
#        print()



# while True:
#        a=int(input("enter the number"))
#        if(a==0):
#               print("quitting")
#               break
#        else:
#               for i in range(1,a+1):
#                      print(i) 


# for i in range(4,0,-1):
       

#        for i in range(1,5): 
#               print("1",end="")
#        # for j in range(5,0,-1): 
#        print()  


# def absolute(a):
#        print("absolute of",a,"is",abs(a))  
       
# absolute(-7)
                

# def factorial(n):
#        if n==1:
#               return 1
#        return factorial(n-1)*n
# print(factorial(4)) 


# def greet(name):
#        print(name)
# x=greet("gopi")
# print("value in x is ",x)
# print(type(x))  


# def fun(a,):
#        return 1,2
# z=fun() 
# print(z) 

# def area(radius,pi=3.14):
#        return pi*(radius**2)
# a=int(input("enter the radius")) 
# print(area(a))
# def ad(a,b,c):
#        return a+b+c 

# def ad(a,b):
#        return a+b
# # def ad(a,b,c):
# #        return a+b+c 
# print(ad(2,3)) 
# print(ad(1,2,3)) 


def find_largest(*x):
       max=0 

       for i in x:
              if(len(i)>max):
                     max=len(i)
                     maxstr=i
       return max
print(find_largest("gopi","sai","hello"))
