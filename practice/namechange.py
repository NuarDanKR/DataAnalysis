#files = input().split()


files = '1.jpg 10.png 11.png 2.jpg 3.png'.split(' ')
print(list(map((lambda x : x.zfill(7) if len(x)<7 else x),files))) 

