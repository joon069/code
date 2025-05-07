season = int(input())
if season <=5 and season >= 3:
    print("봄입니다.")
elif season <= 8 and season >= 6:
    print("여름입니다.")
elif season <= 11 and season >= 9:
    print("가을입니다.")
elif season <= 2 or season == 12:
    print("겨울입니다.")
else:
    print("잘못된 계절입니다.")