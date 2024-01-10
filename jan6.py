# i=0  
# lis=[]
# while i<=5:
#     a=int(input("enter the numbers")) 
#     pos=0 
#     for x in lis:
#         if x>a:
#             break 
#         pos+=1
#     lis.insert(pos,a) 
#     i+=1
# print(lis) 


# lis=[1,2,3,4]
# lis=[]
# for i in range(1,6):
#     lis.append(i**2) 

# lis1=[x*x for x in range(1,6) ]
# print(lis) 
# print(lis1) 
lis=[]
# string=input("enter the string").split(" ") 
# for i in string:
#     lis.append(i.upper())
# print(lis)

# upper=[x.upper() for x in input("enter the string ").split(" ")] 
# print(upper) 
# ans=0
# sum1=[ans+int(x) for x in input().split(" ")] 
# print(sum(sum1)) 
# lis=[] 
# for i in range(1,21):
#     if i%2==0 and i%3==0:
#         lis.append(i**2)
# print(lis)

# lis=[]
# def removevowels(string):
#     for i in string:
#         if i in "AEIOUaeiou":
#             continue
#         else:
#             lis.append(i.upper())  
        


# inpu=input("enter the string") 
# removevowels(inpu) 
# print(lis)
# lis=[]
# mylist=["bhopal",25,"$",43]
# for x in mylist:
#     if type(x) is int:
#         lis.append(x)
# print(lis) 
# lis=[]
# input=list(map(str,input().split(" "))) 
# for x in input:
#     if x=="the":
#         continue
#     else:
#         lis.append(len(x))
# print(lis) 

# lis=[10,3,5,2,9]
# lis.remove(max(lis)) 
# lis.remove(min(lis)) 
# print(lis)


album="Aashiqui 2",2013,"ArjtihSingh",((1,"thum hi ho"),(2,"chahum Mai"),(3,"meri Aashiqui"))
print("Title: ",album[0])  
print("Year:" ,album[1])
print("Singer:",album[2])
for i in album[3]:
    print("\tsong Number :",i[0],"song Name :",i[1])  

