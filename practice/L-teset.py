# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%[markdown]
# Lambda와 map, filter, reduce
## 1. Lambda
# %%
# 함수 사용과 기초적인 lambda 사용법

## 함수 사용시
def double(x):
    return 2*x

list(map(double,[1,2,3]))

## lambda 사용시
(lambda x : x*2)(8)

### 람다에 조건 걸기
a=[4,5,6,7,8,9]
map((lambda x : x/2 if x%2==0 else x),a)

del a

# %%[markdown]
## 2. map 사용하기
# %%
a=[1,2,3,4,5]
b=[5,4,3,2,1]

c=list(map((lambda x,y:x*y),a,b))

# %%[markdown]
## 3. filter 사용하기
# %%
# lambda로 필터링 해보기

# 1. function을 통해서
test = [4,6,8,10,12,14]

def f(x):
    if 5<x<10 :
        return x
    else :
        return

list(map(f,test))    

# %%
# 2.function을 간단히
def g(x):
    return 5<x<10

list(filter(g,test))


# %%
# 3. lambda를 이용해서!
list(filter((lambda x: x if 5<x<10 else None),test))


# %%
# 4.lambda 식을 더 간단하게
list(filter((lambda x: 5<x<10),test))

