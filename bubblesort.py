#bubble sort
a = []
n=int(input('No. of elements: '))
print('Enter %d numbers: ' % n)
for i in range(0,n):
    num=(input())
    a.append(num)

# a.sort() 
for i in range(1,n):
   for j in range(0,n-i):
       if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]

print('sorted array: ', a)