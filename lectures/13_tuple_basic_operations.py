t1 = 1, 2, 3, 4, 5, 'a', 'b', True, False, [1, 3], 'a', 'b', 'a'

print(t1, type(t1))

# 通过索引提取元素值
print(t1[5])  # a
print(t1[5:9])  # 切片是左闭右开的 => 索引为 5, 6, 7, 8 => ('a', 'b', True, False)

# 使用内建函数获取元组中的数据
# 获取一个元素在元组中出现次数: count()内建函数
print(t1.count('a')) # 3

# 通过元素值获取索引位置
print(t1.index('b')) # 6