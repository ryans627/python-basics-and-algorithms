def func(x, y, z):
    print(f"x的值: {x}")
    print(f"y的值: {y}")
    print(f"z的值: {z}")


# 通过位置参数传递实参
func(1, 2, 3)

print('-' * 100)
# 通过形参关键字传递实参
func(z=666, x=521, y=1314)
print('-' * 100)

# 位置参数和关键字参数结合使用
# 位置参数一定要在关键字参数前面，位置参数和关键字参数不能重复
func(4, 5, z=6)
func(4, x=3, z=10)  # TypeError: func() got multiple values for argument 'x'
