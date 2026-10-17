#count digit in a number
number=input("Enter a number:")
count=0
for num in number:
    count+=1
print("count:",count)

#count digit in a number
n=int(input("Enter a number:"))
n=abs(n)
count=0
if n==0:
    count=1
else:
    while n>0:
        digit=n %10
        n//=10
        count+=1
  
print("count:",count)

#sum of digits
n=input("Enter a number:")
total=0
for digit in n:
    total+=int(digit)
print("total:",total)


#sum of digits
n=int(input("Enter a number:"))
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print("total:",total)