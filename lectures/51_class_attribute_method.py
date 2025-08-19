class Hero:
    # 类属性：类中的变量叫做类属性
    age = 18

    def __init__(self, name):
        # 实例属性：名字
        self.name = name

    # 类中定义的函数就叫做：实例方法
    def cast_a_skill(self, skill):
        print(f"正在释放{skill}技能")

    # 类方法: 定义格式，固定装饰器
    @classmethod
    def sneer(cls): # cls: 代表类的名字
        print("聊天窗口已打开，准备火力全开，开喷")
        print("一秒十句，还能十步一人")
        print("亮表情包，让对面破防")


ali = Hero('阿狸')
print(f"我的英雄名字是：{ali.name}")
# 传递实参，给形参使用
ali.cast_a_skill('Q')
# 类属性与类方法的调用
ali.sneer()
# 总结：实例属性，类属性，实例方法，类方法，对象都可以进行调用
# 类属性和类方法：类本身可以调用
# 但是类本身不可以调用实例属性和实例方法
print('-' * 100)
print(f"调用类属性: {Hero.age}")
print(f"调用类方法: {Hero.sneer()}")