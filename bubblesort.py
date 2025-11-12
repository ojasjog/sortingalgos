def swap(a,b):
    return b, a
    

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


A = [44, 32, 78, 508, 99]

print(bubble_sort(A))
                
