import random as rand

dice = rand.randint(1,6)

val = int(input("값 :"))

if not(0<val<7):
    print("잘못된 값을 입력하셨어요")
    val = int(input("값 :"))
    if dice==val:
        print("정답입니다!",dice)
        break

elif dice==val:
    print("정답입니다!",dice)

else:
    while dice!=val:
        print("틀렸습니다 값을 다시 입력해주세요.",dice)
        val = int(input("값 :"))
        if dice==val:
            print("정답입니다!",dice)
            break