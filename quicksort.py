def qsort(A,low,high):
    
    if low<high:
        pi=partition(A,low,high)
        qsort(A,low,pi-1)
        qsort(A,pi+1,high)

def partition(A,low,high):
    p=low+1
    q=high
    pivot = A[low]
    while p<q:
        if A[p]<=pivot:
            p+=1
        if A[q]>=pivot: 
            q-=1
        else:
            A[p],A[q]=A[q],A[p]

  
    

A=list(map(int,input().split()))
low=0
high=len(A)-1
print("unaorted Array",A)
print("sorted array",qsort(A,low,high))

