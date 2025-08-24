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

# # 通过A类创建实例对象
# x = A()
# print(x.money)
# print(x.money_class)
# print('-' * 100)
#
# # 删除对象的实例属性
# delattr(x, 'money') # delattr(对象名, '实例属性名')
# # print(x.money) #  AttributeError: 'A' object has no attribute 'money'
#
# # 删除对象的类属性
# delattr(x, 'money_class')
# print(x.money_class) # AttributeError: 'A' object has no attribute 'money_class'

x = A()
x.a()
x.e()

delattr(x, 'a') # 删除对象的实例方法
x.a() # AttributeError: 'A' object has no attribute 'a'

delattr(x, 'e')
x.e() # AttributeError: 'A' object has no attribute 'e'