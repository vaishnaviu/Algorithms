A = [4,5,3,1,0,2]
n = len(A)

for i in range(1,n):
    key = A[i]
    j = i-1
    while j>=0 and A[j]>key:
        A[j+1] = A[j]
        j=j-1
    A[j+1] = key

    print(A)