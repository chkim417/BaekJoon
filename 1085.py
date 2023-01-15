x, y, w, h = map(int, input().split())
xx = w - x
yy = h - y
print(min(x, y, xx, yy))