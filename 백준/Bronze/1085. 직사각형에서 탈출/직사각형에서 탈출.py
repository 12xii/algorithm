x, y, w, h = map(int, input().split())
wx = w - x
hy = h - y

if(x > wx):
    if(y > hy):
        print(hy if wx > hy else wx)
    else:
        print(y if wx > y else wx)
else: 
    if(y > hy):
        print(hy if x > hy else x)
    else:
        print(y if x > y else x)