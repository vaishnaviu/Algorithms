A = [2,3,1,4,9,0,2,4]
n = len(A)

for i in range(n-1):
    min = A[i]
    pos = i
    for j in range(i+1, n):
        if A[j]<min:
            min = A[j]
            pos = j
    A[i], A[pos] = A[pos], A[i]

print(A)