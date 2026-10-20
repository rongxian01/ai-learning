# quiz.py —— 清账专用：写完这 10 条，第 7/8/10/11 项一起勾
# 规则：独立写，不许抄示范文件；每写一条跑一次，全对才算数

# 1. 定义 name = "容贤"、age = 25、height = 1.75
name = "容贤"
age = 25
height = 1.75
# 2. 用 f-string 打印：你好容贤，你今年25岁
print(f"你好{name},你今年{age}岁")
# 3. 把 age 转成文本，用 + 拼接打印：我25岁了
print("我" + str(age) + "岁了")
# 4. 把文本 "3.14" 转成 float，加 0.01 后打印
print(float("3.14") + 0.01)
# 5. 打印 int(3.99) 的结果，亲眼验证砍尾
print(int(3.99))
# 6. 用 f-string + :.2f 打印 height（1.75）
print(f"身高{height:.2f}米")
# 7. input 问"你学f校叫什么？"，打印：欢迎来自XX的同学
school = input("你学校叫什么？")
print(f"欢迎来自{school}的同学")
# 8. input 问年f龄，转成 int，打印：明年你XX岁
age = input("你多大了？")
print(f"明年你{int(age) + 1}岁")
# 9. 打印 7 % 2 和 8 % 2（奇偶判断）
print(7 % 2, 8 % 2)
# 10. 用 // 和 % 把 135 秒拆成"X分X秒"打印
total = 135
print(f"{total // 60}分{total % 60}秒")