# setquiz.py —— 第 22 项 集合练习
# 规则同前：先自己写，跑 python setquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 22 才算过

# 题 1（热身）：建集合 + 增 + 删
# 场景：一班工具。建一个集合 tools，里头放 "扳手" 和 "螺丝刀"
# 做四件事：
#   ① 打印这个集合
#   ② 加一把 "钳子"（提示：集合用 add，不是 append）
#   ③ 拿走 "扳手"（提示：remove）
#   ④ 打印改完的集合
# —— 在下面写 ——
tools = {"扳手","螺丝刀"}
print(tools)
tools.add("钳子")
tools.remove("扳手")
print(tools)
# 题 2（本项看家本领 · 去重）
# 场景：来料登记。下面这箱螺丝，料号重复了一堆
materials = ["M6", "M8", "M6", "M10", "M8", "M6"]
# 做三件事：
#   ① 用 set() 去掉重，打印去重后的集合
#   ② 打印原来几条、去重后剩几个（提示：len）
#   ③ 把去重结果倒回列表（list(set(...))），打印
# —— 在下面写 ——
set(materials)
print(set(materials))
print(len(materials))
print(len(set(materials)))
unique = list(set(materials))
print(unique)
# 题 3：判断在不在
# 还是上面那箱料，做两件事：
#   ① 打印 "M8" 在不在（登记过的）
#   ② 打印 "M12" 在不在（没登记过的）
# 提示：in，和字典一个套路
# —— 在下面写 ——
print("在不在:","M8" in set(materials))
print("在不在:","M12" in set(materials))
# 题 4（交并差三连）
# 场景：两位同学想选的课
alice = {"高数", "物理", "英语"}
bob = {"物理", "化学", "英语"}
# 依次做：
#   ① 打印两人都想选的（交集 &）
#   ② 打印两人合起来想选的全部（并集 |）
#   ③ 打印只有 alice 想选的（差集 -）
#   ④ 打印只有 bob 想选的
# —— 在下面写 ——
print(alice & bob)
print(alice | bob)
print(alice - bob)
print(bob - alice)
# 题 5（验收题）：报名号有没有重复？
# 场景：收上来一串报名号，要查出里面有没有人重复报名
signups = ["A01", "B02", "A01", "C03", "B02", "D04"]
# 做两件事：
#   ① 比较"名单条数"和"去重后个数"——一样就是没重复，不一样就是有
#      用 if/else 打印结论：要么 "没有重复"，要么 "有重复"
#   ② 顺手把去重后的名单打印出来看看
# 提示：len(signups) vs len(set(signups))——集合最经典的实战用法，不用循环
# —— 在下面写 ——
a = len(signups)
b = len(set(signups))
if a > b:
    print("有重复")
else:
    print("没重复")
print(set(signups))
# ============ 参考答案（做完再对）============
# 1. tools = {"扳手", "螺丝刀"}
#    print(tools)
#    tools.add("钳子")
#    tools.remove("扳手")
#    print(tools)
#    # ⚠️ 集合打印顺序不定，每次可能不一样，内容对就行
#
# 2. materials = ["M6", "M8", "M6", "M10", "M8", "M6"]
#    print(set(materials))                     # 三个料号（顺序不定）
#    print(len(materials), len(set(materials)))  # 6 3
#    unique = list(set(materials))
#    print(unique)
#
# 3. print("M8" in set(materials))     # True
#    print("M12" in set(materials))    # False
#    # 或者题 2 存过了：unique = set(materials)，再 "M8" in unique
#
# 4. alice = {"高数", "物理", "英语"}
#    bob = {"物理", "化学", "英语"}
#    print(alice & bob)    # {'英语', '物理'}  交集：都想选
#    print(alice | bob)    # 四门全（高数/物理/英语/化学）并集：合起来
#    print(alice - bob)    # {'高数'}           差集：alice 独有
#    print(bob - alice)    # {'化学'}           差集：bob 独有
#
# 5. signups = ["A01", "B02", "A01", "C03", "B02", "D04"]
#    if len(signups) == len(set(signups)):
#        print("没有重复")
#    else:
#        print("有重复")
#    print(set(signups))
#    # 条数 6 ≠ 种数 4 → 有重复
#    # 这就是"len 对比法"：不写循环，一行判断有没有重复
