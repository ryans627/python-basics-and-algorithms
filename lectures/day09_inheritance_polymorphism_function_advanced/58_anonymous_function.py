# 语法格式lambda 形参1, 形参2,... 冒号 : 返回值
lambda x, y: x + y

# 调用匿名函数: 将匿名函数整体括起来，再直接在匿名函数后面加上括号传递实参即可
print((lambda x, y: x + y)(13, 14))  # 27
# 匿名函数使用lambda关键字，普通函数定义使用def
# 匿名函数没有return关键字也可以返回值

# 1. 给匿名函数取名字进行调用
func = lambda x, y: x + y
print(func(11, 22)) # 33
print(type(func)) # <class 'function'>