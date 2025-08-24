"""
函数名需要符合标识符命名规则

def 函数名():
    pass
"""

# 需求：一个月正常有三十天，每逢1号，15号，30号，就唱歌

# 函数的定义：不会自动执行代码，需要手动调用才会执行函数中的代码块

def rap():
    print("111")
    print("222")
    print("333")
    print("444")

while True:
    day = int(input('今天是多少号？'))

    if day == 1:
        rap()
    elif day == 15:
        rap()
    elif day == 30:
        rap()
    elif day == 0:
        print("游戏结束！")
        break
    else:
        print("今天不唱歌，只有初一十五三十开唱")

