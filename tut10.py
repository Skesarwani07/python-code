#to print the following series:
#54321
#4321
#321
#21
#1
n=int(input("enter a number: "));
for i  in range (n,0,-1):
    for j in range (i,0,-1):
        print (j,end=" ")
    print("\n ")