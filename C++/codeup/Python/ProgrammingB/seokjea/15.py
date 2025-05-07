a = int(input('첫번째 숫자>'))
b = int(input('두번째 숫자>'))
c = int(input('세번째 숫자>'))

if a > b:
    if a > c:
        print(f"기장 큰 수는 {a}")
    else:
        print(f"가장 큰 수는{c}")
else:
    if b < c:
        print(f"가장 큰 수는{c}")
    else:
        print(f"가장 큰 수는 {b}")