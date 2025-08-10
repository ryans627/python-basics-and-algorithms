# # 使用浅拷贝，可变的数据类型: 字典，列表，集合
# import copy
#
# dict1 = {"list_num": [1, 2, 3], "num": 666}
# print(f"拷贝之前的字典内容是: {dict1}")
# # 对字典进行浅拷贝
# new_dict = copy.copy(dict1)
# print(f"拷贝之后的字典内容是: {new_dict}")
# print("-" * 100)
# # 将字典的list_num列表值提取出来，添加一个数字4
# # 然后查看添加之后的字典和原来的字典的内容
# new_dict['list_num'].append(4)
# print(f"添加数据之后：拷贝的字典内容是: {new_dict}") # 添加数据之后：拷贝的字典内容是: {'list_num': [1, 2, 3, 4], 'num': 666}
# print(f"添加数据之后：原字典内容是: {dict1}") # 添加数据之后：原字典内容是: {'list_num': [1, 2, 3, 4], 'num': 666}
# # 备份数据未生效：当被拷贝的数据发生修改，原数据也跟着修改 => 备份属于无效
# # 备份成功：被拷贝字典新增一个数据，原字典没有任何变化


# 使用深拷贝
import copy

dict1 = {"list_num": [1, 2, 3], "num": 666}
print(f"拷贝之前的字典内容是: {dict1}")
# 对字典进行浅拷贝
new_dict = copy.deepcopy(dict1)
print(f"拷贝之后的字典内容是: {new_dict}")
print("-" * 100)
# 将字典的list_num列表值提取出来，添加一个数字4
# 然后查看添加之后的字典和原来的字典的内容
new_dict['list_num'].append(4)
print(f"添加数据之后：拷贝的字典内容是: {new_dict}") # 添加数据之后：拷贝的字典内容是: {'list_num': [1, 2, 3, 4], 'num': 666}
print(f"添加数据之后：原字典内容是: {dict1}") # 添加数据之后：原字典内容是: {'list_num': [1, 2, 3], 'num': 666}