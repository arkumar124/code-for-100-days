m=int(input('Enter the no. of rows in matrix :'))
n=int(input('Enter the no. of columns in matrix :'))
a=[[0 for x in range(m)] for y in range(n)]
b = [[0 for x in range(n)] for y in range(m)]
print('Order of Matrix : '+str(m)+'x'+str(n)+' Enter the Elements:')

mat = []
for j in range(m):
    row = []
    for k in range(n):
        row.append(int(input()))
    mat.append(row)

for row in mat:
    print(row)


print('\nTransposed matrix:')
res = [[mat[j][k] for j in range(m)] for k in range(n)]
for row in res:
    print(row)