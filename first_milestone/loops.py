# for i in range(5):
#     print("Python")

# count=5
# while count > 0:
#     print("Python")
#     count-=1

# number_of_lives=3
# while number_of_lives > 0:
#     print("Mario is alive")
    
#     number_of_lives-=1
# print("Mario is dead")

# for i in range(5):
#     print(i)

# for i in range(0,20,2):
#     print(i)

# num_list = [1,2,3,4,5,6,7,8,9,10]

# for num in num_list:
#     print(num**2)
#     print("#")

# skills = ["python", "java", "c", "chatgpt", "html", 1,2,3,4,5]

# for s in skills:
#     print(s)


#############################################################
# Break
# num_list = [1,2,3,4,5,6,7,8,9,10]

# for i in num_list:
#     if i == 7:
#         break
#     print(i)
#############################################################
# Continue (bypass)
    
# num_list = [1,2,3,4,5,6,7,8,9,10]

# for i in num_list:
#     if i == 7:
#         continue
#     print(i)

# Pass (placeholder)
# num_list = [1,2,3,4,5,6,7,8,9,10]

# for i in num_list:
#     if i == 7:
#         pass
#     print(i)


# for i in range (5):
#     for j in range(i,5):
#         print("P",end=" ")
#     print()
n=5
for i in range(n):
    for j in range (i+1):
        print(" ", end ="")
    for j in range (i,n):
        print("P", end ="")
    print()