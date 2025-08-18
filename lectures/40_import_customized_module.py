# 导入自定义模块中的函数和变量进行使用
from lectures.ryans.a import func_a
from lectures.ryans.b import func_b
# # 方式1: 导入模块
# import ryans_module
#
# # 引用模块中的变量
# print(ryans_module.age)
# print('-' * 100)
#
# # 引用模块中的函数
# ryans_module.func()

# # 方式2
# # from ryans_module import age, func
# from ryans_module import *
#
# print(age)
#
# func()

# 从包中导入模块
from ryans import a, b
print('导入ryans包中a模块中的变量和函数进行使用' + '-' * 100)
print(a.age)
func_a()

print('导入ryans包中b模块中的变量和函数进行使用' + '-' * 100)
print(b.age)
func_b()

# 方式2: 从包名.模块名 导入 具体的函数或者变量
from ryans.a import age
print(age)