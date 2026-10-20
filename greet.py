# greet.py —— 第一次和程序对话
# 跑法：python greet.py

name = input("你叫什么名字？ ")      # 弹问题、等你打字、收答案
age = input("你多大了？ ")

print(f"你好{name}！")
print(f"你今年{age}岁")

# 想对年龄做计算？先转数字——input 收回来的永远是文本
next_age = int(age) + 1
print(f"明年你{next_age}岁")
