# tuplequiz.py —— 第 23 项 元组练习
# 规则同前：先自己写，跑 python tuplequiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 23 才算过

# 题 1（热身）：建元组 + 索引 + 切片
# 场景：一颗螺栓的规格书，三项：料号 "M6"、名称 "螺栓"、表面处理 "镀锌"
spec = ("M6", "螺栓", "镀锌")
# 做四件事：
#   ① 打印料号（0 号位）
#   ② 打印最后一项（提示：负索引）
#   ③ 切片取前两样，打印（提示：含头不含尾）
#   ④ 打印这个元组一共有几样（提示：len）
# —— 在下面写 ——
print(spec[0])
print(spec[-1])
print(spec[0:2])
print(len(spec))
# 题 2（对比题）：列表是草稿本，能改
# 还是同样三样规格，这次建成列表 bom = ["M6", "螺栓", "镀锌"]
# 做两件事：
#   ① 把第一样改成 "M8"（列表直接下标赋值）
#   ② 打印改完的 bom
# 想一想（不用写代码）：同样的事对元组干会发生什么？（概念课第 8 幕你撞过）
# —— 在下面写 ——
bom = ["M6", "螺栓", "镀锌"]
bom[0] = "M8"
print(bom)
# 元组直接炸
# 题 3：拆包
# 场景：平面图上一个点的坐标
point = (3, 4)
# 做三件事：
#   ① 一行拆包：x, y = point
#   ② 用 f-string 打印：x=3, y=4
#   ③ 再来一个装三样的：name, price, qty = ("螺栓", 9.9, 100)，打印 name price qty
# —— 在下面写 ——
x, y = point
print(f"x={x},y={y}")
name, price, qty = ("螺栓", 9.9, 100)
print(f"name={name},price={price},qty={qty}")
# 题 4（验收题）：元组当字典的键
# 场景：仓库格子坐标 → 放的货。坐标是"不会变"的，正好当键
# 做四件事：
#   ① 建空字典 locations = {}
#   ② 存两条：locations[(0, 0)] = "角钢"、locations[(1, 2)] = "螺栓"
#   ③ 打印 locations[(1, 2)]（按坐标取货）
#   ④ 用 items() 遍历，每行打印成：坐标 (0, 0) 放着 角钢
# 思考题（答案写在注释里，不用跑）：如果键写成列表 locations[[0, 0]] 会怎样？
#   提示：想想 item 20 学的"键必须不会变"
# —— 在下面写 ——
locations = {}
locations[(0, 0)] = "角钢"
locations[(1, 2)] = "螺栓"
print(locations[(1, 2)])
for k, v in locations.items():
    print(f"坐标{k}放着{v}")
# ============ 参考答案（做完再对）============
# 1. print(spec[0])        # M6
#    print(spec[-1])       # 镀锌
#    print(spec[:2])       # ('M6', '螺栓')
#    print(len(spec))      # 3
#
# 2. bom = ["M6", "螺栓", "镀锌"]
#    bom[0] = "M8"
#    print(bom)            # ['M8', '螺栓', '镀锌']
#    # 元组同样干 → TypeError: 'tuple' object does not support item assignment
#
# 3. x, y = point
#    print(f"x={x}, y={y}")        # x=3, y=4
#    name, price, qty = ("螺栓", 9.9, 100)
#    print(name, price, qty)       # 螺栓 9.9 100
#
# 4. locations = {}
#    locations[(0, 0)] = "角钢"
#    locations[(1, 2)] = "螺栓"
#    print(locations[(1, 2)])      # 螺栓
#    for coord, name in locations.items():
#        print(f"坐标 {coord} 放着 {name}")
#    # 键写列表 → TypeError: unhashable type: 'list'
#    # （列表会变，不能当键；元组不会变，才能当键）
