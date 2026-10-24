# dictquiz.py —— 第 20 项 字典练习
# 规则同前：先自己写，跑 python dictquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 20 才算过

# 题 1：热身 · 按键取值（不是按号！）
# 下面这本书记住：字典用【名字】找，不用【第几号】找
book = {"title": "设计心理学", "author": "诺曼", "price": 59}
# 做两件事：
#   ① 分别打印 title、author、price 三个值
#   ② 打印这个字典一共有几对键值对（提示：len）
# —— 在下面写 ——
print(book["title"])
print(book["author"])
print(book["price"])
print(len(book))
# 题 2：★get 三连（item 21 的肌肉记忆，这题最重要）
# 还是上面那本书，做三件事，看清三个输出的差别：
#   ① 打印 book.get("title")              ← 键存在
#   ② 打印 book.get("publisher")          ← 键不存在，没给默认值
#   ③ 打印 book.get("publisher", "未填")   ← 键不存在，给了默认值
# 提示：② 会打印 None（空），③ 会打印"未填"——这就是 get 的两参数意义
# —— 在下面写 ——
print(book.get("title"))
print(book.get("publisher"))
print(book.get("publisher", "未填"))
# 题 3：增 / 改 / 删
# 还是那本书，依次做：
#   ① price 改成 49
#   ② 增加一对 "year": 2010
#   ③ 删掉 author 这一对（提示：del）
#   ④ 打印整个字典
# ⚠️ 记住：改和增是同一个语法 book["xxx"] = 值，键在就改，键不在就增
# —— 在下面写 ——
book["price"] = 49
book["year"] = 2010
del book["author"]
print(book)

# 题 4（验收题）：in 判断 + 遍历 + 累加
scores = {"语文": 92, "数学": 88, "英语": 95}
# 依次做：
#   ① 判断 "数学" 这个键在不在，在就打印它的值
#   ② 用 .items() 遍历，每行打印成这种格式：语文 92
#   ③ 算出总分并打印（提示：先 total = 0，再在循环里一个个加上去）
#   ④ 用 len(scores) 算出平均分并打印
# —— 在下面写 ——
if "数学" in scores:
    print(scores["数学"])

print(scores.items())

total = 0  
for k, v in scores.items():
    print(k, v) 
    total = total + v       
print(total)
avg = total / len(scores)
print(avg)


# 题 5（加分 · item 25 的预告）：数每个字母出现几次
word = "designscout"
# 统计每个字母出现几次，最后打印这个字典
# 提示：和 list 一样，需要先建一个空字典 counter = {}
#       然后 for ch in word: 里判断这个字母在不在 counter 里
#       在 → 原值 +1；不在 → 记 1
# —— 在下面写 ——
counter = {}
for ch in word:          # 外层这个位置，本来就属于 for（生产 ch）
    if ch in counter:    # 里层这个位置，才属于 if（盘问 ch）
        counter[ch] = counter[ch] + 1
    else:
        counter[ch] = 1
print(counter)
# ============ 参考答案（做完再对）============
# 1. print(book["title"])
#     print(book["author"])
#     print(book["price"])
#     print(len(book))            # 3
#
# 2. print(book.get("title"))            # 设计心理学
#     print(book.get("publisher"))        # None  ← 取不到，但没崩
#     print(book.get("publisher", "未填")) # 未填  ← 取不到，给个兜底
#
# 3. book["price"] = 49
#     book["year"] = 2010
#     del book["author"]
#     print(book)
#
# 4. if "数学" in scores:
#         print(scores["数学"])        # 88
#
#     for k, v in scores.items():
#         print(k, v)                  # 语文 92 / 数学 88 / 英语 95
#
#     total = 0
#     for v in scores.values():
#         total = total + v
#     print(total)                     # 275
#
#     print(total / len(scores))       # 91.666...
#
# 5. counter = {}
#     for ch in word:
#         if ch in counter:
#             counter[ch] = counter[ch] + 1
#         else:
#             counter[ch] = 1
#     print(counter)
#     # 或者一行流（item 21 要练的那招）：
#     # counter[ch] = counter.get(ch, 0) + 1
#
# ⚠️ 题2 最容易犯的错：以为 get 和 [] 一样，写成 book.get["publisher"]
#    方括号是取值，圆括号是给 get 传参——两者不能换
