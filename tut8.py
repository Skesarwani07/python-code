#to print the following series:
#12345
#12345
#12345
#12345
#12345
n=int(input("enter a number: "));
for i  in range (1,n+1):
    for j in range (1,n+1):
        print(j,end="")
    print('\n')