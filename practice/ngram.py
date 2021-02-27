txt=input('단어: ')
word=list(txt)
r=list(reversed(word))

if word == r:
    print('회문')
else :
    print('회문이 아닙니다.')