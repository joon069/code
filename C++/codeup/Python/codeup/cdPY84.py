h,b,c,s = map(int, input().split())
mp3 = float(h * b * c * s)/8/1024/1024
print(format(mp3, ".1f"), "MB")