def bsort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    return


l=[60,85,98,75,23]
print("before sorted:",l)
bsort(l)
print("the sorted list is:")
print(l)