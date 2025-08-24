class A:
    money_class = 1314

    def __init__(self):
        self.money = 520

    @classmethod
    def e(cls):
        print("正在调用类方法e")

    def a(self):
        print("正在调用a实例方法")

    def b(self):
        print("正在调用b实例方法")

    def c(self):
        print("正在调用c实例方法")

    def d(self):
        print("正在调用d实例方法")


x = A()
# 使用反射内建函数hasattr()判断对象中是否有该方法或者属性
# hasattr(对象名, '属性名或者方法名') => bool
print(hasattr(x, 'money_class')) # True
print(hasattr(x, 'money')) # True
print(hasattr(x, 'a')) # True
print(hasattr(x, 'b')) # True
print(hasattr(x, 'c')) # True
print(hasattr(x, 'd')) # True
print(hasattr(x, 'func')) # False