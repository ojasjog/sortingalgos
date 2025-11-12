def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, 0, -1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    print(A)

A = [1, 665, 25, 4, 76, 8, 46, 2, 1]

insertion_sort(A)
