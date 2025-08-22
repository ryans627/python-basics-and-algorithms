# 继承的基本语法，在定义类的名字后面加上小括号，在括号中写上父类的名字即可
class A:
    q = '1' # 类属性
    def __init__(self):
        self.w = 2 # 实例属性

    def e(self): # 实例方法
        print("正在调用A类中的实例方法e")

    @classmethod # 类方法
    def r(cls):
        print("正在调用A类的类方法r")

a = A()
print(a.q)
print(a.w)
a.e()
a.r()
print('-' * 100)

# 单继承基本使用
# 加了括号 => 新式类
# 不加括号 => 旧式类
# A类是B类的父类, B类是子类
class B(A):
    pass

b = B()
b.e()
b.r()
print(b.q)
print(b.w)

