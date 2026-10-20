# nestedquiz.py —— 第 16 项 嵌套循环练习
# 规则同前：先自己写，跑 python nestedquiz.py 自验，答案在文末——做完再对，别偷看
# 标准：每题独立写对，item 16 才算过

# 题 1：矩形星星阵（热身·双层缩进）
# 打印 3 行、每行 4 个星号，用嵌套循环写
# 提示：外层管"行"（range(3)），内层管"列"（range(4)）；内层 print("*", end="")，外层体末尾 print() 换行
# —— 在下面写 ——
for i in range(3):
    for j in range(4):
        print("*",end="")
    print()


# 题 2：坐标矩阵（理解圈套圈的转动顺序）
# 外层 i 走 1-2，内层 j 走 1-3，打印成两行三列：
# 1,1 1,2 1,3
# 2,1 2,2 2,3
# 提示：每格 print(f"{i},{j}", end=" ")，外层末尾 print()
# —— 在下面写 ——
for i in range(1,3):
    for j in range(1,4):
        print(f"{i},{j}", end=" ")
    print()

# 题 3：九九乘法表（终级目标·本项验收题）
# 输出 1×1=1 到 9×9=81 的下三角表，每行一条，列间两空格，格式 1×2=2
# 提示三件套：① 外层 range(1,10) ② 内层 range(1, 外层变量+1)——+1 别忘了（含头不含尾）
#           ③ 每格 print(..., end="  ")，内层结束后 print() 换行（这行的缩进在外层体里，4 格！）
# —— 在下面写 ——
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}", end="  ")
    print()

# ============ 参考答案（做完再对）============
# 1. for i in range(3):
#        for j in range(4):
#            print("*", end="")
#        print()
#
# 2. for i in range(1, 3):
#        for j in range(1, 4):
#            print(f"{i},{j}", end=" ")
#        print()
#
# 3. for i in range(1, 10):
#        for j in range(1, i + 1):
#            print(f"{j}×{i}={i * j}", end="  ")
#        print()
