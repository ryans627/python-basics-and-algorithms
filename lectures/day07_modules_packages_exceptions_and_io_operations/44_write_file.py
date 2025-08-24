# 当文件不存在时，以读的方式打开文件，程序会报错:
# FileNotFoundError: [Errno 2] No such file or directory: 'rap2.txt'
# file = open('rap2.txt', encoding='utf-8')

# # 当文件不存在时，以写的方式打开文件，会新建文件
# # mode='w', 会重写/覆盖原来的内容，写入新的内容
# file = open('rap2.txt', mode='w', encoding='utf-8')
# file.write('aaaa, \nbbbbbbbb')
# file.close()

# # mode='a', 会追加写入文件内容
# file = open('rap2.txt', mode='a', encoding='utf-8')
# file.write('aaaa, \nbbbbbbbb\n')
# file.close()

# 使用上下文管理打开文件：

with open('../../resources/rap.txt', 'a', encoding='utf-8') as file:
    # 'a': 追加写入内容
    file.write('追加我想加入的内容/n冲冲冲！')