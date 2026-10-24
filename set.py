# set.py —— 第 22 项 集合（一袋子不重复的名字）
#
# 列表 = 排队：按【第几号】找，可重复
# 字典 = 查规格表：按【名字】找，名字→规格
# 集合 = 来料登记簿：只记【有没有】，同一个料号只登一次
#
# 你做过来料就知道：一箱螺丝里混着重复的料号，
# 登记的时候你不会问"它是第几个"，你只问"这个料号登过没有"
# 集合干的就是这件事

# ============ 第一幕：集合长什么样 ============
# 花括号，但没有冒号——里面是一个个"光名字"，没有配对的值

colors = {"红", "绿", "蓝"}
print("--- 集合内容 ---")
print(colors)                  # 三个颜色，顺序每次可能不一样！
print(type(colors))            # <class 'set'>
print(len(colors))             # 3

# ⚠️ 注意打印顺序：集合是【无序】的，
#    同样的内容，多跑几次顺序可能不同——所以永远别依赖集合的顺序

# ============ 第二幕：看家本领——去重 ============
# 来料登记：同一个料号，只登一次

materials = ["M6", "M8", "M6", "M10", "M8", "M6"]
print("--- 原始来料（6 条，重复一堆）---")
print(materials)

print("--- 登过记之后（只剩 3 个料号）---")
print(set(materials))

# 去重之后还想当列表用 → list(set(...))
unique = list(set(materials))
print("--- 去重后的清单 ---")
print(unique)

# ============ 第三幕：判断在不在 ============
# in 在集合上问"在不在"，和字典一个套路（集合里全是名字，问名字就行）

print("--- 在不在判断 ---")
print("M8 在不在：", "M8" in set(materials))    # True
print("M12 在不在：", "M12" in set(materials))  # False

# ============ 第四幕：交集 & 并集 ============
# 两份名单：两边都有的（交 &）、全部合起来的（并 |）

team_a = {"甲", "乙", "丙"}
team_b = {"丙", "丁", "戊"}

print("--- 交集：两边都有 ---")
print(team_a & team_b)         # {'丙'}

print("--- 并集：合起来（重复的自动合一）---")
print(team_a | team_b)         # 五个

# ============ 第五幕：差集 ============
# 我有、他没有的（减号）

print("--- 差集：甲队独有 ---")
print(team_a - team_b)         # {'甲', '乙'}
print("--- 差集：乙队独有 ---")
print(team_b - team_a)         # {'丁', '戊'}

# ============ 第六幕：增和删 ============
# 集合用 .add() 添加（不是 append！也没有"第几个"可插）

tools = {"扳手", "螺丝刀"}
tools.add("钳子")
print("--- 加了一把钳子 ---")
print(tools)

tools.remove("扳手")           # 删掉一把
print("--- 拿走扳手 ---")
print(tools)

# ⚠️ remove 删一个不在的 → KeyError，程序当场停
# tools.remove("电钻")          # 想见识报错就把这行注释取消，跑一次

tools.discard("电钻")          # discard 删不存在的 → 一声不出，安全版
print("--- discard 一把不在的，平安无事 ---")
print(tools)

# ============ 第七幕：三个坑（踩一个炸一个）============

# 坑 1：集合【无序】——没有"第几个"，不能按号取
# tools[0]                     # TypeError: 'set' object is not subscriptable

# 坑 2：空集合必须写 set()，{} 是空字典！
empty_set = set()
empty_dict = {}
print("--- 两种空的身份 ---")
print(type(empty_set), type(empty_dict))   # <class 'set'> <class 'dict'>

# 坑 3：集合里的元素必须"不会变的"（和字典的键同一个规矩）
# tools.add(["电池", "充电器"])  # TypeError: unhashable type: 'list'
tools.add(("电池", "充电器"))    # 元组不会变，可以进集合
print("--- 元组能进集合 ---")
print(tools)

# ============ 本课小结 ============
# 集合 = 一袋子不重复的名字：只问"有过没有"，不问"第几个、值多少"
# 三大武器：去重 set(名单) / 在不在 in / 交并差 & | -
# 三大坑：无序（没索引）/ 空集合是 set() 不是 {} / 元素必须不可变
