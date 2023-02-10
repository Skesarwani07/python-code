#to print the sum of digits of a number 
n =int(input("enter a number: "))
sum=0;
i=n;
d=0;
while (i!=0):
    a=i%10;
    sum+=a;
    i//=10;
    d+=1;
print(f"the sum of digits is of {n} is {sum}");
print(f"the no. of digits : {d}");


