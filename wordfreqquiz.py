# wordfreqquiz.py —— 第 25 项 综合词频练习
# 规则同前：先自己写，跑 python wordfreqquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：三题独立写对，item 25 才算过（模块 C 收官）

# 题 1：split 热身（新本事）
sentence = "python is fun python is powerful"
#   ① 用 .split() 拆成单词名单，打印
#   ② 打印第 2 个词（提醒：索引从 0 开始）
#   ③ 打印一共几个词
# —— 在下面写 ——
print(sentence.split())
s = sentence.split()
print(s[1]) 
print(len(s)) 
# 题 2：词频账本（不许用 Counter）
words2 = ["a", "b", "a", "c", "b", "a"]
#   用 for + if/else 手写版，建成 {词: 次数}，打印
#   （提示：连回 dictquiz 题 5——空字典当账本、for 送货、if 盘问、入库）
# —— 在下面写 ——
counts = {}
for w in words2:
    if w in counts:
        counts[w] = counts[w]+1
    else:
        counts[w] = 1
print(counts)
# 题 3（验收题）：完整 top 3（不许用 Counter，不许用 sorted）
text3 = "data science is fun data is powerful data science rules"
#   ① 统计词频（账本或一行流都行）
#   ② 输出次数 top 3：奖牌榜套路——找最大 → 记下 → 摘掉 → 再找（连回 wordfreq.py 第 4 幕）
#   （提醒：摘奖牌前先复印账本，别毁原件）
# —— 在下面写 ——
count = {}
w1 = text3.split()
for ch in w1:
    if ch in count:
        count[ch] = count[ch]+1
    else:
        count[ch] = 1
print(count)
board = dict(count)
for medal in ["金牌", "银牌", "铜牌"]:
    best_word = ""
    best_count = 0
    for w, c in board.items():
        if c > best_count:
            best_word = w
            best_count = c
    print(medal, ":", best_word, best_count, "次")
    del board[best_word]

# ============ 参考答案（做完再对）============
# 1. ① words = sentence.split()          → ['python','is','fun','python','is','powerful']
#    ② print(words[1])                    → 'is'
#    ③ print(len(words))                  → 6
#
# 2. counts = {}
#    for w in words2:
#        if w in counts:
#            counts[w] = counts[w] + 1
#        else:
#            counts[w] = 1
#    print(counts)                         → {'a': 3, 'b': 2, 'c': 1}
#
# 3. counts3 = {}
#    for w in text3.split():
#        counts3[w] = counts3.get(w, 0) + 1
#    board = dict(counts3)
#    for medal in range(3):
#        best_word = ""
#        best_count = 0
#        for w, c in board.items():
#            if c > best_count:
#                best_word = w
#                best_count = c
#        print(best_word, best_count)
#        del board[best_word]
#    → data 3 / science 2 / is 2
#    注意：science 和 is 并列 2 次——奖牌榜取账本里先到的（字典保序），两种顺序都算对，
#    但要能说清"并列时谁上榜全看遍历顺序"（集合才乱，字典按插入序是稳的）
