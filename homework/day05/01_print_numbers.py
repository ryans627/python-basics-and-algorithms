# 作业：使用while循环输出1 2 4 5 6 8 10
i = 0
while i < 10:
    i += 1
    if i == 3 or i == 7 or i == 9:
        continue
    else:
        print(i, end=' ')

print("-" * 100)

# 使用for循环输出1 2 4 5 6 8 10
# range: 左闭右开. 要取到10必须range(1, 11)
for i in range(1, 11):
    if i == 3 or i == 7 or i == 9:
        continue
    print(i, end=" ")

print("-" * 100)

nums = [1, 2, 4, 5, 6, 8, 10]

for num in nums:
    print(num, end=" ")