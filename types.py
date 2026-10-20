# types.py —— 四种基础类型 + 互相转换
# 跑法：python types.py

# 四种类型各一例
name = "容贤"          # str 文本
age = 25               # int 整数
height = 1.75          # float 小数
is_designer = True     # bool 真假

print(type(name), type(age), type(height), type(is_designer))

# 转换 1：str -> int（字符串转数字，内容必须"干净"）
age_text = "25"
age_number = int(age_text)
print(age_number + 1)              # 26，转成数字就能算了

# 转换 2：int -> str（数字转文本，为了拼接）
print("我 " + str(age_number) + " 岁")

# 转换 3：float -> int（小数转整数：直接砍掉小数，不四舍五入！）
print(int(3.99))                   # 3，不是 4

# 转换 4：str -> float
print(float("3.14") + 0.01)        # 3.15

# 坑 1：int("3.14") —— 字符串转 int 不接受小数点
# print(int("3.14"))               # 取消注释跑一次：会炸

# 坑 2："3" + 3 —— 文本和数字不能直接相加
# print("3" + 3)                   # 取消注释跑一次：会炸
