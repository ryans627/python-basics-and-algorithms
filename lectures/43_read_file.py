# 打开文件
file = open('../resources/rap.txt', mode='r', encoding='utf-8') # utf-8国际编码
# file打开的文件对象执行对应操作
# # 1. 一次性读取文件的所有内容：文件对象.read()
# content = file.read()
# print(type(content))
# print(content)

# # 2. 一次性读取所有内容，一行一行读取，返回一个列表，每一行的内容是字符串
# content = file.readlines()
# print(content) # ['别墅里面唱k,\n', '水池里面银龙鱼,\n', '我送阿叔茶具,\n', '他研墨下笔直接给我四个字,\n', '大展鸿图大师亲手提笔字,\n', '大展鸿图搬来放在办公室.']
# # 将读取的列表中的数据每一行的换行符进行删除
# content_list = []
# for i in content:
#     content_list.append(i.strip()) # strip去除字符串的空格制表符换行符: \t \n 空格
# else:
#     print(content_list)

# 3. 一次读取文件中一行内容
line = file.readline()
print(line)
line = file.readline()
print(line)

# 关闭文件
file.close()