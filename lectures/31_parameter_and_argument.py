# 函数在定义的时候在括号中可以写入形参：形式参数
def kung_fu(name):
    print(f"顶级大师：{name}，正在举行公开赛，全网直播")
    print("来一套闪电五连鞭")
    print("当时大意啦")
    print("没有闪")
    print("偷袭！")
    print("直接躺地上")
    print("年轻人，不讲武德")
    print("耗子尾汁")

# 调用函数的时候在括号中可以写入实参：实际参数
# TypeError: kung_fu() missing 1 required positional argument: 'name'
# 定义形参之后一定要传递实参：位置参数，不能多也不能少，要一一对应
kung_fu("马保国")