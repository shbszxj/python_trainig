# 5.2 条件测试
# 5.2.1 检查是否相等
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

# 5.2.2 检查是否相等时不考虑大小写
car = 'Audi'
print(car.lower() == 'audi')

# 5.2.3 检查是否不相等
car = 'Audi'
print(car != 'audi')

# 5.2.4 比较数字
age = 18
print(age == 18)
print(age < 21)
print(age > 21)

# 5.2.5 检查多个条件
# 1. 使用and检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 <= 18)

# 2. 使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

# 5.2.6 检查特定值是否包含在列表中
