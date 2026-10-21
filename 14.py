# #remove space
# s=input("Enter a sentence: ")
# w=s.replace(" ","")
# print(w)

# #check anagram string
# s1=input("Enter the first string: ")
# s2=input("Enter a second string: ")
# if sorted(s1)==sorted(s2):
#     print("anagram")
# else:
#     print("not a anagram")

# #find first non repeating character
# s=input("enter a string: ")
# for ch in s:
#     if s.count(ch)==1:
#         print("first non repeating character is:",ch)
#         break
#     else:
#         print("all character is repeating")


#count of words in string
s=input("enter a strind: ")
w=s.split()
count=len(w)
print(count)