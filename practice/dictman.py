
#manipulating dict x

x={'a':10,'b':20,'c':30}
x.setdefault('d', 0)
print(x)

x.update(d=40)

print(x)

#manipulating dict y
y={1:'what',2:'is',3:'your'}
print(y)
y.setdefault(4,'name')
y.update(zip([4,5],['favorite','food']))
print(y)

print(x.keys())
print(y.values())



