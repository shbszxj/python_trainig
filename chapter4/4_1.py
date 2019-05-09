# 第四章操作列表
# 4.1遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4.1.1 深入研究循环
# 使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表

# 4.1.2 在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# 在 for 循环中，想包含多少行代码都可以。
# 在代码行 for magician in magicians 后面，每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次。
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# 4.1.3 在for循环结束后执行一些操作
# 在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
