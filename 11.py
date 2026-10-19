#GCD of a number
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

#find lcm of two numbers
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
lcm=max(a,b)
while True:
    if lcm%a==0 and lcm %b==0:
        break
    lcm+=1
print(lcm)