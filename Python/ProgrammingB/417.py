age = int(input("Enter your age: "))
if age >= 20:
    print("성인입니다.")
elif age >= 13 and age <20:
    print("청소년입니다.")
elif age < 13:
    print("어린이입니다.")