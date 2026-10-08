#fibonacci series
n=int(input("Enter a number of terms:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#reverse a number
n=int(input("Enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)