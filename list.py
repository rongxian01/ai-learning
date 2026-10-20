# list.py —— 第 18 项 列表（模块 C 开门）
#
# 今天之前：一个变量 = 一个盒子，装一个数
# 今天开始：一个变量 = 一整个柜子，里面按号排一堆东西
#
# 类比（你做过的电梯）：电梯楼层从 1 层开始数
#                            Python 列表从 0 号开始数
#                            —— 这是今天唯一的大坑，先记住它

# ============ 第一幕：建一个列表 ============
# 方括号 [] 表示"这是一堆"，逗号隔开每一项
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("--- fruits 里现在有：---")
print(fruits)
print("一共几个：", len(fruits))

# ============ 第二幕：按号取东西（索引）============
# ⚠️ 号从 0 开始！第一个是 [0]，不是 [1]
print("--- 按号取（注意从 0 开始）---")
print("第 0 号位：", fruits[0])
print("第 1 号位：", fruits[1])
print("第 2 号位：", fruits[2])
print("最后一个：", fruits[-1])     # -1 是倒数第一，不用数有几个

# 数有几个 vs 最后一个的号，差 1
print("--- len 和索引的关系 ---")
print("一共", len(fruits), "个，所以最后一个的号是", len(fruits) - 1)

# ============ 第三幕：往里加 ============
print("--- append 追加到末尾 ---")
fruits.append("西瓜")
print(fruits)

print("--- insert 插到指定位置 ---")
fruits.insert(1, "草莓")     # 插到 1 号位，后面的统统往后让
print(fruits)

# ============ 第四幕：往外拿 / 删 ============
print("--- pop 拿出来（不写号 = 拿最后一个）---")
last = fruits.pop()
print("拿出来的是：", last)
print("剩下的：", fruits)

print("--- pop(0) 拿第一个 ---")
first = fruits.pop(0)
print("拿出来的是：", first)
print("剩下的：", fruits)

print("--- remove 按内容删（不用管它在几号）---")
fruits.remove("香蕉")
print(fruits)

# ============ 第五幕：切片（一次取一段）============
# [头:尾] 含头不含尾——和 range 一个规矩！
print("--- 切片 [1:3] 含头不含尾 ---")
nums = [10, 20, 30, 40, 50]
print("原列表：", nums)
print("取 [1:3]：", nums[1:3])      # 20, 30 —— 30 在，40 不在
print("取 [:2]：", nums[:2])        # 从头到 2 号位之前 = 10, 20
print("取 [2:]：", nums[2:])        # 从 2 号位到最后 = 30, 40, 50
print("取 [-2:]：", nums[-2:])      # 最后两个

# ============ 第六幕：for 遍历（你已经会了）============
# 列表就是你 item 11 学的"三种可迭代"里第一种
print("--- for 挨个点名 ---")
for f in fruits:
    print("水果：", f)

# ============ 坑1：号超了 → IndexError ============
print("--- 坑1：号超了 ---")
small = ["a", "b"]
print("small[0] =", small[0])
# print(small[2])   # ← 这行会崩：IndexError: list index out of range
print("small 只有", len(small), "个，号只到", len(small) - 1)
print("small[2] 会崩：IndexError: list index out of range")

# ============ 坑2：remove 不存在的东西 → ValueError ============
print("--- 坑2：删不存在的东西 ---")
# fruits.remove("柠檬")   # ← 这行会崩：ValueError: list.remove(x): x not in list
print("删一个列表里没有的'柠檬'：ValueError")

# ============ 坑3：pop 是"拿出来"，不是"看看" ============
print("--- 坑3：pop 会改变列表本身 ---")
demo = ["一", "二", "三"]
taken = demo.pop()        # 拿出来 → 列表少一个
print("拿出来的是：", taken)
print("列表变了：", demo)   # ← 注意：demo 已经不是原来的三个了