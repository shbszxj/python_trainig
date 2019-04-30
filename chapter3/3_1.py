# 3.1 列表是什么
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1 访问列表元素
print(bicycles[0].title())

# 3.1.2 索引从0而不是1开始
print(bicycles[1].title())
print(bicycles[3].title())

# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素
print(bicycles[-1])

# 3.1.3 使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
