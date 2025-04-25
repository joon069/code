import random

ai = random.randint(1,3)
user = int(input("가위(1)바위(2)보(3): "))
print(f"ai = {ai}")
print(f"유저 = {user}")
if ai==1:
    if user==2:
        print("유저 승리")
    elif user==3:
        print("ai 승리")
    else:
        print("비김")
elif ai==2:
    if user==3:
        print("유저 승리")
    elif user==1:
        print("ai 승리")
    else:
        print("비김")
else:
    if user==1:
        print("유저 승리")
    elif user==2:
        print("ai 승리")
    else:
        print("비김")