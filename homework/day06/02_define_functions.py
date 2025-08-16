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
def func1(a, b, c, d=1, e=2, f=3, g=4, h=5, i=6, j=7):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, i={i}, j={j}")

# 创建一个函数，可以接收3～无数个参数
def func2(a, b, c, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}, args={args}, kwargs={kwargs}")

# 创建一个函数，可以接收无数个参数
def func3(*args, **kwargs):
    print(f"args={args}, kwargs={kwargs}")

# 创建一个函数，不可以接收参数
def func4():
    print("No arguments")

func1(1, 2, 3)  # a=1, b=2, c=3, d=1, e=2, f=3, g=4, h=5, i=6, j=7
func1(1, 2, 3, 3, 6, 9, 100)  # a=1, b=2, c=3, d=3, e=6, f=9, g=100, h=5, i=6, j=7
func1(1, 2, 3, j=10, e=21, i=30, d=40, f=13, g=7, h=2222)  # a=1, b=2, c=3, d=40, e=21, f=13, g=7, h=2222, i=30, j=10
print("-" * 100)

func2(1, 3, 4, 10)
func2(1, 3, 100,27,31130,z="123")
print("-" * 100)

func3()
func3(1, 3, 100,27,31130,z="123")
print("-" * 100)

func4() # No arguments
# func4(1) # TypeError: func4() takes 0 positional arguments but 1 was given