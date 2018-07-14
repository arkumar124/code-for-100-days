a=[]
n=int(input("Enter length of Array : "))
print("Enter Array : ")
for i in range(n):
    x=int(input())
    a.insert(i,x)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        j=j+1
    i=i+1
for i in range(n):
    print(a[i],end=" ")