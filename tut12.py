#to print the following series:
#*****
#****
#***
#**
#*
n=int(input("enter the value of n : "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*  ",end="")
    print("\n")