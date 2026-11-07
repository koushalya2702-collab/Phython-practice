x=10
print(type(x))  #find the type

x=10
y=float(x)  #type conversion
print(y)

a = 10
b = 3
print(a + b)  
print(a - b)  
print(a * b)  #arithmetic operations
print(a / b)  
print(a // b)  
print(a % b)  
print(a ** b)  


a=10
b=8
print(a)  #swapping of number without using third variable
a,b=b,a
print(a,b)


a=10
b=20
temp=a
a=b        #swapping of number using third variable
b=temp
print(a,b)

name=input("Enter your name: ")
age=int(input("Enter your age: "))
# print(f"hello {name} ,you are {age} years old ")             #use of f string
print("Hello " + name +" you are " + str(age) + " years old")

sentence=input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())          #string manipulation
print(sentence.strip())
print(sentence.replace(" ","__"))


length = input("Enter any sentence: ")
space=length.replace(" ","")            #find length 
print(len(space))


x = 5  # Assignment operators
x += 3 
x -= 2  
x *= 4  
x /= 6  

a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False   #Comparison Operators
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25)  # Output: True