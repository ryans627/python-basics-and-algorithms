def func1():
    print("正在执行func1...")
    func4()

def func2():
    print("正在执行func2...")
    print(a)

def func3():
    print("正在执行func3...")
    func1()

def func4():
    print("正在执行func4...")
    func2()

func3()