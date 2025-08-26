"""
作业2:
- 创建一个函数，可以接收3～10个参数
- 创建一个函数，可以接收3～无数个参数
- 创建一个函数，可以接收无数个参数
- 创建一个函数，不可以接收参数

以上的函数，不需要写逻辑，只要定义符合规范的形参即可
函数没有返回值，就会返回None
返回值必须是None，代码数量必须是最少
"""

# 创建一个函数，可以接收3～10个参数
def func1(a1, a2, a3, a4=1, a5=2, a6=3, a7=4, a8=5, a9=6, a10=7):
    pass

# 创建一个函数，可以接收3～无数个参数
def func2(a, b, c, *args, **kwargs):
    pass

# 创建一个函数，可以接收无数个参数
def func3(*args, **kwargs):
    pass

# 创建一个函数，不可以接收参数
def func4():
    pass

func1(1, 2, 3)
func1(1, 2, 3, 3, 6, 9, 100)
func1(1, 2, 3, j=10, e=21, i=30, d=40, f=13, g=7, h=2222)
print("-" * 100)

func2(1, 3, 4, 10)
func2(1, 3, 100,27,31130,z="123")
print("-" * 100)

func3()
func3(1, 3, 100,27,31130,z="123")
print("-" * 100)

func4() # No arguments
# func4(1) # TypeError: func4() takes 0 positional arguments but 1 was given