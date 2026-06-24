#Python functions assignment-2

#1. Rectangle Area Calculator Problem: Develop a function calculate_area(length,
#width) that computes the area of a rectangle. Ensure the function includes a descriptive docstring.

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


#2. Customizable Greetings Problem: Create a function greet(name, greeting="Hello")
#that outputs a personalized message. Demonstrate how the default argument behaves when omitted versus when provided.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Preeti")  # Uses default greeting
greet("Ash", "Heyo")  # Uses custom greeting

#3. Dynamic Summation Problem: Implement a function sum_all(*args) that accepts any
#number of numerical inputs and returns their cumulative sum.

def sum_all(*args):
    return sum(args)
    for num in args:
        total += num
        return total
    
    print (sum_all(1, 2, 3, 4, 5))

#4. User Profile Generator Problem: Design a function create_profile(name, age, **kwargs) 
# that takes mandatory identity details and optional attributes like city or profession,
# printing a formatted summary.

def create_profile(name, age, **kwargs):
    profile = f"Name: {name}\nAge: {age}\n"
    for key, value in kwargs.items():
        profile += f"{key.capitalize()}: {value}\n"
    print(profile)

print (create_profile("Alice", 30, city="New York", profession="Engineer"))

#5. Recursive Factorials Problem: Write a recursive implementation of a function
#factorial(n) to calculate the factorial of a given non-negative integer.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  

#6. Lambda-Based Sorting Problem: Given a list of dictionaries representing students with
# ‘name’ and ‘age’ keys, utilize a lambda function within the sort() method to organize the list by age.

students = [
    {"name": "Alice", "age": 25},   
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 30}
]
print("Before sorting:", students)
students.sort(key=lambda x: x["age"])
print("After sorting:", students)

#7. Functional Filtering Problem: Use the filter() function with a lambda expression to get
# all numbers greater than 5 from a list [1, 7, 3, 9, 2, 8]

numbers = [1, 7, 3, 9, 2, 8]
filtered_numbers = list(filter(lambda x: x > 5, numbers))
print("Numbers greater than 5:", filtered_numbers)

#8. Function Decorator with Arguments Problem: Create a decorator repeat(num_times)
# that makes a function run num_times times.

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hello():
    print("Hello!")

    say_hello()

#9. Generator for Even Numbers Problem: Write a generator function even_numbers(limit)
# that yields even numbers up to a specified limit.

def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

print(list(even_numbers(10)))

#10. Function to Validate Email Format Problem: Write a function is_valid_email(email)
# that checks if a string is a basic email format (contains ‘@’ and a ‘.’ after ‘@’).

def is_valid_email(email):
    if "@" in email:
        domain_part = email.split("@")[1]
        if "." in domain_part:
            return True
    return False

print(is_valid_email("usercorrect@example.com"))  # True
print(is_valid_email("userinvalid@example"))      # False

#11. List Initialization and Access Problem: Create a list fruits = ["apple", "banana",
# "cherry"] . Access and print the second element. Add “orange” to the end of the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1]) 

fruits.append("orange")
print(fruits)

#12. List Slicing Problem: Given numbers = [10, 20, 30, 40, 50, 60] , extract a sub-list
# containing [30, 40, 50] using slicing.

numbers = [10, 20, 30, 40, 50, 60]
sub_list = numbers[2:5]
print(sub_list)

#13. List Comprehension (Even Numbers) Problem: Use list comprehension to create a new
# list containing only the even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

#14. List Manipulation (Remove Duplicates) Problem: Write a function
# remove_duplicates(input_list) that takes a list with potential duplicates and returns a
# new list with only unique elements, preserving order.

def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 3, 2, 1, 4, 5, 3]))

#15. Nested Lists (Matrix Access) Problem: Create a nested list representing a 3x3 matrix.
# Access and print the element in the second row, third column.

matrix = [
    [19, 13, 3],
    [14, 53, 6],
    [74, 83, 43]
]
print(matrix[1][2]) 

#16. List Sorting (Multiple Criteria) Problem: Sort a list of strings words = ["banana",
# "apple", "cherry", "date"] alphabetically. Then, sort it by the length of the words.

words = ["banana", "apple", "cherry", "date","fig"]
words.sort()
words.sort(key=len)
print(words)

#17. List Concatenation and Repetition Problem: Concatenate two lists list1 = [1, 2]
# and list2 = [3, 4] . Then, create a new list by repeating list1 three times.

list1 = [1, 2]
list2 = [3, 4]
combined_list = list1 + list2
repeated_list = list1 * 3
print(combined_list)
print(repeated_list)

#18. Checking Element Existence Problem: Write a function check_item(item, my_list)
# that returns True if item is in my_list , otherwise False

def check_item(item, my_list):
    return item in my_list

print(check_item(5, [1, 2, 3, 4, 5]))  # True
print(check_item(6, [1, 2, 3, 4, 5]))  # False

#19. List Reversal Problem: Reverse a list data = [1, 2, 3, 4, 5] in-place and also
# create a new reversed list without modifying the original.

data = [1, 2, 3, 4, 5]
data.reverse()
print(f"In-place reversed list: {data}")

original_data = [1, 2, 3, 4, 5]
new_reversed_data = original_data[::-1]
print(f"New reversed list: {new_reversed_data}")
print(f"Original list remains unchanged: {original_data}")

#20.List as a Stack/Queue Problem: Demonstrate how a Python list can be used as a stack
# (LIFO) and a queue (FIFO) using append() , pop() , and insert() / pop(0)

stack = [] #LIFO
stack.append(1)
stack.append(2)
print(f"Stack after pushes: {stack}")
print(f"Popped from stack: {stack.pop()}")
print(f"Stack after pop: {stack}")

queue = [] #FIFO
queue.append(1)
queue.append(2)
print(f"Queue after enqueuing: {queue}")
print(f"Dequeued from queue: {queue.pop(0)}")
print(f"Queue after dequeue: {queue}")

#21. Set Creation and Basic Operations Problem: Create a set colors = {"red", "blue",
#"green"} . Add “yellow” to the set. Try adding “red” again and observe the result. Remove
#“blue” from the set.

colours = {"red", "blue", "green"}
print(f"Initial set: {colours}")
colours.add("yellow")
print(f"Set after adding 'yellow': {colours}")
colours.add("red") 
print(f"Set after trying to add 'red' again: {colours}")
colours.remove("blue")
print(f"Set after removing 'blue': {colours}")

#22. Set Union and Intersection Problem: Given two sets set_a = {1, 2, 3, 4} and
#set_b = {3, 4, 5, 6} , find their union and intersection.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)

print(f"Union of set_a and set_b: {union_set}")
print(f"Intersection of set_a and set_b: {intersection_set}")

# 23. Set Diffference and Symmetric Difference Problem: For the same sets set_a and set_b, find their difference (set_a - set_b) and symmetric difference.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

difference_set = set_a.difference(set_b)
symmetric_difference_set = set_a.symmetric_difference(set_b)

print(f"Difference of set_a and set_b (set_a - set_b): {difference_set}")
print(f"Symmetric difference of set_a and set_b: {symmetric_difference_set}")

#24. Checking Subsets and Supersets Problem: Determine if set_c = {1, 2} is a subset of
#set_a = {1, 2, 3, 4} . Determine if set_a is a superset of set_c .

set_a = {1, 2, 3, 4}
set_c = {1, 2}

is_subset = set_c.issubset(set_a)
is_superset = set_a.issuperset(set_c)

print(f"Is set_c a subset of set_a? {is_subset}")
print(f"Is set_a a superset of set_c? {is_superset}")

#25. Removing Duplicates from a List using Set Problem: Write a function
#unique_elements(input_list) that takes a list and returns a new list with all duplicate elements removed using a set.

def unique_elements(input_list):
    return list(set(input_list))

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(original_list)
print(f"Original list: {original_list}")
print(f"List with unique elements: {unique_list}")

#26. Frozen Sets Problem: Explain what a frozenset is and provide a simple example of
#when it might be useful. Solution:

my_frozenset = frozenset([1, 2, 3])
dictionary_with_frozenset_key = {my_frozenset: "This is a frozenset key"}
print(dictionary_with_frozenset_key)

try:
    my_frozenset.add(4)
except AttributeError as e:
    print(f"Error: {e}") # Output: Error: 'frozenset' object has no attribute 'add'

#27. Set Comprehension Problem: Use set comprehension to create a set of squares of odd numbers from 1 to 10. Solution:

odd_squares = {x**2 for x in range(1, 11) if x % 2 != 0}
print(odd_squares)

#28. Counting Unique Words Problem: Write a function count_unique_words(text) that 
# takes a string of text and returns the number of unique words in it (case-insensitive). Solution:

import re

def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower()) 
    return len(set(words))

text = "Hello world, hello Python, world is great!"
print(f"Unique words: {count_unique_words(text)}") 

#29. Membership Testing Efficiency Problem: Demonstrate the efficiency of the in operator
# for membership testing within a large set compared to a list. Solution:

import time
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))
# Check in list
start_time = time.time()
_ = 999_999 in large_list
end_time = time.time()
print(f"Time to check in list: {end_time - start_time:.6f} seconds")
# Check in set
start_time = time.time()
_ = 999_999 in large_set
end_time = time.time()
print(f"Time to check in set: {end_time - start_time:.6f} seconds")



#30. Multi-Set Intersection Problem: Given three separate sets, identify the specific elements
#that are present in every one of them. Solution:

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {4, 6, 7, 8}
common_elements = s1.intersection(s2, s3) # or s1 & s2 & s3
print(f"Common to all three: {common_elements}") # Output: {4}


#31. Tuple Creation and Access (Immutability) Problem: Create a tuple coordinates =
#(10, 20) . Access and print the first element. Try to modify an element and explain the outcome. 

coordinates = (10, 20)
print(f"Original coordinates: {coordinates}")
print(f"First element: {coordinates[0]}") # Output: 10
try:
    coordinates[0] = 15
except TypeError as e:
    print(f"Error: {e}") # Output: Error: 'tuple' object does not support

#32. Tuple Unpacking Problem: Given a tuple person = ("Alice", 30, "New York") ,
#unpack its elements into three separate variables name , age , and city . Solution:

person_info = ("Alice", 30, "New York")
name, age, city = person_info
print(f"Name: {name}, Age: {age}, City: {city}")

#33. Tuples as Dictionary Keys Problem: Create a dictionary where keys are tuples
#representing coordinates (e.g., (x, y) ) and values are names of locations. Solution:

location_map = {
(0, 0): "Origin",
(10, 20): "Park Entrance",
(5, -5): "Fountain"
}
print(location_map[(10, 20)]) # Output: Park Entrance

#34. Returning Multiple Values from a Function Problem: Write a function that returns a tuple
#of two values, and demonstrate how to unpack them. Solution:

def get_dimensions():
    return 100, 200 # Python automatically packs this into a tuple
width, height = get_dimensions()
print(f"Width: {width}, Height: {height}") # Output: Width: 100, Height: 2

#35. Tuple Concatenation and Repetition Problem: Concatenate two tuples tup1 = (1, 2)
#and tup2 = (3, 4) . Repeat tup1 twice. Solution:

tup1 = (1, 2)
tup2 = (3, 4)
combined_tuple = tup1 + tup2
repeated_tuple = tup1 * 2
print(f"Combined: {combined_tuple}") # Output: (1, 2, 3, 4)
print(f"Repeated: {repeated_tuple}") # Output: (1, 2, 1, 2)

#36. Checking Element Existence in Tuple Problem: Check if "apple" is in ("apple",
#"banana", "cherry") . Solution:

fruits_tuple = ("apple", "banana", "cherry")
print("apple" in fruits_tuple) #true
print("grape" in fruits_tuple) #false

#37. Counting Elements in Tuple Problem: Count the occurrences of 5 in (1, 5, 2, 5, 3,5)

my_tuple = (1, 5, 2, 5, 3, 5, 1)
count_of_5 = my_tuple.count(5)
print(f"Count of 5: {count_of_5}") # Output: 3

#38. Nested Tuples Problem: Create a nested tuple matrix = ((1, 2), (3, 4)) . Access
#the element 4 . 

matrix_tuple = ((1, 2), (3, 4), (5, 6))
element = matrix_tuple[1][1] # Access second tuple, then its second elemen
print(element) # Output: 4

#39. Single Element Tuple Syntax Problem: How do you create a tuple with a single element,
#e.g., (5,) ? Explain why (5) is not a tuple. 

single_element_tuple = (5,)
print(f"Type of (5,): {type(single_element_tuple)}") # Output: <class 'tup
not_a_tuple = (5)
print(f"Type of (5): {type(not_a_tuple)}") # Output: <class 'int'>

#40. Sorting a List of Tuples Problem: Given a list of tuples grades = [('Alice', 90),
#('Bob', 75), ('Charlie', 95)] , sort it by the second element (grade) in descending order.

grades = [('Alice', 90), ('Bob', 75), ('Charlie', 95)]
grades.sort(key=lambda item: item[1], reverse=True)
print(grades) # Output: [('Charlie', 95), ('Alice', 90), ('Bob', 75)]

#41. Dictionary Creation and Access Problem: Create a dictionary person = {"name":
#"John", "age": 30, "city": "New York"} . Access and print the person’s age. Add a
#new key-value pair for “occupation”: “Engineer”. 

person = {"name": "John", "age": 30, "city": "New York"}
print(f"Age: {person['age']}") # Output: Age: 30
person["occupation"] = "Engineer"
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'o

#42. Iterating Through Dictionary Items Problem: Iterate through the person dictionary and
#print each key-value pair.

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

#43. Using get() with a Default Value Problem: Try to access a non-existent key “salary” from
#the person dictionary using person['salary'] and then using person.get('salary',
#'N/A') . Explain the difference.

person = {"name": "John", "age": 30, "city": "New York"}

try:
    print(person['salary'])
except KeyError as e:
    print(f"Error with direct access: {e}") 
salary = person.get('salary', 'N/A')
print(f"Salary using .get(): {salary}")

#44. Dictionary Comprehension Problem: Use dictionary comprehension to create a dictionary
#where keys are numbers from 1 to 5 and values are their squares.

squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#45. Merging Dictionaries Problem: Merge two dictionaries dict1 = {"a": 1, "b": 2} and
#dict2 = {"b": 3, "c": 4} . If there are common keys, dict2 ’s values should override dict1 ’s.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

#method 1:
merged_dict_update = dict1.copy() # Create a copy to avoid modifying dict1
merged_dict_update.update(dict2)
print(f"Merged with update(): {merged_dict_update}") # Output: {'a': 1, 'b

#method 2:
merged_dict_unpack = {**dict1, **dict2}
print(f"Merged with **: {merged_dict_unpack}") # Output: {'a': 1, 'b': 3,

#46. Counting Word Frequencies Problem: Write a function word_frequency(sentence)
#that takes a sentence and returns a dictionary where keys are words and values are their
#frequencies (case-insensitive). Solution:

import re
def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower()) # Extract words and convert to lowercase   
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict
sentence = "This is a test sentence. This sentence is a test."
print(word_frequency(sentence)) 

#47. Nested Dictionaries Problem: Create a nested dictionary representing a student’s grades in
#different subjects. Access and print the student’s grade in ‘Math’. Solution:

student_grades = {
"name": "Emily",
"grades": {
"Math": 95,
"Science": 88,
"History": 92
}
}
math_grade = student_grades["grades"]["Math"]
print(f"Emily's Math grade: {math_grade}") 


#48. Deleting a Key-Value Pair Problem: From the person dictionary, remove the “city” key-
#value pair.

person = {"name": "John", "age": 30, "city": "New York", "occupation": "Engineer"}
del person["city"]
print(person)  

#49. Dictionary keys() , values() , items() Views Problem: Given a dictionary data =
#{"a": 1, "b": 2, "c": 3} , print its keys, values, and items as lists. Solution:

data = {"a": 1, "b": 2, "c": 3}
print(f"Keys: {list(data.keys())}")  
print(f"Values: {list(data.values())}")  
print(f"Items: {list(data.items())}") 

#50. Inverting a Dictionary Problem: Write a function invert_dict(d) that takes a dictionary
#and returns a new dictionary where keys become values and values become keys. Assume all
#values are unique and hashable. Solution:

def invert_dict(d):
    return {value: key for key, value in d.items()}
my_dict = {"a": 1, "b": 2, "c": 3}
inverted = invert_dict(my_dict)
print(inverted) 