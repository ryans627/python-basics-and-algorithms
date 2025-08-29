a = ('a', 'b', 10, 30, 'a', 'b', 10, 30)

result = a.index('b', 2, 6) # 索引范围：左闭右开 => 能取到的范围: [2, 5]

print(result) # 5

