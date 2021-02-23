a = list(range(0,15,2))

for index,val in enumerate(a,1):
    print(f'[{index}번]{val}')

b=[i + 5 for i in range(10) if i % 2 == 1]
#c=[6,8,10,12,14]
print("b:",b)

print("b.sum:",sum(b))