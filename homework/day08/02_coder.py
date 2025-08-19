class Coder:
    @classmethod
    def imagine(cls):
        print("我爱幻想")

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"我{self.name}的工作就是写代码")

    def sleep(self):
        print(f"我{self.name}要睡觉了")


coder1 = Coder("郭靖")
coder1.imagine()
coder1.work()
coder1.sleep()

print("-" * 100)

coder2 = Coder("黄蓉")
coder2.imagine()
coder2.work()
coder2.sleep()