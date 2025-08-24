# # 全局变量
# name1 = "刘亦菲"
#
# # 全局变量在函数内部可以直接使用
# def show():
#     # 局部变量只能在函数内部使用，不能在函数外面使用
#     name2 = "赵丽颖"
#     print(f"局部变量name2: {name2}")
#     print(f"全局变量name1: {name1}")
#
# show() # 局部变量name2: 赵丽颖 # 全局变量name1: 刘亦菲


name = "刘亦菲"

def show():
    # 使用global关键字，将局部变量升级为全局变量
    global name
    name = "赵丽颖"
    print(f"函数内部name值: {name}")

print(f"函数调用之前：name值: {name}") # 函数调用之前：name值: 刘亦菲
show() # 函数内部name值: 赵丽颖
print(f"函数调用之后：name值: {name}") # 函数调用之后：name值: 赵丽颖