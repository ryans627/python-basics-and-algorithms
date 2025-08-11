"""
作业2.
注册账号密码时：
1. 要求账号为纯英文，否则无法注册，并且提示用户首字母必须是大写，如果用户输入的不是首字母大写则帮用户改为大写并输出账号信息
2. 要求密码长度为6-12位，
3. 如果密码正常，那么提示密码的长度，以及密码的后四位输出给用户
4. 如果密码不符合需求那就提示用户注册失败请重新输入
"""

username = input("请输入账号，账号需要为全英文且首字母必须大写：")

if not username.isalpha():
    print("您输入的账号存在非英文，注册失败。")
else:
    username = username[0].upper() + username[1:]
    username.istitle()
    print(f"您输入的账号为：{username}")

    password = input("请输入密码，密码长度需要为6-12位：")
    if 6 <= len(password) <= 12:
        print(f"您输入的密码长度为{len(password)}, 最后四位是{password[-4:]}")
    else:
        print("密码长度不符合要求，注册失败，请重新输入！")
