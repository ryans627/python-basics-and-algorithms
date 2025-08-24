# # 跳出本次循环：continue
# # 需求：给定一串数字字符，当字符中有0那么就跳过，其他数字输出
# s1 = "0812739801749107591076910769"
# list1 = []
#
# for i in s1:
#     if i == "0":
#         continue
#     else:
#         # print(i, end=',')
#         list1.append(i)
#
# print(list1)
# # 判断列表中是否有该字符：使用in关键字
# print('0' in list1) # False
#
# # 退出整个循环: break
# s1 = "812739801749107591076910769"
# list2 = []
# for i in s1:
#     if i == "0":
#         break
#     else:
#         # print(i, end=',')
#         list2.append(i)
# print(list2)
# # 判断列表中是否有该字符：使用in关键字
# print('0' in list2) # False

# while循环使用break和continue
# 当i等于8的时候 退出循环
# i = 1
# while i <= 100:
#     if i == 8:
#         break
#         i += 1

# 需求：1-100之间逢7过的游戏
# 数字能够被7整除，或者数字中包含7，那么都要跳过，将没有跳过的数值添加到列表
# 数字当中包含7的解决方案：先讲数字转化为字符串，然后进行判断7是否包含在字符串中
res = []
i = 1
while i <= 100:
    i += 1
    if i % 7 == 0 or '7' in str(i): # '7' in '37'
        continue
    else:
        res.append(i)

print(res)
