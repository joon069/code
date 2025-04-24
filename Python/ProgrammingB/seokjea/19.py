import random
r = random.randint(0,99)
if 0<=r<=9:
    r = '0'+str(r)
else:
    r = str(r)

count = 0
bookgun = int(input("복권번호를 입력하시오(0~99)"))
bookgun = '0'+str(bookgun)

print(f"당첨 번호는 {r}입니다.")

if r[0] == bookgun[0]:
    count+=1
elif r[0] == bookgun[1]:
    count+=1
elif r[1] == bookgun[0]:
    count+=1
elif r[1] == bookgun[1]:
    count+=1

if count == 2:
    print("상금 100만원!")
elif count == 1:
    print("상금 50만원!")
else: print("상금이 없습니다.")