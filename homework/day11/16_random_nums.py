"""
第16题：
A,随机生成8个的0-10（范围包含0和10）之间的数字存入列表。
B,设计一个函数，定义一个形参，并且调用改函数传递一个实参列表(随机生成的列表)，返回这个列表中8个数字出现的次数
C，然后调用函数并传入该列表，进行测试，打印出最终结果。
    比如【2,3,4,2,5,6,4，1】:
    - 2出现的次数2次
    - 1出现的次数1次
    - 3出现的次数1次
"""
import random

# def get_num_freq(nums: list) -> dict:
#     num_freq = {}
#     for num in nums:
#         if num in num_freq:
#             num_freq[num] += 1
#         else:
#             num_freq[num] = 1
#     return num_freq

num_list = []
for i in range(8):
    num_list.append(random.randint(0, 10))
else:
    print(num_list)


def get_freq_and_print(nums):
    for num in set(nums): # 遍历的是集合
        print(f"{num}出现的次数{nums.count(num)}次") # 统计的是列表

get_freq_and_print(num_list)