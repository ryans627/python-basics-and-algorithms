username = input("Please type in your username: ")
password = input("Please type in your password: ")

print(f"Your username is: {username}, and your password is {password}.")

# day02
# 同时输入账号密码，用,隔开
username_password = input("请输入你的账号密码，中间用逗号隔开：") # 1234,qwer
print(username_password.split(',')) # 列表
l = username_password.split(',')
print(f"您输入的账号是: {l[0]}, 您输入的密码是: {l[1]}")