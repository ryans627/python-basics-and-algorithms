# 函数功能可以进行传递

def gong_fu():
    print("来一套闪电五连鞭")
    print("当时大意啦")
    print("没有闪")
    print("偷袭！")
    print("直接躺地上")
    print("年轻人，不讲武德")
    print("耗子尾汁")

# 通过函数的名字也就是函数引用可以将函数功能进行传递
gong_fu() # 调用函数
# 传递功夫
# 变量名 = 函数名
xiaofu = gong_fu
print('-' * 100)
xiaofu() # xiaofu() 等同于 gong_fu()