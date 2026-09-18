def add_item(items):
    items.appemd(10)

    data = [1,2,3]
    add_item(data.copy())
    print(data)

#one more example....
numbers = [1, 2, 3]

numbers2 = numbers

numbers2.append(4)

print(numbers)
print(numbers2)