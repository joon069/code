# #0~100 사이 점수
# while True:
#   a = int(input("점수를 입력해주세요: "))
#   if 0 <= a <= 100:
#     if a >= 80:
#       print("합격입니다.")
#       break
#     else:
#       print("불합격입니다.")
#       break
#   else:
#     print("다시 입력하세요.")

# # 홀수 짝수
# for i in range(1, 31):
#   if i%2==0:
#     print(f"{i} 짝수")
#   else:
#     print(f"{i} 홀수")

# #구구단 외자!
# import random
# print("구구단을 외자! 구구단을 외자!")
# while True:
#   a = random.randint(1, 9)
#   b = random.randint(1, 9)
#   c = int(input(f"{a} * {b}? "))
#   if c != a*b:
#     print("틀렸습니다!")

# #break 문
# a = int(input("숫자 입력: "))
# for i in range(1, 20):
#   if i > a:
#     break
#   print(i, end=" ") 

# #구구단 2트
# import random
# print("구구단을 외자! 구구단을 외자!")
# while True:
#   a = random.randint(1, 9)
#   b = random.randint(1, 9)
#   c = int(input(f"{a} * {b}? "))
#   if c != a*b:
#     print(f"땡! 정답은 {a*b}")