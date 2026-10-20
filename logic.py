# logic.py —— 把多个判断拼成大条件：and / or / not + 短路求值
#
# if 一次只能问一个是非题；and/or/not 让你把几个是非题拼成一个更细的条件。
# 人话：
#   and  = 且（两边都真，才真）
#   or   = 或（有一个真，就真）
#   not  = 非（真假翻转）

# ============ 第一部分：and / or / not 各长啥样 ============
age = 25
has_id = True                    # 带身份证了吗

# 场景：进某个场所要"成年 且 带证"
print(age >= 18 and has_id)       # True  —— 两个都真 → 放行
print(age >= 18 and not has_id)   # False —— 成年但没证 → 拦住

# 场景：优惠"是会员 或 今天生日"（有一个就行）
is_vip = False
is_birthday = True
print(is_vip or is_birthday)      # True  —— 有一个真 → 有优惠

# not 就是翻转
print(not has_id)                 # False —— has_id 是真，not 翻成假

# ============ 第二部分：短路求值（Python 的懒人绝技）============
# 规则：and 左边一假 → 右边看都不看；or 左边一真 → 右边看都不看。
# 关键用途：用 and 给危险操作当保镖。

num = 0
# 100 / num 在 num=0 时会崩（0 不能当除数，ZeroDivisionError）。
# 但 and 先算左边 num != 0：num=0 时它是假 → 短路，右边 100/num 压根不执行 → 不崩
if num != 0 and 100 / num > 5:
    print("num 非零，且 100/num 比 5 大")
else:
    print("安全走过——左边没通过，短路拦下了除法，没崩")

# 自己试：把上面 num = 0 改成 num = 20 再跑
#   → 左边 num!=0 是真，才会去看右边 100/20=5，5>5 假 → 还是走 else，但不崩
