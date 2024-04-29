def ssort(l):
    n=len(l)
    for i in range (0,n):
        small=l[i]
        for j in range (i+1,n):
            if l[j]<small:
                small=l[j]
                temp=l[j]
                l[j]=l[i]
                l[i]=temp
    return

l=[30,50,14,20,10]
print("before sorted",l)
ssort(l)
print("after sorted",l)