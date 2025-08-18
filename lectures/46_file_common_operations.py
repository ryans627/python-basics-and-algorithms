# 文件常用操作 导入os模块
import os
import shutil

# 删除一个文件
os.remove('rap2.txt')

# 删除一个文件夹: 只能删除空文件夹
os.rmdir()

# 递归删除非空文件夹
# 把指定文件夹里面所有文件/文件夹全部删空，最后删除空文件夹
# 慎用：一旦执行递归删除，文件无法恢复
shutil.rmtree('tq')