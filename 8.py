#Alphabet pattern
n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#inverted triangle pattern
n=4
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#repeated alphabet triangle
n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()