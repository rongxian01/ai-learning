# whilequiz.py —— 第 15 项 while 循环练习
# 规则：先自己写，跑 python whilequiz.py 自验，答案在文末——做完再对，别偷看
# ⚠️ while 有死循环风险：忘了让条件往结束走 → 终端刷屏不停 → Ctrl+C 强杀
# 标准：每题独立写对，item 15 才算过

# 题 1：基本 while + 计数器
# 用 while 打印 1 2 3 ... 10（每个一行）
# 提示：count = 1 起步；count <= 10 就转；每圈记得 count = count + 1（忘这行=死循环）
# —— 在下面写 ——
count = 1
while count <= 10:
    print(count)
    count = count +1

# 题 2：while + break（最常用的输入循环模式）
# 让用户反复输入，输入 "quit" 就退出，否则回显"你输了：X"
# 提示：while True: 永远真，靠里面的 if x == "quit": break 收工
# —— 在下面写 ——
while True:
    x = input("write a sentence")
    if x == "quit":
        break
    print("你输了：" + x)

# 题 3：while + continue + 取模
# 打印 1 到 10 里所有的偶数（跳过奇数）
# 提示：奇数用 n % 2 != 0 判断（item 10 学过取模）；奇数就 continue 跳过
# —— 在下面写 ——

n = 0
while n < 10:
    n = n + 1
    if n % 2 != 0:
        continue
    else:
        print(n)


# ============ 参考答案（做完再对）============
# 1. count = 1
#    while count <= 10:
#        print(count)
#        count = count + 1
# 2. while True:
#        x = input("输点啥（quit 退出）：")
#        if x == "quit":
#            break
#        print("你输了：", x)
# 3. n = 0
#    while n < 10:
#        n = n + 1
#        if n % 2 != 0:
#            continue
#        print(n)
