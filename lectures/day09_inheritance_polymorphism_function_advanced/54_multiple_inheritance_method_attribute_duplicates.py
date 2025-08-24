class A:
    money = 100 # 类属性

    def w(self):
        print('A类: 正在调用w方法')


class B:
    money = 200

    def w(self):
        print('B类: 正在调用w方法')

# 如果多个父类的属性或者方法重名，那么优先会使用先继承的父类的属性和方法
class C(A, B):
    pass

c = C()
print("通过C类创建的c对象调用属性和方法:")
print(c.money) # 100
c.w() # A类: 正在调用w方法

print("-" * 100)

# 需要使用B类中的相同的属性和方法，只需要在继承的时候调换多继承的顺序即可
class D(B, A):
    pass

print("通过D类创建的d对象调用属性和方法:")
d = D()
print(d.money)
d.w()
print("-" * 100)

# 通过__mro__魔法属性可以获取类的继承顺序
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(D.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# 在python中，一切皆对象，所有类的父类都是object