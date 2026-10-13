#armstrong number
n=int(input("Enter a number: "))
total=0
temp=n
power=len(str(n))
while n>0:
    digit=temp%10
    total+=digit**power
    temp=temp//10
if temp == total:
    print("Armstrong number")
else:
    print("Not an armstrong number")


#sum of digits
n=int(input("Enter a number:"))
total=0
while n >0:
    digit=n%10
    total+=digit
    n//=10
print("Total",total)