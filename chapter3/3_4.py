# 3.4 使用列表是避免索引错误
motorcycles = ['honda', 'yamaha', 'suzuki']
# 索引 -1 总是返回最后一个列表元素
print(motorcycles[-1])

# 仅当列表为空时，这种访问最后一个元素的方式才会导致错误：
# motorcycles = []
# print(motorcycles[-1])
