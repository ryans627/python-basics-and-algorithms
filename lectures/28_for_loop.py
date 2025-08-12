# 使用for关键字结合内建函数range()完成循环体构造
# range()是左闭右开的区间，包含开始，不包含结束
# range(10): 从0开始，到10结束，不包含结束
# range(1,10): 开始：1，到10结束，不包含结束
# for i in range(10):
#     print(i, end = ' ')
#
# list_a = []
# list_b = []
# # 使用for循环结合range()保存1-100之间的所有偶数和奇数分别存放到两个不同的列表中
# for i in range(1, 101):
#     if i % 2 == 0:
#         list_a.append(i)
#     else:
#         list_b.append(i)
#
# print(f"1-100所有的奇数: {list_b}")
# print(f"1-100所有的偶数: {list_a}")

# 字符串遍历
s1 = "djaiofgyqoy8@返回东风浩荡口服液012937"
for i in s1:
    print(i, end=",")
print()
print("-" * 100)

# 列表遍历
list1 = [1,2,3,32,3,434,4,2,2,2,2]
for i in list1:
    print(i, end="-")

# 元组，集合，字典都可以使用for循环遍历提取元素值