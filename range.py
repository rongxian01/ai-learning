# range.py —— 第 17 项 range() 三个参数
# 你已经会用的：range(1, i+1)（两个参数）
# 今天只差第三个参数 step（步长），外加两个方向的坑

# ============ 第一幕：一个参数（起点和步长都锁死）============
# range(5) = 从 0 开始、每次 +1、共 5 个
print("--- range(5) ---")
for x in range(5):
    print(x, end=" ")
print()

# 想从 3 开始？range(5) 做不到，起点被锁死在 0

# ============ 第二幕：两个参数（起点解锁，步长还是锁死 1）============
# range(2, 6) = 从 2 开始、到 6 之前停、每次 +1
# 这就是你天天写的 range(1, i+1)——已会
print("--- range(2, 6) ---")
for x in range(2, 6):
    print(x, end=" ")
print()

# ============ 第三幕：三个参数（步长解禁）============
# range(起点, 终点, 步长)：每次跳多少
print("--- range(0, 10, 2) 每次跳2 ---")
for x in range(0, 10, 2):
    print(x, end=" ")
print()

# 步长 3：0 3 6 9（注意 9 在、10 不在——stop 依然不含）
print("--- range(0, 10, 3) 每次跳3 ---")
for x in range(0, 10, 3):
    print(x, end=" ")
print()

# 步长 1 就是回到老样子（默认）
print("--- range(0, 5, 1) 和 range(5) 一样 ---")
for x in range(0, 5, 1):
    print(x, end=" ")
print()

# ============ 第四幕：步长给负数 = 倒着走 ============
# 起点大、终点小、步长负数 → 从大数往小数倒放
print("--- range(10, 0, -1) 倒着数10到1 ---")
for x in range(10, 0, -1):
    print(x, end=" ")
print()

# 只倒到 5（stop 依然不含 5）
print("--- range(10, 5, -1) ---")
for x in range(10, 5, -1):
    print(x, end=" ")
print()

# ============ 第五幕：坑1 · stop 依然不含（老坑第三次登场）============
# 含头不含尾在带 step 时照样成立：stop 那个数永远出不来
print("--- 坑1：range(1, 10, 2) 里 9 在不在？ ---")
for x in range(1, 10, 2):
    print(x, end=" ")
print()  # 1 3 5 7 9 —— 9 在，因为 9 刚好踩在 stop 前面那一格

print("--- 想打印1到9的奇数：range(1, 10, 2) ---")
for x in range(1, 10, 2):
    print(x, end=" ")
print()

# ============ 第六幕：坑2 · 空 range 不报错，但什么也不干 ============
# 起点比终点小、步长却是正的 → 一圈都转不到，屏幕空空如也
# ⚠️ 这是"不报错 ≠ 干活"家族的-new成员：它安静得很，你可能以为程序坏了
print("--- 坑2：range(5, 10, -1) 会打印什么？ ---")
for x in range(5, 10, -1):
    print(x, end=" ")
print()  # 什么都没有！不报错、不刷屏、就是不出东西

# ============ 第七幕：坑3 · 步长不能是 0 ============
# range(0, 10, 0) → ValueError: range() arg 3 must not be zero
# 想死循环可以，但别用 range 的 step 去死，真要死循环用 while（见笔记 ### 12）
