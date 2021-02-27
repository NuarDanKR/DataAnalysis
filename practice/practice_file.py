with open('words.txt','r') as file:
    count=0
    words=file.readlines()
    
    #n 제거
    for i in range(len(words)):
        words[i]=words[i].strip('\n')
    
    for word in words:
        if(len(word)<11):
            count+=1

print(count)

    