from random import randint, choice

# 左闭右闭的区间, 包含开始和结束的整数值
# 获取1-3随机整数
num1 = randint(1, 3)
# 获取1-100随机整数
num2 = randint(1, 100)

print(num1, num2)

# 从列表中，随机提取一个元素值
names_list = ['刘亦菲', '张曼玉', '赵丽颖', '杨幂', '刘诗诗', '江疏影']
print(f"随机挑选一个女明星陪你吃饭：{choice(names_list)}")
