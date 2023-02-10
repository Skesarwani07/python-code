#to print the following pattern:
#1
#22
#333
#4444
#5555
n=int(input("enter a number: "));
for i  in range (1,n+1):
    for k in range (1,i+1):
        print(i, end ="")
    print("\r")
