G = 6.674*10**-11
m1, m2,r = map(float, (input("질량1: "), input("질량2: "), input("거리: ")))

F = G * m1 * m2 / r**2
print(F)
# 만유인력 공식