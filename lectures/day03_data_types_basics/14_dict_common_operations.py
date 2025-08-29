dict_info = {'name': '蔡徐坤', 'age': 27, 'sex': '男', 'job': 'singer'}

print(len(dict_info)) # 4

# 字典查询操作
# 语法格式: 字典['key']

print(dict_info['name']) # 蔡徐坤
dict_info['job'] # singer

# 获取字典中所有的keys
print(dict_info.keys()) # dict_keys(['name', 'age', 'sex', 'job'])
# 获取字典中所有的values
print(dict_info.values()) # dict_values(['蔡徐坤', 27, '男', 'singer'])
# 获取字典中所有的键值对
print(dict_info.items()) # dict_items([('name', '蔡徐坤'), ('age', 27), ('sex', '男'), ('job', 'singer')])

# 使用update()方法
# 语法格式: 字典.update()
# 字典合并，默认加到末尾
dict_info.update({'hobby': "basketball"})
print(dict_info) # {'name': '蔡徐坤', 'age': 27, 'sex': '男', 'job': 'singer', 'hobby': 'basketball'}

# 给字典新增一个键值对
print('---' *  100)
dict_info['like'] = 'rap'
print(dict_info) # {'name': '蔡徐坤', 'age': 27, 'sex': '男', 'job': 'singer', 'hobby': 'basketball', 'like': 'rap'}
dict_info['job'] = 'actor'
# 如果key存在，则会覆盖这个key对应的原来的值
print(dict_info) # {'name': '蔡徐坤', 'age': 27, 'sex': '男', 'job': 'actor', 'hobby': 'basketball', 'like': 'rap'}

# pop()方法
print(dict_info) # {'name': '蔡徐坤', 'age': 27, 'sex': '男', 'job': 'actor', 'hobby': 'basketball', 'like': 'rap'}
dict_info.pop('sex')
print(dict_info) # {'name': '蔡徐坤', 'age': 27, 'job': 'actor', 'hobby': 'basketball', 'like': 'rap'}

#使用clear方法清空字典
dict_info.clear()
print(dict_info) # {}

print('-' * 100)

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 3 # 1.0和1的哈希值相同

print(my_dict) # {1: 3, '1': 2}
print(f"{my_dict[1] + my_dict['1'] + my_dict[1.0]}") # 8