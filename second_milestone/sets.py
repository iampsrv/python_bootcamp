# data_sci={"R","Tableau","SAS","Python","SQL","Git"}
# data_analysis= {"Python","SQL","Git","Java","Scala","Hadoop"}

# print("Skills required for data science and data analysis", data_sci.union(data_analysis))
# print("Skills only required for data science", data_sci.difference(data_analysis))
# print("Skills only required for data analysis", data_analysis.difference(data_sci))
# print("Common Skills required for both data science and data analysis", data_sci.intersection(data_analysis))



#remove duplicate numbers

# my_list = [1,2,3,4,5,6,7,1,2,6,5,4,3,2]
# print(my_list)

# my_list=list(set(my_list)) # Data type conversion
# my_list.sort()
# print(my_list)

# my_set = {1, 2, 3}
# frozen_set = frozenset(my_set) # Creating an immutable version of the set using
# print(frozenset)
# frozenset.add(4)
# print(frozenset)


my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
