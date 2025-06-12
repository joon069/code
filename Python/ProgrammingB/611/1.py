#여철준
# id = input("id: ")
# pw = input("pw: ")
# if id == "admin" and pw == "1234":
#   print("환영합니다.")
# elif id == "admin" and pw != "1234":
#   print("pw 틀림")
# elif id != "admin" and pw == "1234":
#   print("id 틀림")
# if(id.count('"') or id.count("'") or 
#   id.count('\\') or id.count("#") or 
#   id.count('(') or id.count(')') or 
#   id.count('%') or id.count(':') or 
#   pw.count('"') or pw.count("'") or
#   pw.count('\\') or pw.count("#") or
#   pw.count('(') or pw.count(')') or
#   pw.count('%') or pw.count(':') ):
#   print("뒤져라 걍")

#권길현
# a = int(input("니 나이: "))
# y = int(input('몇년?: '))
# future = a + (y - 25)
# if future <= 0:
#   print("정자시절이네")
# else:
#   print(f"간다간다 쑝간다.{future}")

#문재준
# import random
# n = int(input("주사위 눈 개수: "))
# d1 = random.randint(1,n)
# d2 = random.randint(1,n)
# c = input("짝/홀: ")
# if (d1 + d2) % 2 == 0 and c == '짝':
#   print(f"짝임 {d1 + d2}")

# elif (d1 + d2) % 2 == 0 and c == '홀':
#   print(f"짝임 멍청아 {d1 + d2}")

# elif (d1 + d2) % 2 == 1 and c == '짝':
#   print(f"홀임 멍청이 {d1 + d2}")

# elif (d1 + d2) % 2 == 1 and c == '홀':
#   print(f"홀임 {d1 + d2}")

#김강
# jumin = input("주민번호: ")
# two = jumin.count('2')
# print(two)

#권기법
# n = int(input("숫자 입력: "))
# for i in range(1, n+1):
#   if i % 2 != 0:
#     print(i)

#성민규
# money = int(input("어 돈내놔: "))
# f = money
# days = int(input("며칠?: "))

# #days 만큼 입력을 받음
# ch = []
# for i in range(days):
#   daily_input = int(input())
#   ch.append(daily_input)

# for i in range(days):
#   money += int(money * ch[i] / 100)

# if(money < 0):
#   print("인생역전실패")

# elif(money > 0):
#   print("인생역전")
# elif(money == f):
#   print("본전")

#진수화
# aaa =  int(input("배수 입력: "))
# for i in range(10):
#   n = int(input("과연 배수일까?: "))
#   if n % aaa == 0:
#     print(f"{aaa}의 배수")
#   else:
#     print(f"{aaa}의 배수 아님")
# print("배수 찾기 종료")

#강태은
# n = int(input("배열크기: "))
# arr = []
# for i in range(n):
#   arr.append(int(input()))

# #find max value and index
# max_value = arr[0]
# max_index = 0
# for i in range(1, n):
#   if arr[i] > max_value:
#     max_value = arr[i]
#     max_index = i
# print(max_value, "\n", max_index+1)

#박하린
# n = int(input("평행사변형의 값: "))
# for i in range(n, 0, -1):
#   print(" " * i, "*" * n)

#정현태
# n = int(input("입력: "))
# for i in range(1, n+1):
#   s=str(i)
#   if'3' in s or '6' in s or '9' in s:
#     print("짝", end=" ")
#   else:
#     print(i, end=" ")

#권길현
# pw = []
# for i in range(5, 0,-1):
#   num = int(input())
#   pw.append(num)

# f = 10
# b = 1
# realPW = ""
# for i in pw:
#   realPW += str(i % f // b)
#   f *= 10
#   b *= 10
# print(realPW)

#print(12345 % 100 // 10)

#암살 대상 1위 신은총의 문제
name = []
money = []
부자놈 = []
n = int(input())
for i in range(n):
    put = input()
    deal = put.split()
    
    보낸놈 = deal[0]
    받는놈 = deal[1]
    돈 = int(deal[2])
    
    if 보낸놈 not in name:
        name.append(보낸놈)
        money.append(10000)
    if 받는놈 not in name:
        name.append(받는놈)
        money.append(10000)
    #operator
    보낸놈idx = name.index(보낸놈)
    받는놈idx = name.index(받는놈)
    
    money[보낸놈idx] -= 돈
    money[받는놈idx] += 돈
    
    큰돈 = max(money)
    부자놈.append(money.index(큰돈))
부자돈 = max(money)
부자돈위치 = money.index(부자돈)
찐부자 = name[부자돈위치]

print(f"{찐부자}가 {부자돈}으로 돈이 가장 많다.")
