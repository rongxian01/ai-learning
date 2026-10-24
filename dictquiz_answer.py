# dictquiz_answer.py —— 第 20 项 字典 · 带知识点注释的完整答案
# 用法：先自己做 dictquiz.py，做完再对照这个文件
# 每一行注释都是知识点，不是废话


# ═══════════ 题 1：按键取值（不是按号！）═══════════

book = {"title": "设计心理学", "author": "诺曼", "price": 59}
# ↑ 建字典：花括号 {} 里放"键: 值"，逗号隔开
#   冒号【左】永远是键，冒号【右】永远是值，写下去那一刻就定死

print(book["title"])        # 方括号里填【键的名字】，不是第几号
                            # 键是字符串，所以要带引号
print(book["author"])
print(book["price"])

print(len(book))            # len() 数的是"有几对键值对"，这里是 3


# ═══════════ 题 2：get 三连（本项最重要）═══════════

print(book.get("title"))             # 键存在 → 和 book["title"] 完全一样
print(book.get("publisher"))         # 键不存在 → 给 None
                                     # None 是 Python 的"空"，不等于 0，也不等于空字符串
print(book.get("publisher", "未填"))  # 键不存在 → 给第二个参数里的兜底值
                                     # ★ 实战就用这个版本

# 对比：book["publisher"] 会直接 KeyError，整个程序停下来
# 而 get 不会崩 —— 所以外部来的数据（配置、表单、接口）一律用 get


# ═══════════ 题 3：增 / 改 / 删 ═══════════

book["price"] = 49          # 键已存在 → 改值
                            # 注意：改和增是【同一个语法】，Python 不问你想要哪个
book["year"] = 2010         # 键不存在 → 新增一对

del book["author"]          # del 后面要写清【删谁】：del 字典名[键]
                            # 写成 del["author"] 会报 SyntaxError: cannot delete literal
                            # （因为 ["author"] 前面没东西，Python 以为你在现场造一个新列表）

print(book)                 # {'title': '设计心理学', 'price': 49, 'year': 2010}
                            # 键按插入顺序保留（Python 3.7 以后）


# ═══════════ 题 4①：in 判断在不在 ═══════════

scores = {"语文": 92, "数学": 88, "英语": 95}

if "数学" in scores:         # in 只回答"在不在"，不告诉你值是多少
    print(scores["数学"])    # 确认在之后，再用方括号取值 → 88
    # 这一行【必须缩进】：缩进 = 归属，它是 if 的"身体"

# 对比：scores.get("数学") 是【取值】不是【判断】
#       它直接给你 88，不会给你 True / False


# ═══════════ 题 4②：items() 遍历 ═══════════

for k, v in scores.items():
    # items() 把每一对键值打包成一个盒子：('语文', 92)
    # k, v 把盒子当场拆开：前面接键，后面接值
    # 一个 for 自己会走完全部三轮，不用写三遍
    print(k, v)              # 语文 92 / 数学 88 / 英语 95


# ═══════════ 题 4③：累加总分 ═══════════

total = 0                    # ① 循环【外面】先归零，只写一次

for v in scores.values():    # 只要值时用 .values()，不用拆包
    total = total + v        # ② 循环【里面】，每轮加一次
                             # 右边先算（上一轮留下的 total + 这一轮的 v），再存回左边

print(total)                 # ③ 循环【外面】打印结果 → 275

# ⚠️ 常见错：total = 0 写在循环后面、累加写在循环外面
#    → 循环结束后 v 停在最后一个值 95，结果变成 0 + 95 = 95


# ═══════════ 题 4④：平均分 ═══════════

print(total / len(scores))   # len(scores) = 3（几对键值对）
                             # / 是真除法，结果是小数 91.66666666666667

# 想要两位小数，两种写法都行：
#   print(round(total / len(scores), 2))          → 91.67
#   print(f"平均分 {total / len(scores):.2f}")     → 平均分 91.67


# ═══════════ 题 5（加分）：词频统计 ═══════════

word = "designscout"
counter = {}                 # 先建一个【空字典】，准备往里装统计结果

for ch in word:              # for 能遍历字符串，一轮一个字
    if ch in counter:        # 这个字母以前出现过吗？
        counter[ch] = counter[ch] + 1   # 出现过 → 在原值上加 1（键存在 = 改）
    else:
        counter[ch] = 1                 # 第一次见 → 记 1（键不存在 = 增）

print(counter)
# {'d': 1, 'e': 1, 's': 2, 'i': 1, 'g': 1, 'n': 1, 'c': 1, 'o': 1, 'u': 1, 't': 1}
# s 出现两次，其余各一次


# 同样的逻辑，用 get 可以压成一行（item 21 要练成肌肉记忆的那招）

counter2 = {}
for ch in word:
    counter2[ch] = counter2.get(ch, 0) + 1
    # get(ch, 0)：有就取原值，没有就当 0 → 再 +1 → 存回去
    # 一行顶掉上面的 if-else 四行

print(counter2)
# 结果和 counter 完全一样
