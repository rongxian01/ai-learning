# ============================================================
# wordfreq.py —— item 25 综合词频 · 概念课
#
# 目标：一段英文文本 → 每个单词出现几次 → 输出 top 3
# 规矩：不许用 collections.Counter（现成轮子，学习阶段禁坐）
# 自包含铁律：每幕自己备齐数据，不依赖上面几幕——单独复制任何一幕都能跑
#
# 跑通标准：5 幕输出全对，结尾奖牌榜三行
# ============================================================


# ---------- 第 1 幕：文本变单词名单（新本事：split）----------
text = "the cat sat on the mat the cat ran"    # 本幕自备：一段文本
words = text.split()          # 按空格拆，返回名单
print("1. split 拆队:", words)
print("   共", len(words), "个词")

# split 的读法：名单 = 文本.split(分隔符)
#   默认按空格拆；也可以指定："a-b-c".split("-") → ['a', 'b', 'c']
#   连回 item 19：拆出来的也是"排成一队的东西"（列表）


# ---------- 第 2 幕：词频账本（空字典 + for + if/else，已会）----------
words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat", "ran"]   # 本幕自备：单词名单
counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1     # 见过 → +1 存回
    else:
        counts[w] = 1                 # 初见 → 记 1
print("2. 账本:", counts)

# 连回 dictquiz 题 5 七关：for 送货 / if 盘问 / 入库三件套
# 计数从 1 开始 = "含当前这一圈"；不写回 = 白算


# ---------- 第 3 幕：账本一行流（get 默认值，item 21 的用武之地）----------
words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat", "ran"]   # 本幕自备：同一份名单

counts_a = {}                      # 版 A：if/else 手写版
for w in words:
    if w in counts_a:
        counts_a[w] = counts_a[w] + 1
    else:
        counts_a[w] = 1

counts_b = {}                      # 版 B：get 一行流
for w in words:
    counts_b[w] = counts_b.get(w, 0) + 1   # 取不到就当 0，加完存回

print("3. 手写版:", counts_a)
print("   一行流:", counts_b)
print("   两版一样吗:", counts_a == counts_b)

# get(w, 0) 读法："查 w，查到了用真数，查不到用兜底 0"
# 一行流 = if/else 两行的压缩：兜底 0 自动顶"初见"的班，账本一字不差


# ---------- 第 4 幕：奖牌榜 top3（不用 sorted，循环找最大）----------
counts = {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1, "ran": 1}   # 本幕自备：现成账本
counts3 = dict(counts)        # 复印一份再摘（不毁原件——连回切片是看一眼）
for medal in ["金牌", "银牌", "铜牌"]:
    best_word = ""            # 擂主名牌：开扫前空着（占位）
    best_count = 0            # 擂主席绩：垫底，保证第一个候选能当选
    for w, c in counts3.items():    # items() 送盒子，两个变量拆盒子
        if c > best_count:    # 出现更大的 → 更新擂主
            best_word = w
            best_count = c
    print("4.", medal, ":", best_word, best_count, "次")
    del counts3[best_word]    # 摘掉擂主，下一轮找下一个
    print("   摘完剩下:", counts3)   # 每颁一块就打一次：账本越摘越少（亲眼验证"名次是摘出来的"）
print("   原件还好吗:", counts)

# 拆解奖牌榜五件套：
#   复印 counts3      ← 摘奖牌会毁数据，先复印（dict(x) 是复印机）
#   哨兵 best_count=0 ← 垫底：词频最少 1 次，0 起步谁都打得过
#   items() 拆包      ← 连回 tuplequiz 题 4：w 当名牌、c 拿来比
#   del 摘掉          ← 连回 dictquiz 题 3：del d["键"] 删这一对
#   缩进归属          ← del 站外层（每块奖牌摘一次），掉进内层就掏空账本


# ---------- 第 5 幕：Counter 长什么样（认识，不许坐）----------
# 标准库里有现成轮子：
#   from collections import Counter
#   Counter(words).most_common(3)
# 学习阶段禁坐的原因：轮子会掩盖账本原理，而面试官要听的是原理
# 知道它存在 + 能手写 = 合格；只会 import = 花架子
