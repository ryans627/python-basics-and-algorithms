class A:
    q = '1' # 类属性

    def w(self):
        print('正在调用w方法')


class B:
    e = 2
    def r(self):
        print('r实例方法正在被调用')

class C(A, B):
    pass

c = C()
print("通过C类创建的c对象调用属性和方法:")
print(c.q)
c.w()
print(c.e)
c.r()