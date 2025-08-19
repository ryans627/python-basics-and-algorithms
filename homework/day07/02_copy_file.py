"""
作业2:

创建函数 copy_file，接收两个参数：file_a, file_b
    * 将file_a复制一份到文件file_b，要求内容完全一致
    * 如果a文件不存在或者b文件已存在，就打印【目标错误，无法复制】
"""


def copy_file(file_a, file_b):
    relative_dir = "../../resources/"
    file_a_path = relative_dir + file_a
    file_b_path = relative_dir + file_b

    try:
        f_a = open(file_a_path, mode='rb', encoding='utf-8')
    except FileNotFoundError:
        print("目标错误，无法复制")
    else:
        content_a = f_a.read()
        try:
            f_b = open(file_b_path, mode='w', encoding='utf-8')
        except FileExistsError:
            print("目标错误，无法复制")
        else:
            f_b.write(content_a)
        finally:
            f_b.close()
    finally:
        f_a.close()


copy_file("rap.txt", "rap_copy.txt")