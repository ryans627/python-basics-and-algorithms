# 需求：同事需要做冒烟测试，现在没有烟，让我跑腿买包烟
# 同事给你50块，然后要求去便利店买一包华子，然后拿给他，不用找零

def run_errands(money):
    print(f"拿到同事的{money}元")
    print("下楼，去便利店")
    print(f"拿一包华子，进行支付，剩余{money-45}")
    hua_zi = "硬中华香烟"
    # 函数的返回值
    return hua_zi


cigarette = run_errands(50)

print(cigarette)