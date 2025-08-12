from random import randint

# list_nums = []
# num1 = randint(1, 100)
# list_nums.append(num1)
# print(list_nums)

# 使用while关键字构造循环体
# 循环计数变量，来判断条件是否成立继续执行循环代码
# 计数变量需要不断地累加，才能终止循环条件
# i = 1
# list_num = []
# while i <= 10:
#     list_num.append(randint(1, 100))
#     i += 1 # 即: i = i + 1
#
# print(list_num, len(list_num))

# i = 1
# while i <= 100:
#     # 默认每次输出内容都会自动换行
#     # 可以改变默认换行符\n, 按照指定格式输出内容
#     print(i, end=",")
#     i += 1

# 输出1-100所有的偶数和奇数
odds = []
evens = []

i = 1
while i <= 100:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
    i += 1

print(f"1-100所有的奇数: {odds}")
print(f"1-100所有的偶数: {evens}")
