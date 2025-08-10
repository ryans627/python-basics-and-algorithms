"""
3.输入11位手机号，获取之后输出手机号后四位
"""
phone_number = input("请输入您11位的手机号：")
# print(phone_number[-4:-1]) 这种写法是错误的，因为字符串切片操作左闭右开，取不到[-1]
print(phone_number[-4:])