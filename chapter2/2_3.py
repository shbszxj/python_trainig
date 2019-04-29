"This is a string."
'This is also a string.'

name = "ada lovelace"
# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
print(name.title())

print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

# 要在字符串中添加制表符，可使用字符组合\t
print("\tPython")

# 要在字符串中添加换行符，可使用字符组合\n
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 要确保字符串末尾没有空白，可使用方法 rstrip()
favorite_language = "python          "
print(favorite_language.rstrip())
print(favorite_language)

# 要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = "       python          "
print(favorite_language.strip())
print(favorite_language.lstrip())
