#to print the following series:
#A
#BC
#DEF
#GHIJ
#KLMNO
n=65
i=1
while (i<=5):
    j=1 ;
    while(j<=i):
        print(chr(n), end="")
        j+=1
        n+=1 ;
    print("\n")
    i+=1;