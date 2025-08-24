# 定义一个A类：封装4个实例方法
class A:
    def a(self):
        print("正在调用a实例方法")

    def b(self):
        print("正在调用b实例方法")

    def c(self):
        print("正在调用c实例方法")

    def d(self):
        print("正在调用d实例方法")

# 通过A类创建实例对象
x = A()

x.a()
x.b()
x.c()
x.d()

# 给x对象添加新的方法: 前提是必须有该方法或者函数的引用
# 给x对象添加一个输出的功能函数
setattr(x, 'e', print) # setattr(对象, 方法名字, 函数功能)
x.e('我的x对象获取了一个新的e方法，可以进行输出任意内容')
print("-" * 100)

def func():
    print("我是 func函数，一旦被调用就开始摸鱼.....")

setattr(x, 'w', func)

x.w()
print("-" * 100)
# 覆盖对象原来的方法，使用新方法的功能
setattr(x, 'a', input) # 对象a方法被input功能覆盖了，那么调用a方法的时候就会执行input函数
x.a("请输入值：")