def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i] 
        j = i - 1 
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j] 
            j -= 1
        A[j + 1] = key
        
    print(A)

A = [88, 665, 25, 4, 76, 8, 46, 2, 1]
insertion_sort(A)