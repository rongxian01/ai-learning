# compquiz.py —— 第 24 项 推导式练习
# 规则同前：先自己写，跑 python compquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 24 才算过

# 题 1：列表推导 ×2（本项主打）
# 场景 A：零件边长 → 截面积
edges = [1, 2, 3, 4, 5]
#   ① 用一行列表推导，算出每个边长的平方，打印
# 场景 B：来料单里筛合格件
thickness = [0.5, 1.2, 0.8, 2.0, 0.3, 1.5]
#   ② 用一行列表推导，只留 >= 1.0 的，打印（提示：if 站末尾当门卫）
# —— 在下面写 ——
s = [x * x for x in edges]
print(s)
# 题 2：字典推导 ×2
t = [x for x in thickness if x >= 1.0]
print(t)
# 场景 A：工具清单 → 每样的名字长度
tools = ["扳手", "螺丝刀", "钳子", "电钻"]
#   ① 用一行字典推导，建成 {工具名: 名字长度}，打印
# 场景 B：旧价目表涨价一成
old_prices = {"扳手": 45, "螺丝刀": 12, "钳子": 30}
#   ② 用一行字典推导，每样价格 ×1.1，打印（提示：来源用 .items()，键不变值翻新）
# —— 在下面写 ——
tool_len = {t:len(t) for t in tools}
print(tool_len)

new_prices = {k:v*1.1 for k,v in old_prices.items()}
print(new_prices)
# 题 3（验收题）：一行流去重 + 统计
# 场景：收上来一串报名学校，大小写不统一，还有重复
schools = ["ZJU", "pku", "ZJU", "THU", "pku", "SJTU"]
# 做两件事：
#   ① 用一行集合推导，去重后全部转成大写，打印
#      （提示：字符串变大写用 .upper()，如 "pku".upper() → "PKU"）
new_schools = {s.upper() for s in schools}
print(new_schools)
#   ② 用一行字典推导，建成 {学校: 出现次数}（提示：数数用 .count()）
# —— 在下面写 ——
counts_schools = {c:schools.count(c) for c in set(schools)}
print(counts_schools)
# ============ 参考答案（做完再对）============
# 1. ① areas = [e * e for e in edges]
#       print(areas)                # [1, 4, 9, 16, 25]
#    ② thick = [t for t in thickness if t >= 1.0]
#       print(thick)                # [1.2, 2.0, 1.5]
#
# 2. ① tool_len = {t: len(t) for t in tools}
#       print(tool_len)             # {'扳手': 2, '螺丝刀': 3, '钳子': 2, '电钻': 2}
#    ② new_prices = {k: v * 1.1 for k, v in old_prices.items()}
#       print(new_prices)           # {'扳手': 49.5, '螺丝刀': 13.2, '钳子': 33.0}
#
# 3. ① upper = {s.upper() for s in schools}
#       print(upper)                # {'ZJU', 'PKU', 'THU', 'SJTU'}（顺序不定）
#    ② counts = {s: schools.count(s) for s in set(schools)}
#       print(counts)               # {'ZJU': 2, 'pku': 2, 'THU': 1, 'SJTU': 1}
