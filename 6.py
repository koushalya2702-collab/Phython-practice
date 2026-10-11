#increasing number triangle
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#decreasing number triangle
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#repeated number triangle
n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()


#floyds triangle pattern
n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()