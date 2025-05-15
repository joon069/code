
# # 55 Page

# for i in range(1, 100, 2):
#   print(i, end=" ")


# #55 Page

# dan = int(input("원하는 단은?: "))
# for i in range(1, 10):
#   print(f"{dan} * {i} = {dan*i}")

# sum = 0
# a = 1
# for a in range(1,101):
#   sum += a
#   a += 1
# print(sum)

# char = str(input("문자열 입력: "))
# count = 0
# for i in char:
#   if i == 'a':
#     count +=1
# print(count)

# n = int(input())
# for i in range(n+1):
#   print(i, end=" ")

# n = int(input())
# for i in range(n):
#   print("*", end="")

# array = [273, 74, 103, 57, 52]
# index = 0
# for i in array:
#   print(f"{index} {i}")
#   index += 1

import turtle
t = turtle.Turtle()
t.shape("turtle")

#1
# for count in range(6):
#   t.circle(100)
#   t.right(60)
# turtle.done()

#2
# for i in range(4):
#   t.forward(100)
#   t.right(90)
# turtle.done()

#3
# n = int(input("정수 입력> "))
# for i in range(n):
#   t.forward(100)
#   t.left(360/n)
# turtle.done()

#4
# for i in range(5):
#   t.forward(100)
#   t.right(144)
# turtle.done()

#5
# n = int(input("정수 입력> "))
# sum = 1
# for i in range(1, n+1):
#   sum *= i
# print(sum)

# sum = 0
# for i in range(1,101):
#   sum += i
#   if sum >= 1000:
#     break
# print("1~100의 합에서 최초로 1000을 넘는 위치: ",i)

# sum = 0
# for i in range(1,101):
#   if i % 3 == 0:
#     continue
#   sum += i
# print("1~100의 합(3의 배수 제외) :  ",sum)

# mult = 1
# for a in range(1, 100):
#   if a % 2 == 0:
#     continue

#   print(f"{mult} * {a} = {mult*a}")
#   mult *= a

#   if mult >= 100:
#    break