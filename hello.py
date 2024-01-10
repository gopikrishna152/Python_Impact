def calculate(number):
    for i in range(1,number+1):
        binum=bin(i)
        octnum=oct(i) 
        hexnum=hex(i)
        print(i,octnum[2:],hexnum[2:],binum[2:],sep=" ")
calculate(17)