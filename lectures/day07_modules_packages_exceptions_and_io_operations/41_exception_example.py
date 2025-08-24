# print(a) # NameError: name 'a' is not defined

"""
* 通过try关键字可以进行异常的捕获
* 可以将可能会出现异常的代码放置于try当中
* 如果程序出现异常，不会报错，会执行except中的代码
* 如果没有出现异常，那么会执行else中的代码
* 最后不管异常是否出现，都会执行finally中的代码
"""

try:
    print(1)
    print("通过try关键字可以进行异常的捕获")
    print(2)
    # 0不能被当作被除数
    print(1 / 0) # 当try中的代码出现异常之后，不会继续执行，而是会直接跳转到except中的代码执行
    print(3)
except Exception: # 对所有的异常进行处理
    print(4)
    print("如果程序出现异常，不会报错，会执行except中的代码")
    print(5)
else:
    print(6)
    print("如果没有出现异常，那么会执行else中的代码")
    print(7)
finally:
    print(8)
    print("最后不管异常是否出现，都会执行finally中的代码")
    print(9)

