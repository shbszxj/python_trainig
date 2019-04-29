user_name = 'Eric'
print("Hello " + user_name + ", would you like to learn some Python today?")

print("Hello " + user_name.title() +
      ", would you like to learn some Python today?")

print("Hello " + user_name.upper() +
      ", would you like to learn some Python today?")

print("Hello " + user_name.lower() +
      ", would you like to learn some Python today?")

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_person = 'Albert Einstein'
message = famous_person + \
    ' once said, "A person who never made a mistake never tried anything new."'
print(message)

famous_person = '        Albert Einstein        '
print("\t\n" + famous_person)
print(famous_person.lstrip() + "12312312")
print(famous_person.rstrip() + "12312312")
print(famous_person.strip() + "12312312")
