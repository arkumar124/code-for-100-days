from math import gcd

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
num3 = int(input("Enter Number 3:"))
num4 = int(input("Enter Number 4:"))
a = [num1,num2,num3,num4]  
lcm = a[0]
for i in a[1:]:
  gc =gcd(lcm,i)
  lcm = int(lcm*i/gc)
print(gcd(a[0],gcd(a[1],gcd(a[2],a[3]))))
print (lcm)
