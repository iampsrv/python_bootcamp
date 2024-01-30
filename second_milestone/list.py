'''
# cart = ["bag", "vegetables", "smartphone", "football"]

# # for item in cart:
# #     print(item)
# cart.append("shoes")

# print(cart)

my_list = list(range(1, 10))
# for i in my_list:
#     print(i)
print(my_list)

print(my_list[0])
print(my_list[8])
my_list[8]="nine"

print(my_list)

my_list.append('mango') # Appending an element at the end
my_list.extend(['grapes', 'kiwi'])

print(my_list)

my_list.remove('mango') # Removing a specific element
del my_list[0] # Removing element at index 0
my_list.pop() # Removing the last element and returning it

print(my_list)
'''

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenated_list = list1 + list2

# print(concatenated_list)
# print(len(concatenated_list))

# my_list = ['apple', 'banana', 'cherry']
# if 'kiwi' in my_list:
#     print("Found!")
# else:
#     print("Not found")

# cart = ["bag", "vegetables", "smartphone", "football","bag"]
# count = cart.count("bag")
# print("No of bag",count)

# my_list = [4, 2, 1, 3, 5]
# # my_list.sort(reverse=True) # Sorting the list in ascending order
# # print(my_list)

# # my_list.reverse()
# print(my_list[::-1])

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[0][1])

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# equal = list1 == list2 # Checking if the two lists are equal
# print(equal)
# print(list1 is list2)

# my_list = [1, 2, 3]
# repeated_list = my_list * 3 # Repeating the list three times
# print(repeated_list)

# my_list = [1, 2, 3]
# a, b, c = my_list # Unpacking the list into separate variables
# print(a, b, c)

# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 10) # Inserting the value 10 at index 2
# print(my_list)

marks =[85,95,89,93,100]
total_marks = sum(marks)
total_subjects = len(marks)
average = total_marks/total_subjects
print("Average marks",average)

print("Minimum marks",min(marks))
print("Max marks",max(marks))

message = "Average marks is {}, Minimum marks is {} and Maximum marks is {}.".format(average, min(marks),max(marks))
print(message)