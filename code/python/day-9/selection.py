a=[]
n=int(input("Enter length of Array : "))
print("Enter Array : ")
for i in range(n):
    x=int(input())
    a.insert(i,x)
for i in range(n):
    for j in range(n):
        if a[i]<a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
        j=j+1
    i=i+1
for i in range(n):
    print(a[i],end=" ")
