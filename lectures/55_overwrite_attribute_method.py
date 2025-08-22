class A:
    money = 100

    def use_money(self):
        # 在类的实例方法中调用实例属性
        # 语法格式: self.实例属性名
        print(f'开始消费，大买特买，开始花钱: {self.money}')


class C(A):
    money = 500

    def use_money(self):
        print(f'开始消费，大买特买，开始花钱: {self.money}')


c = C()
print(c.money)
c.use_money()