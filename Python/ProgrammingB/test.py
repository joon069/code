# string = input("인사말을 입력하세요> ")
# print(string)
# print(type(string))



# number = (input("정수를 입력하세요> "))
# print(number)
# print(type(number))



# string = input("입력>")
# print("자료: ",string)
# print("자료형: ",type(string))



# string_a = input("입력> ")
# int_a = int(string_a)

# string_b = input("입력> ")
# int_b = int(string_b)

# print("문자열 자료: ", string_a+string_b)
# print("정수 자료: ", int_a + int_b)



# input_a = float(input("첫 번째 숫자> "))
# input_b = float(input("두 번째 숫자> "))

# print("덧셈 결과:", input_a + input_b)
# print("뺄셈 결과:", input_a - input_b)
# print("곱셈 결과:", input_a * input_b)
# print("나눗셈 결과:", input_a / input_b)



# print("안녕하세요? 이름을 입력해주세요.")
# name = input()
# print(name + "님, 안녕하세요!")
# print("나이를 입력해주세요.")
# age = input()
# print(20-int(age), "년 후면 20살이시네요!")


# 파일 다루는 법
# f1 = open("movie.txt", "a")
# f1.write(input() + "\n")
# f1.write(input() + "\n")
# f1.close()

# f2 = open("movie.txt", "r")
# movieTitle = f2.readline()
# ticketPrice = f2.readline()
# f2.close()


# print("영화제목: ", movieTitle)
# print("티켓가격: ", ticketPrice+"원")



# print("치킨\t\t21마리")
# print("콜라\t\t2.5L")
# print("감자칩\t\t3판")

# count = 21

# print((9000*count)+((400*2)*count)+(700*count), "원")

# sum = 0
# for i in range(5, 11):
#   sum += i
# print(sum)

# sum = 0
# i = 3
# while i <= 100:
#   sum += i
#   i += 3
# print(sum)

for i in range(1, 10):
  for j in range(1,10):
    print(i,'*', j, '=', j*i)
  print(i,"단")