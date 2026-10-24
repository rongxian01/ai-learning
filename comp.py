# comp.py —— 第 24 项 推导式概念课
# 规则同前：从头跑到尾，看每幕的输出；看完再开 compquiz.py 自己写
# 一句话：推导式 = 把"建空容器 + for 循环往里塞"的四行，压成一行

# ── 第 1 幕：同一个东西，两种写法 ──
# 要 1-5 的平方表

# 循环版（四行）：
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x * x)
print(squares_loop)          # [1, 4, 9, 16, 25]

# 推导版（一行）：
squares_comp = [x * x for x in range(1, 6)]
print(squares_comp)          # [1, 4, 9, 16, 25]  ← 一模一样

# ── 第 2 幕：拆开看三件套 ──
# [要装的料   for x in 来源]
#   ↑            ↑      ↑
#  装什么      逐个拿   从哪拿
# 读法：从 for 那截读起（跟 for 循环一个读法），读完了回头看前面装什么
print([x * 10 for x in range(3)])     # [0, 10, 20]

# ── 第 3 幕：配 if 过滤 ──
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 只要偶数：if 站末尾，当"门卫"
evens = [x for x in nums if x % 2 == 0]
print(evens)                 # [2, 4, 6, 8, 10]

# 对比：不用推导的老写法（过滤 + 装，两个活分三层）
evens_loop = []
for x in nums:
    if x % 2 == 0:
        evens_loop.append(x)
print(evens_loop)            # 一样的结果，四行 vs 一行

# ── 第 4 幕：字典推导 ──
# 列表推导装一队值；字典推导装一键值对——冒号左边是键，右边是值
words = ["螺栓", "螺母", "垫片"]
lengths = {w: len(w) for w in words}
print(lengths)               # {'螺栓': 2, '螺母': 2, '垫片': 2}

# 来源是 items()：键不变、值翻倍
prices = {"螺栓": 9.9, "螺母": 2.5}
doubled = {k: v * 2 for k, v in prices.items()}
print(doubled)               # {'螺栓': 19.8, '螺母': 5.0}

# ── 第 5 幕：推导式是"值"，不是"动作" ──
# 连回 item 19：切片 [::2] 飘在外面是 SyntaxError（动作 ≠ 值）
# 推导式不一样——它天生就是个值，哪都能站：
print([x * 10 for x in range(3)])                    # 直接进 print
print(len([x for x in range(10) if x % 2 == 0]))     # 直接进 len → 5

# ── 第 6 幕：什么时候别硬塞 ──
# 推导版好读，是因为"一个意图一行说完"。以下情况老实写循环：
# ① 要分多步才算出来的（先筛、再换、再统计）
# ② 装什么要带 else 分支（[x if 条件 else y for ...] 能写，初学先别碰）
# ③ 套三层以上——那是可读性地狱，读代码的人想打人
# 口诀：**一行说得清的意图才用推导；说不清的留给 for**

# ── 第 7 幕：全家福 + 预告 ──
# [x ...]       列表推导 → 装一队值
# {x ...}       集合推导 → 装一队不重复（见过就行）
# {k: v ...}    字典推导 → 装一键值对
# 预告 item 25：词频统计的"一行流"就是字典推导——
#   counter = {ch: word.count(ch) for ch in set(word)}
#   （set(word) 先去重，同一个字母不重复算）
print({ch: "design".count(ch) for ch in set("design")})
