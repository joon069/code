import turtle as t
t.shape("turtle")

a = int(input())
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)

t.forward(a)
t.left(120)
t.forward(a)
t.left(120)
t.forward(a)
t.left(120)


t.reset()
r = int(input("반지름의 크기를 얼마로 할까요?"))
t.circle(r)
t.circle(r*2)
t.circle(r*4)

t.done()

