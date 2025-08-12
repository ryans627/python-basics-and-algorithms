print(1 == 1 and 2 == 2)  # True
print(1 == 2 and 2 == 2)  # False
print(1 == 1 and 2 == 1)  # False
print(1 == 2 and 2 == 1)  # False

print("-" * 100)

print(1 == 1 or 2 == 2)  # True
print(1 == 2 or 2 == 2)  # True
print(1 == 1 or 2 == 1)  # True
print(1 == 2 or 2 == 1)  # False

print("-" * 100)

print(not 1 == 1)  # False
print(not 1 == 2)  # True

# 案例练习：要求用户输入中国传统节日，可以是节日名，也可以是日期，输出对应习俗
day = input("要求用户输入中国传统节日，可以是节日名，也可以是日期：")

if day == "中秋节" or day == "8月15":
    print("吃月饼，赏月")
elif day == "端午节" or day == "5月5":
    print("吃粽子，划龙舟")
elif day == "春节" or day == "1月1":
    print("吃年夜饭，放鞭炮看烟花")
else:
    print("不是特别重要的节日，可以不过")
