#reverse a string
s=input("Enter a string: ")
rev=s[::-1]
print("reversed string:",rev)

#check a string polindrome
s=input("Enter a string: ")
s=s.lower()
rev=s[::-1]
if s==rev:
    print("its a polindrome")
else:
    print("its not a polinrome")

#count vowels and consonants
s=input("Enter a string: ")
vowels="aeiouAEIOU"
v_count=0
c_count=0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count+=1
        else:
            c_count+=1
print("vowels:",v_count)
print("consonents:",c_count)

#find frequency of character
s=input("Enter a string: ")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)