"""
作业1:

创建函数new_file, 接收两个参数：name, content:
    * 根据name创建文件，并将content作为文件内容
    * 如果文件已经存在，则打印【文件已存在，无法创建】
"""


def new_file(name, content):
    """创建文件"""
    relative_dir = "../../resources/"
    file_path = relative_dir + name
    print(f"file_path: {file_path}")

    try:
        file = open(file_path, 'x', encoding='utf-8')
    except FileExistsError:
        print("文件已存在，无法创建！")
    else:
        file.write(content)
        file.close()


content = "别墅里面唱k,\n水池里面银龙鱼,\n我送阿叔茶具,\n他研墨下笔直接给我四个字,\n大展鸿图大师亲手提笔字,\n大展鸿图搬来放在办公室."
new_file('test.txt', content)
