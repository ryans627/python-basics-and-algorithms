# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#
# func() # {} <class 'dict'>
# func(x=1, y=2, z=3) # {'x': 1, 'y': 2, 'z': 3} <class 'dict'>

# 需求：设计一个函数，可以接收任意的实参，或者不接收
def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2() # () {}
print("-" * 100)
func2(1, 2, 3) # (1,2,3) {}
print("-" * 100)
func2(q="123") # () {'q': '123'}
print("-" * 100)
func2(1, 2, x=3) # (1, 2) {'x': 3}