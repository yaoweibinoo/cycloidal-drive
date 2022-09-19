## 此代码用于生成摆线针轮驱动方程 X 和 Y
## 与 Solidworks 一起使用
## 生成摆线盘草图
'''
# 减速比 14:1  7015
R = 42
E = 1.5    #E < R/N
Rr = 4
N = 15
'''

# 减速比 19:1  5010/5015
R = 28
E = 1      # E < R/N
Rr = 4
N = 20

# 定义
# R : 滚子 PCD 的半径（节圆直径）
# E : 从输入轴到摆线盘的偏心距（或偏移）
# Rr : 滚子的半径
# N : 滚子数量
# 减速比为 N-1:1

R_EN = R/(E*N)
NmE = N-E
_N = 1-N


#X = (R*cos(t))-(Rr*cos(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
#Y = (-R*sin(t))+(Rr*sin(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))


X = "({}*cos(t)) - ( {}*cos( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) - ({}*cos({}*t)) ".format(R,Rr,_N,R_EN,_N,E,N)
Y = "(-{}*sin(t)) + ( {}*sin( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) + ({}*sin({}*t)) ".format(R,Rr,_N,R_EN,_N,E,N)


print(X)
print(Y)