my_dict = {}

my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 3

print(my_dict) # {1: 3, '1': 2} => 1.0和1是相等的

# 当字典的键已存在，再次赋值会覆盖之前的值
# 1和1.0相等，那么当作建使用的时候就会覆盖
print(my_dict[1] + my_dict['1'] + my_dict[1.0]) # 8