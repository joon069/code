# 결승점에 들어온 순서대로 수상과 상품을 안내하는 딕셔너리 작업하는 함수
d = {}
def g(name):
    if c == 1:
        d[name] = {"우승  ", "편의점 상품권 10만원"} 
    elif c == 2:
        d[name] = {"준우승", "편의점 상품권 5만원"}
    elif c == 3 or c == 4 or c == 5:
        d[name] = {"아차상", "편의점 상품권 3만원"}
    else:
        d[name] = {"참가상", "편의점 상품권 1만원"}

c = 1
ls = []
# 결승점에 들어오는 순서대로 이름 입력하고 함수 호출
while 1:
    name = input("이름 / 종료 : ")
    if  name == '종료':
        print()
        break
    else:
        ls.append(name)
        g(name)
    c+=1

#경기 결과에 따른 이름과 수상 및 상품 출력
s = []
for i in ls:
    name = i
    s = list(d[name])
    if s[0] > s[1]:
        s[0],s[1] = s[1],s[0]
    print(f"{name:<4}{s[0]}{s[1]:<15}")