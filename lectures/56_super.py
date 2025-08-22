class A:
    money = 100

    def use_money(self):
        # 在类的实例方法中调用实例属性
        # 语法格式: self.实例属性名
        print(f'开始消费，大买特买，开始花钱: 100')


class C(A):
    money = 500

    def use_money(self):
        print(f'开始消费，大买特买，开始花钱: 500')

    # 在子类中定义一个实例方法，结合super()内建函数使用父类的属性或者方法
    def use_a_money(self):
        print("我自己有钱我不花，我就花父类的钱")
        print(super().money) # 100
        print('-' * 100)
        super().use_money() # 500


c = C()
print(c.money)
c.use_money()
c.use_a_money()

# 可以使用super()内建函数，调用子类与父类重名的属性或者方法
