# swim.py —— 第 13 项验收：用 and/or/not 拼一个组合条件
#
# 任务：判断今天适不适合户外游泳。
#   输入：水温 temp（数字）、是否阴天 is_cloudy（1=阴天 / 0=晴天）
#   规则：水温 ≥ 26 且 不是阴天 → "适合游"；否则 → "不合适"
#
# 要求（四条）：
#   1. input() 收两个值，都 int() 转成数字
#   2. 组合条件里必须用上 and 和 not（"不是阴天"就是 not is_cloudy）
#   3. if / else 两条路
#   4. 每行加人话注释
#
# 自测三个组合：
#   temp=28, is_cloudy=0 → 适合游（水温够 且 晴天）
#   temp=28, is_cloudy=1 → 不合适（水温柔和但阴天，not 把 1 翻成假）
#   temp=20, is_cloudy=0 → 不合适（水温不够；注意这情况 and 左边就假了，右边根本不看=又短路了）
#
# 写完跑：python swim.py
#
# 另外用一句话回答：什么是"短路求值"？（你刚亲眼见过它挡下一次崩溃）
#
# ==================== 在下面写你的代码 ====================
temp = int(input("today water temp?"))
is_cloudy = int(input("阴天吗？1=阴天，0=晴天："))
if temp >= 26 and not is_cloudy:
    print("swim is ok")
else:
    print("swim is no ok")