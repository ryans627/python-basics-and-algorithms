def outer_func(num1):
    def inner_func(num2):
        print(f'两个数值相加的结果：num1 + num2 = {num1 + num2}')

    return inner_func

# inner_func只有当outer_func被调用的时候才会被加载到内存中
# 由于outer_func没有被调用，所以inner_func没有被加载
# 函数的特性：在定义的时候不会执行，只有调用的时候才会执行函数内部代码
func = outer_func(666) # func = inner_func
func(888) # 等同于调用inner_func(888)
"""
代码执行逻辑:
line 1: 定义outer_func函数 => 
line 10: 调用outer_func函数 => 
line 2: 定义inner_func函数 => 
line 5: 返回inner_func (注意：此时 inner_func “记住了” outer_func 里的 num1 变量) => 
line 10: 得到了inner_func，并命名为func =>
line 11: func(888) =>
line 2: 调用inner_func(888) =>
line 3: print(num1 + num2)
"""