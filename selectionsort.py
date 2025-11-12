def selection_sort(A):
    for i in range(len(A)-1):
        minindex = i
        for j in range(i+1, len(A)):
            if A[j]<A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]
    print(A)
    
    
newlist = list(map(int, input("Enter numbers separated by commas: ").split(",")))

selection_sort(newlist)
