def p(a):
  q = [i.lower() for i in a if i.isalpha()]
  s = [i.lower() for i in a if i.isalpha()]

  for _ in q:
    if q.pop(0) != s.pop():
      return False
  return True

print(p("WoW"))
print(p("Madam, I’m Adam."))
print(p("Madam, I am Adam."))



