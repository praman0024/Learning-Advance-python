#basic list comprenhension..

numbers = [1,2,3,4,5]

squared = []
for i in numbers :
    squared.append(i * i)
    print(squared)

#filtring data..
#you can add conditions inside a comprehension

numbers = [1,2,3,4,5,6]

even = [i for i in numbers if i%2==0]
print(even)

#transforming text data..
names = [" Ali "," Sara "," John "]

cleaned_data = [new_name.strip().lower()for new_name in names if new_name]

print(cleaned_data)  #this is how raw data is cleaned befor analysis..

#dictionary comprehensions..
items = ["apple","banana","cherry"]
prices = [0.5, 0.3, 0.2]
price_dict = {items[i]: prices[i] for i in range(len(items))}
print(price_dict)

#set comprehensions..
#set comprehension remove duplicates automatically...

values = [1,2,2,3,3,4]

unique_squares = {i *i for i in values}
print(unique_squares)  #this is helpful when you only care about unique results..