# import turtle

# name = input("What is your name?")
# print("Hello, " + name + "!")

# turtle.speed(5)
# turtle.goto(0,0)
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(100)

# turtle.home()
# turtle.circle(50,270) # turtle包在python3可能不兼容

# 打印圆的周长: (注释)
pi = 3.14
radius = 6
print(2 * pi * radius)

# 'Let\'s go!' 对引号进行转义

print("Hello,\nworld") # \n表示换行

print('''This is a very long string. It continues here.
And it's not over yet. "Hello, world!"
Still here.''') # 三引号表示长字符串s

print(r"C:\nowhere")

print(r'This is illegal\\')
print(r'C:\Program Files\foo\bar' '\\')
print(r'This is illegal' '\\')