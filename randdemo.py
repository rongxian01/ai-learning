# randdemo.py —— 随机数（random 工具箱）
#
# 今天之前你造数都是 range(0, 20) —— 一串按顺序的名单
# random 是另一个东西：从这堆里"随机抽一个"，每次跑结果都可能不一样
#
# 关键认知：random 是 Python 自带的"标准库"，不是第三方的
#          → 不用 pip install，import 一下就能用
#          （对比：numpy / pandas 这些才要 pip install）

# ===== 第一步：把工具箱搬进工作台 =====
import random

# ===== 第二步：抽一个整数（含头含尾！）=====
print("--- random.randint(1, 20) 连抽 8 次 ---")
for i in range(8):
    n = random.randint(1, 20)
    print(n, end=" ")
print()

# ⚠️ 重点：randint 是【含头含尾】的！
#    randint(1, 20) 能抽到 1，也能抽到 20
#    这和你刚学的 range 正好相反 —— range 是"含头不含尾"
#    所以要 1 到 20 的随机数，randint 写 (1, 20)，range 得写 (1, 21)
print("--- 抽到的最大值可能是 20 吗？---")
big = random.randint(1, 20)
print("这次抽到：", big)
if big == 20:
    print("==> 抽到 20 了！说明 randint 含头含尾")

# ===== 第三步：从一堆东西里随机挑一个 =====
# choice 从"一堆"里挑一个（列表、字符串都行）
print("--- random.choice 从石头剪刀布里随机出拳 ---")
rps = ["石头", "剪刀", "布"]
for i in range(5):
    print(random.choice(rps), end=" ")
print()

# 列表里挑 → 等价于从这堆里随机抽一个
print("--- random.choice(range(1, 21)) 等价于 randint(1, 20) ---")
print("写法A:", random.randint(1, 20))
print("写法B:", random.choice(range(1, 21)))

# ===== 第四步：洗牌（进阶，看看就行）=====
print("--- random.shuffle 洗牌 ---")
cards = ["A", "2", "3", "4", "5"]
random.shuffle(cards)
print(cards)
print("注意：shuffle 是【原地打乱】——它直接改 cards 这张牌本身，不返回新的")

# ===== 坑1：random.randint 的两个参数是闭区间 =====
# randint(1, 20) → 1..20 全都可能
# randint(1, 21) → 1..21，21 也可能跑出来（不是 range 的"不含尾"）
print("--- randint(1, 3) 连抽 12 次，看会不会出 3 ---")
for i in range(12):
    print(random.randint(1, 3), end=" ")
print()

# ===== 坑2：想固定每次都一样？seed =====
# seed = "固定随机种子"，设了它之后 random 的结果就锁死，每次跑都一样
# 调试程序时很有用（不然你调着调着 random 变了，还以为是自己代码改坏了）
print("--- 设了 seed 之后，连跑两次结果一样 ---")
random.seed(42)
print("第一次:", random.randint(1, 100))
random.seed(42)
print("第二次:", random.randint(1, 100))

print()
random.seed(1)
print("不设 seed 再抽:", random.randint(1, 100))
random.seed(2)
print("换个 seed 抽:", random.randint(1, 100))