#to print the following series:
#54321
#5432
#543
#54
#5
n=int(input("enter a number: "));
for i  in range (1,n+1):
    for j in range (n ,i-1,-1 ):
         print(j,end="")
    print('\n')
