# 4.5元祖
# Python将不能修改的值称为不可变的，而不可变的列表被称为元祖
# 4.5.1 定义元祖
dimensions = (200, 50)
print(dimensions)
print(dimensions[1])

# 4.5.2 遍历元祖中的所有值
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元祖变量
dimensions = (200, 50)
dimensions = (400, 100)
print(dimensions)
