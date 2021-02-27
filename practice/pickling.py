#%%
import pickle as pkl

name = 'james'
age =16
adress = '서울 어쩌구'
scores ={'1a34':90,'51hio':89,'45h1':74}

with open('james.p','wb') as file: #wb:write binary
    pkl.dump(name,file)
    pkl.dump(age,file)
    pkl.dump(adress,file)
    pkl.dump(scores,file)

    
# %%
del name,age,adress,scores

with open('james.p','rb') as file :
    name = pickle.load(file)
    age=pickle.load(file)
    adress=pickle.load(file)
    scores=pickle.load(file)

print(name)
print(age)
print(adress)
print(scores)