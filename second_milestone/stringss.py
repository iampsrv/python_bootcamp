# name = "Pranjal"

# print(name[5])


# str1 = "Hello"
# str2 = "World"
# result = str1 + " " + str2 # Concatenating two strings with a space in between
# print(result)

# name = "Pranjal"
# age = 26
# message = "My name is {} and I'm {} years old.".format(name, age)
# print(message)

# text = "Hello, World! World World World"
# new_text = text.replace("World", "Python",2)
# print(new_text)

# text = "Hello, World!"
# print(text.startswith("Hello")) # Checking if the string starts with "Hello" (True)
# print(text.endswith("!"))

# num = "123a"
# alphabets = "abc"
# print(num.isnumeric()) # Checking if the string contains only numeric characters (True)
# print(alphabets.isalpha())
# print(num.isalnum())

# name = "Alice"
# age = 25
# message = f"My name is {name} and I'm {age} years old."
# print(message)

# msg = "my name is pranjal. my age is 26"
# sentence = msg.split(". ")
# print(sentence)
# # capitalized_text = msg.capitalize()
# # print(capitalized_text)
# new_list=[]
# for i in sentence:
#     new_list.append(i.capitalize())
# print(new_list)
# text = ". ".join(new_list)
# print(text)

text = "P7y8t9h6o4n"
digits = ''.join(filter(str.isdigit, text))
letters = ''.join(filter(str.isalpha, text))
print(digits) # Output: "78964"
print(letters)