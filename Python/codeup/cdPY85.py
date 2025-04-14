w,h,b = map(int, input().split())
pic = (w*h*b)/8/1024/1024
print(format(pic, ".2f"), "MB")