# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
file=open('hello.txt','r')
txt=file.read()
print('file:',type(file))
print('txt:',type(txt))
print(txt)
file.close()


# %%
with open ('hello.txt','r') as file:
    txt=file.read()
    print(txt)


# %%
with open('hello.txt','w') as file:
    for i in range(3):
        file.write("Hi everybody! {i}")


# %%
with open('hello.txt','w') as file:
    for i in range(3):
        file.write(f'Hi everybody! {i}\n')


# %%
lines=['안녕하세요\n','적당히\n','바람이 시원해\nrleg']
with open('hello.txt','w') as file:
    file.writelines(lines)


# %%
with open ('hello.txt','r') as file:
    txt=file.read()
    print(txt)


# %%
with open ('hello.txt','r') as file:
    txt=file.readlines()
    print(txt)


# %%
del lines


# %%
with open('hello.txt','r') as file:
    line = None
    while line !='':
        line=file.readline()
        print(line)


