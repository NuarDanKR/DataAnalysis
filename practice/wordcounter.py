import string

print("문장을 입력하세요.")
text = input("입력 :")
print("=======================")
word_to_find = input("찾을 단어 : ")

#단어들의 리스트화
words=text.split()

#모든 단어마다 구두점 제거
for i in range(len(words)):
    words[i]=words[i].strip(string.punctuation)
    
count=0
for word in words:
    if word==word_to_find:
        count+=1

if count==0:
    print("찾을 단어 없음")

print(f"'{word_to_find}'의 개수:",count)