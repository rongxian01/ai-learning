# fstring.py —— f-string：文本拼接的现代写法

name = "容贤"
age = 25
height = 1.75

# 老办法：str() 硬拼，又长又容易漏
print("我是" + name + "，" + str(age) + "岁")

# 新办法：f-string——字符串前加 f，花括号里直接写变量名
print(f"我是{name}，{age}岁")

# 花括号里能写表达式，当场算
print(f"明年我{age + 1}岁")

# 小数位控制：:.2f = 保留 2 位小数
print(f"身高{height:.2f}米")

# 想打真正的花括号？双写 {{ }}
print(f"这是字面量花括号：{{}}")
