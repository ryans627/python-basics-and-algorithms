str1 = "qwer一套连招带走发个表情包ctrl+2"

print(str1, type(str1))

# 内建函数 built-in method
# len(): 查看数据长度
print(len(str1))  # 21

# 通过字符串的索引提取元素值，索引默认从0开始
# 语法格式：字符串[索引值]
print(str1[0])
print(str1[3])
print(str1[20])  # the last character
print(str1[-1])  # the last character can be represented by [-1] 负数索引
print(str1[-2])  # the second last character
# 当元素索引值超出范围时，程序会报错 => IndexError: string index out of range

# 通过索引范围提取多个值：字符个数: 21
# 语法格式: 字符串[开始索引: 结束索引]
# 左闭右开区间：包含开始不包含结束索引值
print(str1[0:4])  # 包含0，不包含4. 范围其实是[0, 1, 2, 3] => qwer
print(str1[:])  # qwer一套连招带走发个表情包ctrl+2
print(str1[4:])  # 一套连招带走发个表情包ctrl+2
print(str1[:15])  # qwer一套连招带走发个表情包
# 切片操作可以指定步长：n-1取值
# 语法格式：字符串[开始索引:结束索引:步长]
print('---' * 100)
print(str1[::2])  # qe一连带发表包tl2
print(str1[1:15:3])  # w一招发情
# 可以把步长设置为-1: 可以将字符串反转
print(str1[::-1]) # 2+lrtc包情表个发走带招连套一rewq
