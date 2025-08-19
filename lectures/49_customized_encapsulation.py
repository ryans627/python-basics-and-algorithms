# 实例属性自定义封装

class Hero:
    # 魔法方法
    # 不需要手动调用，会在特殊机制下自动调用
    # 对象一旦被创建，魔法方法就会被执行
    # 实例属性固定的前面会有一个self代表对象本身
    # self.属性名 = 值
    def __init__(self, name, attack_power, defence_power, hp, mp):
        # 名字
        self.name = name
        # 攻击力
        self.attack_power = attack_power
        # 防御值
        self.defence_power = defence_power
        # 生命值
        self.hp = hp
        # 魔法值
        self.mp = mp


# 通过类可以创建对象
# 对象可以调用实例属性和实例方法
# 语法格式：变量名 = 类名()
yasuo = Hero("亚索", 80, 90, 300, 0)  # 对象
# 通过对象调用实例属性
print(f"我的英雄名字是：{yasuo.name}, 我的攻击力为：{yasuo.attack_power}, 我的护甲值是:{yasuo.defence_power}")
print(f"我的初始生命值是:{yasuo.hp}, 我的魔法值是{yasuo.mp}")
print('-' * 100)

ali = Hero("阿狸", 52, 65, 5000, 2000)  # 对象
# 通过对象调用实例属性
print(f"我的英雄名字是：{ali.name}, 我的攻击力为：{ali.attack_power}, 我的护甲值是:{ali.defence_power}")
print(f"我的初始生命值是:{ali.hp}, 我的魔法值是{ali.mp}")
# 当对象被创建的时候，实例属性的值是固定的
# 同一个类创建的对象拥有不同的实例属性
