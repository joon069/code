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
f1 = open("person.txt", "r")
name = f1.readline()
addr = f1.readline()
f1.close()
print("이름: ", name)
print("주소: ", addr)

