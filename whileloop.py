# whileloop.py —— while 循环：条件还在，就一直干
#
# for = 一批已知东西逐个干（你知道有几个）；
# while = 条件还成立就一直干（干几轮看条件，事前不知道）。
# 类比：for 像数着 10 张图纸一张张审；while 像"客户不满意就继续改"——改几轮看客户。

# ============ 基本式：计数器 ============
count = 0
while count < 5:               # 只要 count < 5，就一直转
    print("第" + str(count) + "圈")
    count = count + 1          # 关键！让 count 变大，条件才会有一天不成立
print("转完，count =", count)

# ============ break：数到 7 就收工 ============
n = 0
while n < 10:
    n = n + 1
    if n == 7:
        print("数到 7，收工！")
        break                  # 立刻跳出整个 while，后面不看了
    print(n)

# ============ continue：1到5，跳过 3 ============
m = 0
while m < 5:
    m = m + 1
    if m == 3:
        continue               # 跳过这一圈剩下的，直接进下一圈
    print(m)

# ============ ⚠️ 死循环长这样（别真跑！）============
# c = 0
# while c < 5:
#     print("永远转")           # 忘了 c = c + 1 → c 永远是 0 → 条件永远真 → 刷屏不停
# 死循环特征：终端疯狂输出停不下来。解法：Ctrl+C 强杀。
