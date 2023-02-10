#to check for a perfect number
n =int(input("enter a number: "));
p=0 ;
for i in range (1 , n):
    if (n%i == 0):
       p+=i ;
if(p==n):
     print (f"{n} : is a perfect number");
else:
    print (f"{n} : is a  not perfect number");
