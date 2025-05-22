# #while
# weight = 70
# while weight > 60:
#   print("운동하자")
#   weight -= 1
# print("목표 달성!")

# a = 5
# while a >= 0:
#   print("실행" )
#   a -= 1
# print("정지!")

# #도전하기
# aa = 5
# while aa >= 1:
#   print("안녕하세요")
#   aa -=1

# n = int(input("n : "))
# while n > 0:
#   print("실행")
#   n -= 1

# nn = int(input("n : "))
# while nn >= 0:
#   print(nn)
#   nn -= 1

# while 1:
#   y = input("y 입력 시 종료> ")
#   if y == 'y':
#     break
#   print(y)

# #while 반복문 연습 2
# sum = 0
# a = 1
# nnn = int(input("N값 입력: "))
# while a<=nnn:
#   sum += a
#   a += 1
# print(sum)

# a = 1
# while a <= 100:
#   if a%3==0:
#     print("짝", end=" ")
#   else:
#     print(a, end=" ")
#   a += 1

# alist = [1,2,1,2]
# while 2 in alist:
#   alist.remove(2)
# print(alist)

# bts = ['정국','뷔','지민','슈가','진','RM','제이홉']
# i = 0
# while len(bts) > i:
#   print(bts[i])
#   i+=1

# dan = int(input("원하는 단은: "))
# i = 1
# while 10 > i:
#   print(f"{dan} * {i} = {dan*i}")
#   i += 1

# import random
# com = random.randint(1,100)
# while True:
#   player = int(input("1부터 100사이의 숫자야 맞춰봐> "))
#   if player == com:
#     print("정답!")
#     break
#   elif player > com:
#     print("DOWN")
#   elif player < com:
#     print("UP")

# import random
# import time

# wlist = ['cat', 'dog', 'fog', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
# print("[타자게임]준비되면 엔터!")
# input()
# start = time.time()

# com = random.choice(wlist)
# n =1
# while n <= 5:
#   print(com)
#   player = input()
#   if com == player:
#     print("통과!")
#     n += 1
#     wlist.remove(com)
#     com = random.choice(wlist)
#   else:
#     print("오타! 다시 도전!")

# end = time.time()
# wt = end - start
# print(f"타자 시간 : {wt:.2f}초")