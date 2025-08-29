def func(a, b, c): # 2, 4, 6
    return c + a, a + b, b + c # 8, 6, 10

c, b, a = func(2, 4,6) # c = 8, b = 6, a = 10

print("a:%d b:%d c:%d" % (a, b, c)) # 10, 6, 8