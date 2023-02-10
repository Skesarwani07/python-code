#to check a number is armstrong or not 
n =int(input("enter a number: "))
i=n ;
d=0 ;
s=0 ;
while (i!=0):
    a=i%10;
    d+=1 ;
    s+=(a**3)
    i//=10 ;
if (s==n) :
        print(f"the number is armstrong {n} ")
else :
        print(f"the number is not armstrong :  {n} ")

