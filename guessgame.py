# guessgame.py —— 模块 B 收尾验收：猜数字游戏
#
# 题目：电脑想一个 1-20 的数，你反复猜，它告诉你大了还是小了，猜中就退出并报猜了几次
#
# 这题不用新知识，全是本周已学的拼装：
#   item 12 if/elif/else  → 三路提示（大了 / 小了 / 猜中了）
#   item 13 and/or/not    → 猜中就在"大了/小了"之外，必须排最前（first-match-wins）
#   item 15 while + break → 反复猜 + 猜中跳出
#   item 17 range         → 造 1-20 这堆候选数
#   item 11 累加器        → 数猜了几次
#
# 标准：能自己跑通 + 喂几组输入都合理 = 模块 B 收官

# ===== 步骤 1：先造出那个数 =====
# 提示：造 1 到 20 的随机数，先用固定数写死也行（写死更容易调通）

import random
answer = random.randint(1, 20)


# ===== 步骤 2：计数器 + 循环 =====
# 提示：count = 0 起步；while True 让它一直猜；break 是出口

count = 0

while True:
    # ===== 步骤 3：问玩家要猜的数 =====
    # 提示：input() 收文本，要算数得 int(input("..."))
    guess = int(input( "your guess number——") )       # ← 先填个占位，别空着

    count = count + 1

    # ===== 步骤 4：三路判断 =====
    # ⚠️ 关键：猜中（相等）那条必须放最前面
    #    因为 first-match-wins——上面有一条命中了，下面的 elif 根本不跑
    if guess > answer:
        print("太大了")
    elif guess < answer:
        print("太小了")
    else:
        print("猜中了！")

        # ===== 步骤 5：猜中就退出 =====
        # 提示：这里只写 break 就够，外面的收尾会自动接上
        break

# ===== 步骤 6：游戏结束汇报 =====
# 提示：用累加器数出来的 count，打印"你一共猜了 N 次"
print(f"你一共猜了 {count} 次")
