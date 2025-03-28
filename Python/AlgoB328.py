'''
반복문 정의
for i in range(시작값, 끝값, 증가값):
    코드
'''

'''
함수 정의
def 함수 이름(매개변수):
    코드
    return 반환값
'''

'''
함수 호출
함수 이름(함수에 전달 할 값)'
'''

#값을 받아 2배로 돌려주는 함수
def double(x):
    return x * 2
print(double(10))
print(double(25))


#문제 01 1부터 n까지의 합을 구하는 함수를 만들어라
def sum_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result
print(sum_n(10))
print(sum_n(100))

'''
리스트
list 는 정보 여러 개를 하난로 묶어 저장하고 관리할 수 있는 기능
리스트는 대괄호 안에 정보 여러 개를 쉼표(,)로 구분하여 적용

리스트 함수들
    len(a) : 리스트 개수 구함
    append(x) : 리스트 맨 뒤에 추가
    insert(i,x) : i 번 위치에 추가
    pop(i) : i 뽑아 냄
    clear : 다 비움
    x in a : x가 a 안에 있는지
'''

#문제 02
#가장 큰 숫자 찾기
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

V = [17,92,18,33,58,7,33,42]
print(find_max(V))


def find_max(a):
    n = len(a)
    idx = 0
    for i in range(1, n):
        if a[i] > a[idx]:
            idx = i
    return idx

V = [17,77,18,33,58,7,33,42,92]
print(find_max(V))