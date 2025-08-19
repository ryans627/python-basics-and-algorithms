# 文件常用操作 导入os模块
import os

os.rename('../resources', '../resource')
os.rename('../resource', '../resources')

# # 1. 重命名 os.rename("原文件名", "新文件名")
# os.rename('../resources/liuyifei.jpg', '../resources/liuyifei2.jpg')
# os.rename('../resources/liuyifei2.jpg', '../resources/liuyifei.jpg')
#
# # 2. 删除文件 os.remove("文件路径")
# os.remove('rap2.txt')
#
# 3. 获取当前文件路径信息
print(os.getcwd()) # 输出当前文件路径信息
#
# # 4. 新建文件夹
# os.mkdir("../resources/example")
#
# # 5. 删除文件夹
# os.rmdir("../resources/example")
#
# # 6. 获取目录下的文件名列表
# print(os.listdir("../resources")) # ['rap.txt', 'liuyifei.jpg']
#
# # 案例：删除一个有内容的文件夹，就必须先删除文件夹下面的文件，再删除文件夹
#
# for i in os.listdir("../resources"):
#     os.remove(i)
# else:
#     # 当else和for循环一起使用的时候，循环正常结束，会执行else里面的代码
#     os.rmdir("../resources")

# # 删除一个文件夹: 只能删除空文件夹
# os.rmdir()
#
# # 递归删除非空文件夹
# # 把指定文件夹里面所有文件/文件夹全部删空，最后删除空文件夹
# # 慎用：一旦执行递归删除，文件无法恢复
# shutil.rmtree('tq')