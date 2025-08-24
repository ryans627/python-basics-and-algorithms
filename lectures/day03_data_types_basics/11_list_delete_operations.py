# 第一种方法：pop() => 默认通过索引删除元素，默认不写索引值删除最后一个元素
# 语法格式: 列表.pop(索引值)
names_list = ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']
print(names_list) # ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']

names_list.pop()
print(names_list) # ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗']

names_list.pop()
print(names_list) # ['刘亦菲', '张曼玉', '赵丽颖', '杨幂']

# 第二种方法：remove() 指定元素值删除. 如果列表中没有指定删除元素，程序会报错.
# 语法格式：列表.remove(元素值)
names_list = ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']
names_list.remove('杨幂')
print(names_list) # ['刘亦菲', '张曼玉', '赵丽颖', '刘诗诗', '江疏影']
# names_list.remove('陈乔恩') # ValueError: list.remove(x): x not in list
print('---' * 100)

# 第三种方法：使用del关键字删除
# 语法格式: del 列表[索引值]
names_list = ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']
del names_list[4]
print(names_list) # ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '江疏影']

# 第四种方法：使用clear()方法清空列表
names_list = ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']
names_list.clear()
print(names_list) # []
