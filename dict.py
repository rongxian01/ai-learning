# dict.py —— 第 20 项 字典（按键查值，不按号）
#
# 列表 = 排队：按【第几号】找
# 字典 = 查规格表：按【名字】找
#
# 你做工业设计见过的物料表（BOM）就是字典：
#   零件名 → 规格/价格
#   "M6螺丝" → "10mm, 0.2元"
# 没有"第几行"的概念，你只关心"这个名字对应什么"

# ============ 第一幕：建一个字典 ============
# 花括号 {} 里放"键: 值"，逗号隔开
# 键（key）  值（value）
student = {
    "name": "容贤",
    "age": 25,
    "major": "工业设计",
    "school": "浙江大学",
}
print("--- 整个字典 ---")
print(student)

# ============ 第二幕：按键取值（不是按号！）============
print("--- 按键取值 ---")
print("name  →", student["name"])
print("age   →", student["age"])
print("major →", student["major"])

# ⚠️ 对比列表：列表用号，字典用名字
#    fruits[0]        ← 列表：第 0 号
#    student["name"]  ← 字典：name 这个名字

# ============ 第三幕：★get —— 取不到也不崩 ============
# 直接 student["phone"] 会崩 KeyError
# get 的好处：取不到给个默认值，程序继续跑
print("--- get 的两个参数 ---")
print('student["name"]        =', student["name"])
print('student.get("name")    =', student.get("name"))
print('student.get("phone")   =', student.get("phone"))          # 没写默认值 → None
print('student.get("phone", "未填") =', student.get("phone", "未填"))  # 写了默认值 → "未填"

# 这就是"安全取值"：表单没填的字段、配置里没有的项，用 get 不会炸

# ============ 第四幕：增 / 改 / 删 ============
print("--- 改：键已存在 ---")
student["age"] = 26          # age 已存在 → 改值
print(student["age"])

print("--- 增：键不存在 ---")
student["phone"] = "138xxxx"  # phone 不存在 → 新增一对
print(student)

print("--- 删 ---")
del student["major"]          # 删掉这一对
print(student)

# ⚠️ 注意：改和增是【同一个语法】——d[key] = 值
#    键在 → 改；键不在 → 增。Python 不问你"是想改还是想加"

# ============ 第五幕：in 判断"有没有这个键"============
print("--- in 判断键 ---")
if "phone" in student:
    print("有 phone 这个键，值是", student["phone"])
if "major" not in student:
    print("major 已经被删了")

# 实战用法：先用 in 探一下，再决定要不要取值 —— 这是 get 之外的第二道保险

# ============ 第六幕：三种遍历 ============
scores = {"语文": 92, "数学": 88, "英语": 95}

print("--- .keys() 只要键 ---")
print(scores.keys())
for k in scores.keys():
    print(k, end=" ")
print()

print("--- .values() 只要值 ---")
print(scores.values())
for v in scores.values():
    print(v, end=" ")
print()

print("--- .items() 键值成对（最常用）---")
print(scores.items())
for k, v in scores.items():
    print(f"{k}：{v}分")

# ⚠️ 直接 for x in scores 遍历的是【键】，不是值
print("--- for x in scores 拿到的是键 ---")
for x in scores:
    print(x, end=" ")
print()

# ============ 坑1：取不存在的键 → KeyError ============
print("--- 坑1：直接取不存在的键 ---")
print("student 现有键：", list(student.keys()))
# student["email"]   # ← 这行会崩：KeyError: 'email'
print('student["email"] 会崩：KeyError —— 用 get 或先 in 判断')

# ============ 坑2：键不能是列表（可变的不能当键）============
# d = {[1,2]: "x"}  → TypeError: unhashable type: 'list'
print("--- 坑2：列表不能当键 ---")
print("{[1,2]: 'x'} 会崩：TypeError: unhashable type: 'list'")
print("（键必须是不会变的——字符串、数字、元组可以；列表不行）")

# ============ 坑3：字典没有"第几个"，不能用号取 ============
print("--- 坑3：字典不是排队的 ---")
# student[0]   # ← KeyError: 0 —— 0 号键不存在
print("student[0] 会崩：KeyError —— 字典按名字找，不按号找")

# ============ 实战小例子：词频统计（item 25 的预习）============
# 这是字典最经典的用法：拿东西当键，数它出现几次
print("--- 实战：数每个字母出现几次 ---")
text = "banana"
counter = {}
for ch in text:
    if ch in counter:
        counter[ch] = counter[ch] + 1     # 见过 → 加一
    else:
        counter[ch] = 1                    # 没见过 → 建一个记 1
print(counter)

# 等价写法（用 get 更简短）—— 这就是 item 21 要练成肌肉记忆的那一招
counter2 = {}
for ch in text:
    counter2[ch] = counter2.get(ch, 0) + 1
print(counter2)