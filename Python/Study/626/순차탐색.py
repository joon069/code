def 순차(ls, a):
  n = len(ls)
  for i in range(0, n):
    if ls[i] == a:
      return i
  return -1

ls = [17, 92, 18, 33, 58, 7, 33, 42]
print(순차(ls, 92))
print(순차(ls, 900))
print(순차(ls, 42))
      