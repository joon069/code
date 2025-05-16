def Member(command, d):
  if command == 1:
    return add_member(d)
  elif command == 2:
    return change_point(d)
  elif command == 3:
    return add_point(d)
  elif command == 4:
    return del_member(d)
  elif command == 0:
    return print_member(d)
  
def add_member(d):
  Id = input("아이디 :")
  point = int(input("마일리지 :"))
  if Id in d:
    print("이미 존재하는 아이디 입니다.")
  else:
    d[Id] = point
  return f"{Id}님을 회원으로 등록하였고, 마일리지 {point}점이 적립되었습니다."

def change_point(d):
  Id = input("아이디 :")
  point = int(input("마일리지 :"))
  if Id in d:
    d[Id] = point
  else:
    print("존재하지 않는 아이디 입니다.")
  return f"{Id}님의 마일리지를 {point}점으로 변경하였습니다."

def add_point(d):
  Id = input("아이디 :")
  addPoint = int(input("마일리지 :"))
  if Id in d:
    d[Id] += addPoint
  else:
    print("존재하지 않는 아이디 입니다.")
  return f"{Id}님을 회원으로 등록하였고, 마일리지 {addPoint}점이 적립되었습니다."

def del_member(d):
  Id = input("아이디")
  if Id in d:
    del d[Id]
  else:
    print("존재하지 않는 아이디 입니다.")
  return f"{Id}님을 회원에서 삭제하였습니다."

def print_member(d):
  return '\n'.join(map(lambda x: f"아이디 : {x} 마일리지 : {d[x]}", d))

member = {
  "kk1234": 12000,
  "lee66": 11000,
  "han55": 3000,
  "hong77": 5000,
  "hwang": 18000
}
while 1:
  command = int(input("1:회원 추가 2: 포인트 변경: 3: 포인트 추가: 4: 회원삭제 0: 종료" ))
  print(Member(command, member), end="\n\n")
  if command == 0:
    break


