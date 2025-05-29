# Find the Most Frequent Word: Write a program that takes a list of words and uses a dictionary to find the most frequent word in the list.

names = {"names":["bayezid" , "saju", "jouynyl","bayezid"]}

count_name = {}

for name in names["names"] :
        count_name[name] = count_name.get(name , 0)+1
print(count_name)



# Reverse a Dictionary: Given a dictionary where the keys are numbers and the values are words, create a new dictionary where the keys are words and the values are numbers.

# python
# Copy code
# # Example input:
# numbers = {1: 'one', 2: 'two', 3: 'three'}
# # Example output:
# # {'one': 1, 'two': 2, 'three': 3}
# Count Vowels in a Sentence: Write a program that counts how many times each vowel appears in a given sentence using a dictionary.

# Merge Dictionaries and Sum Values: Suppose you have two dictionaries, both with integer values, where some keys overlap. Write a program that merges them into one dictionary, summing the values for overlapping keys.

# python
# Copy code
# # Example input:
# dict1 = {'a': 2, 'b': 3, 'c': 5}
# dict2 = {'b': 4, 'c': 2, 'd': 8}
# # Example output:
# # {'a': 2, 'b': 7, 'c': 7, 'd': 8}
# Find the Oldest Person: Create a dictionary of people with their ages and write a program to find the oldest person in the dictionary.

# Create a Dictionary from Two Lists: You have two lists, one of names and one of ages. Write a program to create a dictionary where each name is paired with its corresponding age.

# python
# Copy code
# # Example input:
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 22]
# # Example output:
# # {'Alice': 25, 'Bob': 30, 'Charlie': 22}
# Filter Dictionary by Value: Given a dictionary of students and their grades, write a program that creates a new dictionary containing only students who scored above a certain grade threshold