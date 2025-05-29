# # List of essentials for a Python marathon
# essentials = ["coffee", "snacks", "more coffee", "energy drinks","coffee"]
# coder = ["bayezid"]
# item = essentials[1:]

# appending = essentials.append("snacks")

# removing = essentials.remove("more coffee")

# popping = essentials.pop()

# inserting = essentials.insert(1,"sleep")

# position = essentials.index("coffee")

# counting = essentials.count("coffee")

# sorting = essentials.sort(reverse=  True)

# reversing = essentials.reverse()

# extending = essentials.extend(coder)

# # cleaning = essentials.clear()
# #
# print (essentials)




# Q.1

# Create a list called movies with three of your favorite movie titles.
# Add two more movies at the end using append().
# Insert a new movie at the second position using insert().
# Remove one movie by name with remove().
# Print the final list.


# fav_movies = ["forest gump", "terminal", "three idiots"]

# for _ in range (2):
#     add_name = input("enter movie names : ")
#     fav_movies.append(add_name)

# fav_movies.insert(1,"hera pheri")
# fav_movies.remove("terminal")

# print(fav_movies)


# Q.2

# Make a list called grocery_list with items like "apples," "bananas," and "carrots."
# Use pop() to remove and print the last item.
# Print the index position of "bananas" using index().
# Add "bananas" again and count how many times it appears with count().


# grocery_list = ["apples","bananas","carrots"]

# last_item = grocery_list.pop()
# print("last item is : ", last_item)

# banana = grocery_list.index("bananas")
# print("bananas index is :",banana)

# grocery_list.append("bananas")

# counting = grocery_list.count("bananas")
# print ("counting bananas",counting,"times")



# Q.3

# Create a list called to_do_list with at least five tasks.
# Sort this list in alphabetical order using sort().
# Reverse it back using reverse().
# Clear the entire list with clear() and print the final result.


# to_do_lis = ["python", "salat","study with chatgpt (bff)","SQL","list"]

# to_do_lis.sort()
# print(to_do_lis)

# to_do_lis.sort(reverse=True)
# print(to_do_lis)

# to_do_lis.clear()
# print(to_do_lis)


# Q.4 

# Make two lists: programming_languages = ["Python", "Java"] and new_languages = ["Rust", "Go"].
# Use extend() to combine both lists into programming_languages.
# Print the combined list.


# programming_languages = ["Python", "Java"]
# new_languages = ["Rust", "Go"]

# programming_languages.extend(new_languages)
# print(programming_languages)



# Q.5

# Create a list of numbers from 1 to 10 called nums.
# Remove the number 5 and add 20 at the end.
# Use pop() to remove the last number, and then use count() to see how many times the number 2 appears.
# Print the final list.

# nums = []
# for i in range (1,11):
#     nums.append(i)

# nums.remove(5)
# nums.append(20)
# nums.pop()
# counting = nums.count(2)
# print ("counting",counting,"times")
# print(nums)



# Index Tracker: Create a list of five movie titles and print each title with its index in the format: Index 0: Movie_Name.

# movies = ["hulk", "deadpool", "logan","x-man","dr. stranger"]

# for index,movie in enumerate(movies):
#     print(f"my fav movie is {index} : {movie}")



# Conditional Loop: Given a list of numbers, print only those that are divisible by 3. If a number is greater than 20, stop the loop.

# num =[]

# for i in range (1,21):
#     if i % 3 == 0:
#         num.append(i)

# print (num)



# Nested Loop with Two Lists: Write a nested loop to print each possible pair of names from two separate lists, e.g., ["Alice", "Bob"] and ["Charlie", "Dana"].


# names1 = ["Alice", "Bob"]
# names2 = ["Charlie", "Dana"]

# for name1 in names1:
#     for name2 in names2:
#         print(name1,name2, end = ", ")
# print()


# # zip
# # print("testing zip method")
# # for name1,name2 in zip(names1,names2):
# #     print(name1,name2)



# Find Common Elements: Write code that finds common elements in two lists of numbers. The lists may contain duplicates, but the output list should show only unique common elements.


# list1 = [1,2,3,4,5]
# list2 = [3,4,5]

# uniqe = []
# for item1 in list1:
#     for item2 in list2:
#         if item1 == item2:
#             uniqe.append(item1)
# print(uniqe)



# List Comprehension Practice: Use list comprehension to create a list of squares of all numbers from 1 to 10, but include only squares of even numbers.

# numbers = [1,2,3,4,5]
# square = [num**2 for num in numbers if num%2==0]
# print (square)
    
    
# Write a program to find the sum of all the numbers in the nested list.

# numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
# total = 0

# for row in numbers:
#     for num in row:
#         total += num
# print (total)


# Write a program to replace the grade of Bob with 90.


# grades = [
#     ["Alice", 85],
#     ["Bob", 78],
#     ["Charlie", 92]
# ]

# grades [1][1] = 90
# print(grades)


# Write a program to flatten the list (i.e., convert it into a single list).

# nested_list = [[5, 6], [7, 8], [9, 10]]

# flatten_list =[]

# for sublist in nested_list:
#     for num in sublist:
#         flatten_list.append(num)
# print(flatten_list)        



# Write a program that prints the largest number in each sublist

# numbers = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]

# for num in numbers:
#     print(max(num))


# Write a program to remove the number 5 from the nested list.


# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for num in numbers:
#     if num [1] == 5:
#         num.remove(5)
# print(numbers)


# Create a nested list (matrix) from these two lists. The result should look like this: [[1, 4], [2, 5], [3, 6]]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# matrix = []
# for item1,item2 in zip(list1,list2):
#     matrix.append([item1,item2])
# print(matrix)


#  Create a nested list (matrix) from these two lists. The result should look like this: [1, 2, 3] [4, 5, 6]

# matrix = [[1, 4], [2, 5], [3, 6]]
# output = [[],[]]
# for num in matrix:
#     output[0].append(num[0])
#     output[1].append((num[1]))
# print(output)


# Write a program to add a new column [7, 8, 9] to this matrix, making the result: [[1, 2, 7], [3, 4, 8], [5, 6, 9]]

# matrice = [[1, 2], [3, 4], [5, 6]]
# newdata = [7, 8, 9]

# for i in range(len(matrice)):
#     matrice[i].append(newdata[i])

# print(matrice)
   

# Write a program to count how many times the number 2 appears in the list.

# nested_list = [[2, 3], [5, 2], [4, 2]]
# counting = []

# for row in nested_list:
#     for num in row:
#         counting.append(num)

# print(counting.count(2))