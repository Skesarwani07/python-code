
#factorial of a number
n = int(input("enter the value of number you wish to find the factorial of : "))
fact = 1
i=1
while (i<=n):
    fact*=i
    i=i+1
print (f" fatorial of {n} is : {fact}")