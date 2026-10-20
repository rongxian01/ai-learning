# forquiz.py —— 第 14 项 for 循环练习（明天清醒时写）
# 规则：先自己写对，跑 python forquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题能独立写对，item 14 才算过
# 注意：每题都要写完整的 for 骨架（for 变量 in 东西: + 缩进），别只写一半

# ============ 基础 3 题（item 14 核心）============

# 题 1：range 差一专练
# 用 for + range 打印 0 1 2 3 4 5 6 7 8 9（共 10 个，每个一行）
# 提示：range 里填几？想清楚——你上次就在这想当然栽了
# —— 在下面写 ——

for i in range (10):
    print(i)
# 题 2：遍历列表
# fruits = ["苹果", "香蕉", "橙子"]
# 用 for 逐个打印：吃：苹果 / 吃：香蕉 / 吃：橙子
# —— 在下面写 ——
fruits = ["苹果", "香蕉", "橙子"]
for f in fruits:
    print("吃" + f)
# 题 3：遍历字符串 + input
# 让用户输入一个词，用 for 逐字打印出来（一字一行）
# —— 在下面写 ——
word = input("say a word")
for ch in word:
    print(ch)

# ============ 进阶 2 题（组合活用）============

# 题 4：累加器
# 用 for + range 算 1+2+3+...+100，打印总和
# 提示：循环外先 total = 0，循环里 total = total + i（i 就是每次的那个数）
# —— 在下面写 ——
total = 0
i = 0
for i in range(101): #for i in range(1, 101):
    total = total + i
print(total)

# 题 5：for + if 综合
# scores = [85, 58, 92, 47]
# 用 for 逐个判断：>=60 打印"及格"，否则"挂科"
# 提示：for 里面套 if（缩进再缩一层）
# —— 在下面写 ——
scores = [85, 58, 92, 47]
for i in scores:
    if i >= 60:
        print("及格")
    else:
        print("挂科")

# ============ 参考答案（做完再对）============
# 1. for i in range(10):
#        print(i)                          # range(10)=0-9，含头不含尾（这次别再写 range([0,9])）
# 2. fruits = ["苹果", "香蕉", "橙子"]
#    for f in fruits:
#        print("吃：" + f)
# 3. word = input("输个词：")
#    for ch in word:
#        print(ch)
# 4. total = 0
#    for i in range(1, 101):               # range(1,101)=1到100（两参数写法，item 17 细讲，先见面）
#        total = total + i
#    print(total)                          # 结果 5050
# 5. scores = [85, 58, 92, 47]
#    for s in scores:
#        if s >= 60:
#            print("及格")
#        else:
#            print("挂科")
