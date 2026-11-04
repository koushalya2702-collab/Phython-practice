# #concatenation of array
# nums=[1,2,3]
# result=[]
# for num in nums:
#     result.append(num)
# for num in nums:
#     result.append(num)
# print(result)

nums=[1,2,3]
n=len(nums)
ans=[0]*(n*2)
for i in range(n):
    ans[i]=nums[i]
    ans[i+n]=nums[i]
print(ans)
