"""
场景：要求用户输入任意字符的一串密码.

需求：
提示用户密码是否是纯数字组成
如果密码中出现数字6全部替换成数字7
将密码中所有的出现的小写字母转化为大写
将密码中出现的所有空格进行去除
统计密码中出现的数字8有几次
"""
password = input("请输入密码: ")

if password.isdigit():
    print("您的密码由纯数字组成。")
else:
    print("您的密码不是全部由数字组成。")

new_password = password.replace("6", "7").upper().replace(" ", "")

count = new_password.count("8")

print(f"处理后的密码是{new_password}, 密码中数字8共出现{count}次")
