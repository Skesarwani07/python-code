#to check for a  prime number
n =int(input("enter a number: "));
c=0;
for i in range (1,n+1):
     if(n%i==0):
         c+=1;
if (c==2):
    print(f"{n} : is a prime number");
else :
    print (f"{n} : is not a prime number")


    