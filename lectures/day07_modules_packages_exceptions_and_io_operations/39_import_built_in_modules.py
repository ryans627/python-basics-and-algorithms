# 使用系统自带模块
# from random import randint, random

# 导入方式
# 方式1: 手动导入使用关键字：import
# 需要生成一个随机数

# import random
#
# # 调用格式：模块名.方法名()
# num1 = random.randint(1,100)
# print(num1)

# 方法2: 自动导入
# 在导入模块和包或者库的时候可以使用快捷键
# 直接写函数或者方法的名字，按回车会自动导入。快捷键：Alt + Enter
# 调用格式：方法名()
# 使用场景比较少，因为在有多个模块存在的时候，这种调用可能出现重名，造成问题
# num2 = randint(1, 100)
# print(num2)

import random as rd

num3 = rd.randint(1, 100)