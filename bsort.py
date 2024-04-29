def bsort(l):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if l[j]>j+1:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
        return       
l=[40,30,50,10,90]
n=len(l)
bsort(l)
print("before the sorted list is:",l)
