"""
作业1. 定义一个的计算器的功能函数：要求定义3个形参，传递3个实参，进行判断实参符号，输出加减乘除的结果，比如：
    def calc(num1, num2, mark):
        if mark == "+":
            print(num1 + num2)
        elif mark == "-":
            pass
"""
def calc(num1, num2, mark):
    if mark == '+':
        print(num1 + num2)
    elif mark == '-':
        print(num1 - num2)
    elif mark == '*':
        print(num1 * num2)
    elif mark == '/':
        if num2 == 0:
            print("0不可以作为除数. division by zero is invalid.")
        else:
            print(num1 / num2)
    else:
        print('the mark input is invalid!')

calc(1, 3, "+")
calc(2, 10, "-")
calc(3, 9, "*")
calc(4, 8, "/")
calc(4, 0, "/")
calc(4, 8, "!")
