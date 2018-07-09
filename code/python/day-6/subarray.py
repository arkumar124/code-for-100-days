n=int(input('Enter the number of elements:'))
arr=[]
for x in range(n):
    arr.append(int(input()))
combine=[[]]

for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        sub=arr[i:j]
        combine.append(sub)
for row in combine:
    sum = 0
    for l in range(len(row)):
        sum+=row[l]
    if(sum == 0  and len(row)>0):
        print(row)