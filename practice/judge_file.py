

with open('practice/words.txt','r') as file:
    txt=file.read()
    words=txt.split(' ')
    
    for word in words :
        word=word.strip(',.')
        if 'c' in word:
            print(word)
        
