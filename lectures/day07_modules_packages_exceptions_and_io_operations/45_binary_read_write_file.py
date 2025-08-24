# 只要不是文本文件，都应该要使用二进制的方式读写文件

# 1. 打开原文件进行内容读取
# 使用with关键字打开一个文件：上下文管理器，作用：打开文件操作完成之后不需要手动关闭，而是可以自动关闭

# # rb, wb: 以二进制方式读取/写入
# with open('../resources/liuyifei.jpg', mode='rb') as file_1:
#     content = file_1.read()
#     # 2. 将读取的文件内容写入到新的文件中
#     with open('../resources/liuyifei_copy.jpg', 'wb') as file_2:
#         file_2.write(content)


# 结合for循环备份100张图片
for i in range(1, 101):
    with open('../../resources/liuyifei.jpg', mode='rb') as file_1:
        content = file_1.read()
        # 2. 将读取的文件内容写入到新的文件中
        # 当使用绝对路径的时候，如果路径中有特殊字符，那么需要在路径前面加：r, 代表原生字符串
        with open(fr'../resources/liuyifei_copy{i}.jpg', 'wb') as file_2:
            file_2.write(content)