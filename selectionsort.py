def selection_sort(A):
    for i in range(len(A)-1):
        minindex = i
        for j in range(i+1, len(A)):
            if A[j]<A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]
    print(A)
    
    
A = [99, 100, 34, 25]

selection_sort(A)
