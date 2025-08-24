# 通过装饰器获取一个函数的执行时间
import time

def get_execution_time(f):
    def inner():
        start_time = time.time()
        f() # f() = func()
        end_time = time.time()
        print(f'函数的执行时间为：{end_time - start_time}')
    return inner

# func = get_execution_time(func)
@get_execution_time
def func():
    list_1 = []
    for i in range(1, 6000001):
        list_1.append(i)
    else:
        print(f"{len(list_1)}")

func() # 6000000
# 函数的执行时间为：0.1718590259552002