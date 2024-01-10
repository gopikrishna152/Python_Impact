# text=input("enter the string") 
# word1,word2,word3=text.split() 
# print(word1) 
# print(word2) 
# print(word3) 


# inp=input("enter the 2 numebrs with space") 
# a,b=inp.split()

# print(int(a)+int(b))  
 



# w=list(map(int,input("enter the number").split())) 
# print(w) 

# s=input("enter the roll no,name,per") 
# roll,name,per=s.split("$") 
# print("Roll no is ",roll) 
# print("Name is ",name) 
# print("per is ",per) 


#using the eval 
# s=eval(input("enter the string ")) 
# print(s) 
# 
# 
#   
# from sys import argv 
# print(argv[1])




# print(argv[1]) 
# print(argv[2]) 


# a=10
# msg="hello" 
# f=10.32
# print("values are %f %s %f"%(a,msg,f))  
# print(type(a))  


# a=ord(input("enter the charcter  "))   
# # print(a)

# if a>=65 and a<92:
#     print("it is Capital")
# elif a>=97 and a<122:
#     print("small")  
# elif a>=48 and a<=57:
#     print("it is numebr")
# else:
#     print("it is a symbol") 

# a=int(input("enter the number")) 
# b=int(input("enter the number")) 
# c=int(input("enter the number"))  


# a=int(input("enter the number")) 
# if a%100==0:
#     if a%400==0:
#         print("leap year")
#     else:
#         print("not leap year") 
        
# elif(a%4==0):
#     print("leap year")
# else:
#     print("not leap year")        

class emp:
    def __init__(self):
        self.name="abc"
        self.age=20
        self.salary=20000
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("salary is ",self.salary) 
obj=emp()
print(obj.__dict__)
obj.__dict__["Department"]="IT" 
print(obj.__dict__) 
e1.display()
del obj.__dict__['age']
e1.display()














    







