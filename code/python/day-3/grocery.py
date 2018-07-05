names=[]
amounts=[]
flag=False
file = open('grocery.txt', 'w+')
n=int(input('No of items:'))#taking input for no of items to be stored
print('Enter the item names and their amount in KG:')
for i in range(0,n):#taking input in form of item name and then it's amount in kg
    name=str(input())
    names.append(name)
    amount=int(input())
    amounts.append(amount) 
    file.write(names[i]+' => '+str(amounts[i])+'KG\n')
file.close()
file=open('grocery.txt','r')
if(file.mode=='r'):
    f1=file.readlines() 
search=str(input('Enter the item to search:'))
for i in range(0,len(f1)):
    if search in f1[i]:
        index=i
        flag=True
        break;
if(flag):
    print(str(amounts[index])+' KG')
else: 
    print('Item not in the file.')
file.close()