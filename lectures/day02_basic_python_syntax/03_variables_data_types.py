# 变量名要遵守取名规则
# 以数字，字母，下划线组成，不能是关键字，不能以数字开头
# 变量中可以存储哪些数据类型？
# 整数：正整数，负整数，0

num1 = 666
num2 = -250.3
num3 = 0
# 一次性输出多个变量，用逗号隔开
print(num1, num2, num3)
# 内建函数: python中已经定义/封装的函数
# 比如：print()输出功能；type()查看变量的数据类型
print(type(num1))  # <class 'int'>
print(type(num2))  # <class 'float'>

# 浮点数：小数
num4 = 3.14
print(num4, type(num4))  # <class 'float'>

# 布尔类型：真True, 假False<class 'str'>
# 高亮显示：关键字 => 首字母大写
# 一般会把布尔类型数据归纳为数字类型：True默认是数字1，False默认是数字0
print(True, False, type(True), type(False))  # <class 'bool'>
print(False + True + False)  # 1
print(False + True + False + False + True)  # 2
# PyCharm快捷键：快速规范/格式化代码 => Cmd + Alt + L

# 字符串: 用单引号或者双引号引起来的内容 => 一串字符
name = '吴彦祖'
print(name, type(name))  # <class 'str'>
age = 52
print(name, type(age))
age = '52'
print(name, type(age))
# 字符串可以使用加号（+) 进行拼接
# 字符串还可以使用星号(*)进行拼接，内容复制
print('---' * 100)  # 可以用来打印分割线

# 列表：存放Python中任意的数据类型
# 符号：[]
list_info = ['吴亦凡', 26, 18.7, False]
print(type(list_info))  # <class 'list'>
# 内建函数: len() => 查看数据的长度
print(len(list_info))  # 4

# 元组: tuple
# 存放python中任意的数据类型
# 特性：数据一旦被定义，就不能被修改，只能查看获取
# 符号：()定义元组的时候小括号可以省略
t1 = ('罗志祥', 37, 18.5, True)
print(t1, type(t1))  # ('罗志祥', 37, 18.5, True) <class 'tuple'>
print('-' * 100)
t2 = 1, 2, 3
print(t2, type(t2))
q, w, e, r = '哈哈', '嘿嘿', '嘻嘻', '咯咯'
print(q, w, e, r, type(q), type(w), type(e), type(r))

# 字典: dict
# 符号： {}, 多个key-value pair之间用逗号隔开
# 用空间换时间的一种数据类型
dict_info = {'name': '蔡徐坤', 'age': 27, 'job': '歌手'}
print(dict_info, type(dict_info))

# 集合: set
# 特性就是默认去重，集合里面没有重复的数据
# 符号 {数据1, 数据2, 数据3}
set1 = {1,2,2,3,3,4,5}
print(set1)