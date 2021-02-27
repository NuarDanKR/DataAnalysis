keys=list(range(5))
vals=['a','b','c','d','e']


#아래는 딕셔너리를 만드는 1번 방법
'''
#키로 먼저 딕셔너리 형을 설정
my_dict=dict.fromkeys(keys)

#키에 값 할당
my_dict.update(zip(keys,vals))

print("Items:")
for key,val in my_dict.items():
    print(key,val)

print("\nkeys:")
for key in my_dict:
    print(key,end=' ')

print("\nvalues")
for value in my_dict.values():
    print(value,end=' ')
'''

x={a:None for i in dict.fromkeys(keys).keys()}
print(x)
