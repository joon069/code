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