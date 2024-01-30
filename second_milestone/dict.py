# my_dict = {"name": "Pranjal", "age": 26, "city": "Pune", 2:9}
# print(my_dict["name"])
# print(my_dict)


# book1= {"name":"Start with Why", "author_name":"Simon Simek"}
# book2= {"name":"Wings of fire", "author_name":"APJ Abdul Kalam"}
# book3= {"name":"Ikigai", "author_name":"Hector Garcia"}

# books = [book1,book2,book3]


# for i in books:
#     print(i["author_name"])

# my_dict = {"name": "Alice", "age": 25}
# my_dict["city"] = "New York" # Adding a new key-value pair
# my_dict["age"] = 26
# print(my_dict)

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# keys = my_dict.keys()
# print(keys)

# values = my_dict.values()
# print(values)


# items = my_dict.items()
# print(items)

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}

print(merged_dict)