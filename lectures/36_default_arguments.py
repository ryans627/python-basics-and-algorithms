# 默认参数只能在位置参数的后面，不能写在位置参数前面
# def func(x=1, y, z):
def func(x, y, z=123):
    print(f"x的值: {x}")
    print(f"y的值: {y}")
    print(f"z的值: {z}")


func(1, 2) # x的值: 1 y的值: 2 z的值: 123
print('-' * 100)
func(1, 2, 3) # x的值: 1 y的值: 2 z的值: 3

# 默认参数使用场景：控制实参传递数量范围
# func(x, y=456, z=123): 可以接收1-3个实参：传递1，2，3个实参都可以正常执行，0个或者超过3个实参不能使用

# 定义一个函数可以接收1-5个实参：
def func2(q,w=None,e=None,r=None,a=None):
    pass

func2(1)
func2(1,2)
func2(1,2,3)
func2(1,2,3,4)
func2(1,2,3,4,5)
# func2(1,2,3,4,5,6) TypeError: func2() takes from 1 to 5 positional arguments but 6 were given