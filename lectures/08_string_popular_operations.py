str1 = "qwer一套连招带走发个表情包ctrl+2"

# 通过字符串中的元素值来提取索引值
# 语法格式：字符串.find('元素值')
print(str1.find('招')) # 7
print(str1[7]) # 招
print('---' * 100)

str2 = "qwer一套q连招带走q发q个表情包ctrl+2"
print(str2.find('q')) # 0. 如果字符串当中有多个相同元素值，那么会从左到右返回第一个元素值的索引值
# 需要提取一个字符串中相同的元素值，获取不同索引那么可以使用索引范围操作
print(str2.find('一')) # 4
str2.find('q', 1,)

# 当提取一个元素值在字符串中没有时，那么会返回固定数值: -1
print(str2.find('k'))
print(str2.find('o'))

# 2. 通过字符串元素值来提取索引值: index()方法
# 当需要查找元素值在字符串中没有。那么程序会报错。
# print(str1.index('k')) # ValueError: substring not found
print(str2.index('连')) # 7. 默认是从左往右找
print(str2.rindex('q')) # 从右往左找到的第一个

print("---" * 100)
str1 = "qwer一套q连招带走q发q个表情包ctrl+2"
# 字符串替换方法: replace()
# 语法格式：字符串.replace('旧元素', '新元素')
print(str1.replace('r', 'd')) # qwed一套q连招带走q发q个表情包ctdl+2
# 使用场景：去除字符串中的空格
str2 = '  daksjk dsa dsd qweqe     qw ss '
print(str2, len(str2)) # '  daksjk dsa dsd qweqe     qw ss  33'
print(str2.replace(' ', '')) # 'daksjkdsadsdqweqeqwss'
print(str2) # "  daksjk dsa dsd qweqe     qw ss " => 字符串操作都是生成新字符串，而不是在原字符串做修改.

# 分割字符串 split
str1 = 'a,b,c,d,1,2,3,4,5'
# 语法格式：字符串.split('指定元素值') => 返回一个列表，将字符元素值存储在列表中
print(str1.split(',')) # ['a', 'b', 'c', 'd', '1', '2', '3', '4', '5']

# 面试笔试题：将字符串每一个单词提取存放在列表
str2 = 'name age height hobby like'
words = str2.split(' ')
print(words) # ['name', 'age', 'height', 'hobby', 'like']

# 判断一个字符串是否由纯数字组成 isdigit()
# 语法格式：字符串.isdigit()返回的是一个bool值
str2 = 'name age height hobby like'
print(str2.isdigit()) # 不是纯由数字组成 => False

str3 = '123131458908098231'
print(str3.isdigit()) # 纯由数字组成 => True

str2 = 'nameAheightBhobbyClike'
print(str2.isalpha()) # 判断是否纯由字母组成 => True

# 语法格式：'指定字符'.join(字符串)
str2 = 'name age height hobby like'
print(','.join(str2)) # 'n,a,m,e, ,a,g,e, ,h,e,i,g,h,t, ,h,o,b,b,y, ,l,i,k,e'
print('-'.join(str2)) # 'n-a-m-e- -a-g-e- -h-e-i-g-h-t- -h-o-b-b-y- -l-i-k-e'