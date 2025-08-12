from random import randint

num_list = []
for i in range (1, 8):
    num_list.append(randint(1, 10))
print(f"num_list是: {num_list}")

odd_count = 0
even_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"偶数个数为{even_count}, 奇数个数为{odd_count}")