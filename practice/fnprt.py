def personal_info(**kwargs):
    '''
    kwargs must be dictionary
    '''
    if 'name' in kwargs:
        print('이름:',kwargs['name'])
    if 'age' in kwargs:
        print('나이:',kwargs['age'])
    if 'adress' in kwargs:
        print('주소 :',kwargs['adress'])

duckbea={'name':'김덕배','age':23}

personal_info(**duckbea)

print(duckbea.items())