# 位置参数：形参和实参数量一致，不能多也不能少，用来接收固定的实参数量

def func(name, age, hobby):
    print(f"我的名字是: {name}, 我今年: {age}, 我的爱好是: {hobby}")

#func()
func("蔡徐坤", 27, "唱跳rap篮球") # 我的名字是: 蔡徐坤, 我今年: 27, 我的爱好是: 唱跳rap篮球
# func("蔡徐坤", 27, "唱跳rap篮球", 666) # TypeError: func() takes 3 positional arguments but 4 were given