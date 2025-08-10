# String operations
print("-" * 50 + "字符串str操作" + "-" * 50)

str1 = "qwer一套连招带走发个表情包ctrl+2"
print(str1, len(str1))

print(str1[-1])
print(str1[1:3])
print(str1[::2])

# 反转字符串
print(str1[::-1])

# 通过元素值提取索引值：查找 find => 找不到返回-1
print(str1.find("招"))

# 通过元素值提取索引值: index => 找不到会报错

print(str1.replace("q", "G"))

# 字符串切片操作
str2 = "a,b,c,d,e,f,g,1,2,3,4,5"
print(str2.split(","))

str2 = "name age height hobby like"
print(str2.split(" "))


# 列表list的增删改查 => 很常用
print("-" * 50 + "列表list操作" + "-" * 50)
names_list = ["Ryan", "Nicole", "Jasper"]
print(f"列表的长度是：{len(names_list)}")

print(names_list[:2])

# 修改操作
names_list[0] = "Shawn"
print(names_list)

# 删除操作
