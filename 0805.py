print("hello world")

result1 = 2 * 3
print(result1)

result2 = 53672 + 235253
print(result2)

result3 = 1 / 2 # 浮点数：带小数点的数字
print(result3)

result4 = 1 // 2 # //是取余数
print(result4)

result5 = -3 ** 2 # 先算乘方，再加负号

input("The meaning of life:") # 没有存储用户互动的值
result6 = input("The meaning of life:") # 16行和17行是一个整体，用户input的值会存储为result5并且打印出来返回给用户；只有第16行的话在终端输出结果看起来和第15行是一样的
print(result6)

x = input("x: ")
y = input("y: ")
print(int(x) * int (y)) # int将字符串转换为整数

result7 = pow(2,3) # 执行乘方运算，相当于**
print(result7)

result8 = 10 + pow(2,3 * 5) / 3.0
print(result8)

result9 = abs(-10) # abs计算绝对值
print(result9)

result10 = round(2 / 3) # round将浮点数圆整为与之最接近的整数
print(result10)

import math
result11 = math.floor(32.9) # floor函数包含在模块math中，表示向下圆整；或者在上一行直接用from math import floor，就可以在调用函数时不指定模块前缀写成result11 = floor(32.9)就行
print(result11)
result12 = int(32.9) # 将数字转化为整数
print(result12)

from math import ceil
result13 = ceil(32.3) # ceil返回大于或等于给定数的最小整数(向上圆整)
print(result13)

from math import sqrt
result14 = sqrt(9)
print(result14)
