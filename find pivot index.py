from functools import math
lsum=0
rsum = 0
nums=[]       
n=int(input('enter number of items: '))
print('Enter %d items:' % n) 
for i in range(0,n):
    num=input()
    nums.append(num)
total=sum(nums)

for i in range(0,len(nums)):
    rsum=total-nums[i]-lsum
    if(lsum==rsum):
        print(i)
        lsum = nums[i]+lsum
print(-1)