# 4.3 创建数值列表
# 4.3.1 使用函数range()
for number in range(1, 5):
    print(number)

# 4.3.2 使用range()创建数字列表
# 要创建数字列表，可使用函数list()将range()的结果直接转换为列表。
numbers = list(range(1, 6))
print(numbers)

# 使用函数range()时，还可指定步长。例如，打印1~10内的偶数
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 打印1~10的奇数
even_numbers = list(range(1, 10, 2))
print(even_numbers)

# 下面的代码演示了如何将前10个整数的平方加入到一个列表中
squares = []
for number in range(1, 11):
    squares.append(number ** 2)
print(squares)

# 4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
