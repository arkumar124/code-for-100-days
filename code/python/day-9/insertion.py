def insertion(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key

a=[]
n=int(input("Enter length of Array : "))
print("Enter Array : ")
for i in range(n):
    x=int(input())
    a.insert(i,x)
insertion(a)
for i in range(n):
    print(a[i],end=" ")