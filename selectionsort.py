#A = [5,4,222,10,15]
A = [5,2,6,1,3]

j = 0
while j < len(A):
    key = A[j]
    i = j
    while i < len(A):
        if A[j]>A[i]:
            A[j]=A[i]
            A[i]=key 
            key=A[j]
        i+=1
        print (A)  
    print ("next element")
    j+=1
print (A)
