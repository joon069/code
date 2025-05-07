#1
Carspeed = int(input("현재 속도 입력>"))

if Carspeed >= 50:
    print("과속입니다.")
    print("속도를 줄여주세여요.")
else: 
    print("정상속도입니다.")
    print("즐거운 하루 되세요.")

#2
import random

a=random.randint(1, 9)
b=random.randint(1, 9)
answer=int(input(f"{a}*{b}는 무엇일까요?"))
if answer == a*b:
    print("정답입니다.")
else:
    print("구구단 공부합시다.")

#3
import random
print("동전 던지기 게임을 시작합시다.")
coin = random.randint(0, 1)
User = int(input("앞면(0)/뒷면(1)을 입력해주세요>"))
if coin == User:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")

#4
num = int(input('정수 입력> '))
if num < 0:
    print("음수입니다.")
else:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")

#5
num1 = int(input('첫번째 수 입력>'))
num2 = int(input('두번째 수 입력>'))
if num1 > num2:
    print('첫번째 수가 더 큽니다.')
elif num1 < num2:
    print('두번째 수가 더 큽니다.')
else:
    print('두 수가 같습니다.')

#6
money = int(input("돈 입력>"))
if money >= 5000:
    print('택시 타고 가라')
else:
    if money >= 2000:
        print('버스 타고 가라')
    else:
        print('걸어 가라')

#7
yunSoDuuk = int(input("연소득 입력> "))
jeaJik = int(input("재직기간 입력> "))

if yunSoDuuk >= 40000000 and jeaJik >= 2:
    print("대출 자격 있음")
else:
    if yunSoDuuk < 40000000 and jeaJik >= 3:
        print("연봉 4000만원 이상 필요")
    else:
        if yunSoDuuk >= 40000000 and jeaJik < 2:
            print("재직기간 2년 이상 필요")
        else:
            print("연봉 4000만원 이상, 재직기간 2년 이상 필요")

#8
num = int(input('정수 입력> '))
if num<0 :
    print("음수입니다.")
elif num==0 :
    print("0입니다.")
else:
    print("양수입니다.")

#9
money = int(input("돈 입력>"))
if money >= 5000:
    print('택시 타고 가라')
elif money >= 2000:
    print('버스 타고 가라')
else:
    print('걸어 가라')

#10
score = int(input("당신의 점수는 몇점인가요? "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

#11
age = int(input("나이를 입력해 주세요>"))
if age <= 7:
    print("유아입니다.")
elif 8 <= age <= 13:
    print("초등학생")
elif 14 <= age <= 16:
    print("중학생")
elif 17 <= age <= 19:
    print("고등학생")
else:
    print("성인")

#12
id = "ilovepython"
pawd = 123456

UserId = str(input('아이디을 입력하시오:'))
UserPawd = int(input('비밀번호을 입력하시오:'))

if id == UserId and pawd == UserPawd:
    print('환영합니다.')
elif id == UserId and pawd != UserPawd:
    print('비밀번호가 틀렸습니다.')
elif id != UserId and pawd == UserPawd:
    print('아이디가 틀렸습니다.')
elif UserId == "admin" and UserPawd == 1111:
    print("관리자가 로그인하였습니다.")
else:
    print('아이디와 비밀번호가 틀렸습니다.')

#13
year = int(input("연도를 입력해 주세요"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}은 윤년입니다.")
else:
    print(f"{year}은 윤년이 아닙니다.")

#14
temp = float(input('현재 온도 입력>'))
if temp >= 25:
    print('반바지를 입으세요')
elif temp <= 25:
    print("긴바지를 입으세요")

#15
a = int(input('첫번째 숫자>'))
b = int(input('두번째 숫자>'))
c = int(input('세번째 숫자>'))

if a > b:
    if a > c:
        print(f"기장 큰 수는 {a}")
    else:
        print(f"가장 큰 수는{c}")
else:
    if b < c:
        print(f"가장 큰 수는{c}")
    else:
        print(f"가장 큰 수는 {b}")

#16
INT = int(input('정수 입력>'))
if INT%2==0 and INT%3==0:
    print(f"{INT}은 2와 3의 배수입니다.")
elif INT%2==0 and INT%3 !=0:
    print(f"{INT}은 2의 배수이고 3의 배수는 아닙니다.")
elif INT%2 !=0 and INT%3==0:
    print(f"{INT}은 3의 배수이고 2의 배수는 아닙니다.")
else:
    print(f"{INT}은 2와 3의 배수가 아닙니다.")

#17
민증 = str(input("주민등록번호 입력> "))

if 민증[7] == '1':
    print(f"19{민증[:2]}년에 태어난 남자입니다.")

elif 민증[7] == '3':
    print(f"20{민증[:2]}년에 태어난 남자입니다.")

elif 민증[7] == '2':
    print(f"19{민증[:2]}년에 태어난 여자입니다.")

elif 민증[7] == '4':
    print(f"20{민증[:2]}년에 태어난 여자입니다.")

#18
ut = str(input("윷의 결과를 입력해 주세요>"))

count = int(ut[0]) + int(ut[1]) + int(ut[2]) + int(ut[3])

if count == 4:
    print("윷")
elif count == 3:
    print("걸")
elif count == 2:
    print("개")
elif count == 1:
    print("도")
else:
    print("모")

#19
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

#20
a = int(input('직선1의 길이>'))
b = int(input('직선2의 길이>'))
c = int(input('직선3의 길이>'))

if a+b>c and a+c>b and b+c>a:
    print("삼각형 가능")
else:
    print("삼각형 불가능")