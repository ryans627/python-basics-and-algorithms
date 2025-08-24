# class A:
#     money_class = 1314
#
#     def __init__(self):
#         self.money = 520
#
#     @classmethod
#     def e(cls):
#         print("正在调用类方法e")
#
#     def a(self):
#         print("正在调用a实例方法")

# x = A()
# # 可以使用getattr()反射把对象的属性或者方法传递给变量进行使用
# # getattr(对象名, '属性名或方法名')
# mc = getattr(x, 'money_class')
# print(mc) # 1314
#
# m = getattr(x, 'money')
# print(m) # 520
#
# # 获取实例方法a
# a = getattr(x, 'a')
# a() # 正在调用a实例方法
#
# # 获取类方法e
# e = getattr(x, 'e')
# e() # 正在调用类方法e


class A:

    def a(self):
        print("正在调用a实例方法")

    def b(self):
        print("正在调用b实例方法")

    def c(self):
        print("正在调用c实例方法")

    def d(self):
        print("正在调用d实例方法")


x = A()
# 将类的所有方法名字放到列表中，通过遍历列表反射提取调用
for i in ['a','b','c','d']:
    f = getattr(x, i)
    f()