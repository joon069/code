민증 = str(input("주민등록번호 입력> "))

if 민증[7] == '1':
    print(f"19{민증[:2]}년에 태어난 남자입니다.")

elif 민증[7] == '3':
    print(f"20{민증[:2]}년에 태어난 남자입니다.")

elif 민증[7] == '2':
    print(f"19{민증[:2]}년에 태어난 여자입니다.")

elif 민증[7] == '4':
    print(f"20{민증[:2]}년에 태어난 여자입니다.")

