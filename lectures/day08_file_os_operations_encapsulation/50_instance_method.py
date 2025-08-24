# 实例属性自定义封装

class Hero:
    def __init__(self, name):
        # 名字
        self.name = name

    # 类中定义的函数就叫做：实例方法
    # 发起普通攻击
    def normal_attack(self):
        print("正在发起一次普通攻击，对敌方英雄造成了伤害")

    def cast_a_skill(self, skill):
        print(f"正在释放{skill}技能")

    def return_city(self):
        print("正在回城准备读秒")
        print("3")
        print("2")
        print("1")
        print("回到泉水")

ali = Hero('阿狸')
print(f"我的英雄名字是：{ali.name}")
ali.normal_attack()
# 传递实参，给形参使用
ali.cast_a_skill('Q')
ali.return_city()

# 给实例方法设置位置参数，传递实参进行调用