#Max Consecutive Ones
nums = [1,1,0,1,1,1]
max_count=0
count=0
for num in nums:

    if num==1:
        count+=1
        maximum=max(max_count,count)
    else:
        count=0
print(maximum)