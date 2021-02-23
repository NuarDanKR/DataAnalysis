from pprint import pprint

col, row=map(int,input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

print()

count=0

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end='')
        '''
        if (matrix[i-1][j-1]
        or matirx[i-1][j]
        or matrix[i-1][j+1]
        or matrix[i][j-1]
        or matrix[i][j+1]
        or matrix[i+1][j-1]
        or matrix[i+1][j]
        or matrix[i+1][j+1])=='*':
            count+=1
        print(count,end="")
        else:
            print("."end='')
        '''

    print()


