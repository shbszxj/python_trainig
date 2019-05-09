# 4.4 使用列表的一部分
# 4.4.1 切片
players = [0, 1, 2, 3, 4]
# 例如，如果你要提取列表的第 2~4 个元素，可将起始索引指定为 1 ，并将终止索引指定为4
print(players[1:4])
# 如果你没有指定第一个索引， Python 将自动从列表开头开始：
print(players[:4])
# 例如，如果要提取从第 3 个元素到列表末尾的所有元素，可将起始索引指定为 2 ，并省略终止索引
print(players[2:])
# 例如，如果你要输出名单上的最后三名队员，可使用切片 players[-3:]
print(players[-3:])

# 4.4.2 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
