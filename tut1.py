#series= 1+x**1/1!+x**2/2!+x**3/3!+...............x**n/n!
x=int(input("enter the  value of X: "))
n=int(input("enter the  limit of X: "))
for i in range(0,n+1):
    fact= 1
    s = 0 
    for k in range(1,i+1):
        fact*=k;
        s+=(x**i)/fact ;
print(s);
