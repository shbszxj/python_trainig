# 组织列表
# 3.3.1 使用方法sort（）对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# 现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序
print(cars)
# 按与字母顺序相反的顺序排列列表元素
cars.sort(reverse=True)
print(cars)

# 3.3.2 使用函数sorted（）对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_temp = sorted(cars)
print(cars_temp)
print(cars)

# 3.3.3 倒着打印列表
# 方法 reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用 reverse() 即可
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# 3.3.4 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
