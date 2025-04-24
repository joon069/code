id = "ilovepython"
pawd = 123456

UserId = str(input('아이디을 입력하시오:'))
UserPawd = int(input('비밀번호을 입력하시오:'))

if id == UserId and pawd == UserPawd:
    print('환영합니다.')
elif id == UserId and pawd != UserPawd:
    print('비밀번호가 틀렸습니다.')
elif id != UserId and pawd == UserPawd:
    print('아이디가 틀렸습니다.')
elif UserId == "admin" and UserPawd == 1111:
    print("관리자가 로그인하였습니다.")
else:
    print('아이디와 비밀번호가 틀렸습니다.')
