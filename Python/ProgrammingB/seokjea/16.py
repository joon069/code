INT = int(input('정수 입력>'))
if INT%2==0 and INT%3==0:
    print(f"{INT}은 2와 3의 배수입니다.")
elif INT%2==0 and INT%3 !=0:
    print(f"{INT}은 2의 배수이고 3의 배수는 아닙니다.")
elif INT%2 !=0 and INT%3==0:
    print(f"{INT}은 3의 배수이고 2의 배수는 아닙니다.")
else:
    print(f"{INT}은 2와 3의 배수가 아닙니다.")