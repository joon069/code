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
