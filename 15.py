#find the largest number
nums=list(map(int,input("Enter a number:").split()))
largest=nums[0]
for num in nums:
    if num > largest:
        largest=num
print("largest number is:",largest)


#find the smallest number
nums=list(map(int,input("Enter a number:").split()))
smallest=nums[0]
for num in nums:
    if num < smallest:
        smallest=num
print("smallest number is:",smallest)