#quiz for dojang.io

n = int(input("입력 :"))

for i in range (n):
    for j in range (n-i,0,-1):
        print(' ',end='')
    for k in range (2*i+1):
        print('*',end='')
    print()

