# listquiz.py —— 第 18 项 列表练习
# 规则同前：先自己写，跑 python listquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 18 才算过

# 题 1：索引从 0 开始（热身·最容易栽）
# 下面这个列表，取出"橙子"和最后一个"葡萄"，分别打印
# 提示：橙子是第 3 个，但它的号不是 3
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# —— 在下面写 ——
print(fruits[2])
print(fruits[-1])
# 题 2：建一个自己的清单
# 建一个你手机里的 APP 列表（至少 4 个），做三件事：
#   ① 打印一共有几个
#   ② 追加一个你想装还没装的
#   ③ 删掉一个你早就想卸的
# —— 在下面写 ——
APPs = ["taobao","tiktok","twitter","claude"]
print(len(APPs))
APPs.append("deepseek")
APPs.remove("claude")
print(APPs)
# 题 3：取一段（切片）
# nums = [10, 20, 30, 40, 50]
# 取出中间三个（20, 30, 40），打印出来
# 提示：[头:尾] 含头不含尾——和 range 一个规矩
# —— 在下面写 ——
nums = [10, 20, 30, 40, 50]
print(nums[1:4])


# 题 4（验收题）：数字清单大改造
# nums = [5, 3, 9, 1, 7]
# 依次做：
#   ① 把 10 加到末尾
#   ② 把 0 插到最前面
#   ③ 取出最后那个数，打印它
#   ④ 删掉值为 3 的那个数
#   ⑤ 最后打印整个列表
# 提示：每做一步都可以 print 一下看看列表变成什么样了
# —— 在下面写 ——
nums = [5, 3, 9, 1, 7]
nums.append(10)
nums.insert(0,0)
last = nums.pop()    # 取出 10
print(last)          # 打印 10
print(nums)
nums.remove(3)
print(nums)


# ============ 参考答案（做完再对）============
# 1. print(fruits[2])
#     print(fruits[-1])       # 或 fruits[3]
#
# 2. apps = ["微信", "B站", "地图", "网易云"]
#     print(len(apps))
#     apps.append("飞书")
#     apps.remove("地图")
#
# 3. nums = [10, 20, 30, 40, 50]
#     print(nums[1:4])        # 头 1 尾 4——含 20 不含 50
#
# 4. nums = [5, 3, 9, 1, 7]
#     nums.append(10)         # [5, 3, 9, 1, 7, 10]
#     nums.insert(0, 0)       # [0, 5, 3, 9, 1, 7, 10]
#     last = nums.pop()       # 取出 10
#     print(last)
#     nums.remove(3)          # [0, 5, 9, 1, 7]
#     print(nums)
#
# ⚠️ 题4 最容易错的一步：remove(3) 是按"值"删，不是按号删
#     nums.remove(3) 找的是值为 3 的那一项，不管它在几号位
