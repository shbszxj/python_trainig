# 3.2修改、添加和删除元素
# 3.2.1 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
# 在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.2.3 在列表中删除元素
# 使用del语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# 使用方法pop()删除元素
# 方法pop（）可删除列表末尾的元素，并让你能够接着使用它
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 弹出列表中任何位置处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle_remove = 'yamaha'
motorcycles.remove(motorcycle_remove)
print(motorcycles)
