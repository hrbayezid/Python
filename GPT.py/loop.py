# Q1: Write a loop that prints all even numbers between 1 and 20.
#     Loop Type: for loop (for a straightforward range-based count).


# for i in range (1,21):
#     if (i%2==0):
#         print("even number",i)



# Q2: Create a loop that counts down from 10 to 1, and when it hits zero, it prints "Blast Off!"
#     Loop Type: while loop (while loops are great for countdowns or conditions that end on a specific trigger).


# count = 10

# while count > 0:
#     print("count no: ",count)
#     count -=1
#     if(count == 0): print("blast off")



# Q3: Given a list of numbers, write a loop that calculates the sum of all the numbers in the list.
# Loop Type: for loop (iterate through the list to add each item).


# lst = [1,2,3,4,5,6,7,8,9,10]

# sum = 0
# for total in lst:
#     sum +=total
# print(sum)



# Q4: Write a loop that prints out each character in a string (e.g., "Bayezid"), but makes each vowel uppercase and the consonants lowercase. Loop Type: for loop (to easily access each character by iterating over the string).


# str = "bayezid "

# for i in str:
#     if (i == "a" or i=="e"):
#         print(i.upper(), end="")
#     else:
#         print(i.lower(), end="")



# Q5: Using a loop, write a program that finds the smallest and largest numbers in a given list, without using the built-in min() or max() functions.
# Loop Type: for loop (loop through the list while checking each number against the current smallest/largest).



# numbers = [45, 23, 67, 89, 12, 38, 92, 6, 34]

# smallest = numbers[0]
# largest = numbers[0]

# for num in numbers:
    
#     if num < smallest:
#         smallest = num
    
#     if num > largest:
#         largest = num

# print("Smallest number is:", smallest)
# print("Largest number is:", largest)



# Q6: Given a number n, use a loop to print the multiplication table of n up to 10.
# Loop Type: for loop (simple range-based loop for the times table).


# n = int (input("enter number : "))

# for i in range(11):
    
#     print(n*i)



# Q7: Create a program that prints the first n Fibonacci numbers using a loop.
# Loop Type: while loop (use while here to keep going until n is reached, since the exact number of operations isn’t known beforehand).



# n = int(input("enter the number"))

# a = 0
# b = 1

# count = 0

# while count<n:
#     print (a)
#     c= a+b
#     a=b
#     b=c
#     count+=1



# Q8: Write a nested loop that prints a half pyramid of * symbols with a given height.
# Loop Type: Nested for loops (one for each row, another for each space or * symbol in the row).

# n = int(input("enter the number :  "))

# for i in range (1,n+1):
#     for j in range (i):
#         print ("*" , end = "")
#     print()






# Q9: Write a program using a loop that identifies all prime numbers between 1 and 50.
# Loop Type: Nested for loops (one to check each number in range 1-50, another to check its divisibility).


# for num in range(2,51):
#     for i in range (2,num):
#         if num%i == 0:
#             break
#     else:
#         print(num)



# Sum of the first n natural numbers: 


# n = int(input("enter number : "))

# sum = 0

# for i in range (1, n+1):
#     sum+=i
# print (sum)

# i = 0
# while i <= n:
#     sum+=i
#     i+=1
# print (sum)



# Factorial of a number using a for loop: def factorial(n): 


# n = int(input("enter number : "))

# fact = 1

# for i in range(1, n+1):
#     fact*=i
# print(fact)



# Factorial using a while loop: def factorial(n)

# n = int(input("enter number : "))
# fact = 1
# i=1

# while i<=n:
#     fact*=i
#     i+=1
# print(fact)



# Factors of a given number:

# n = int(input("enter number : "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print (i) 

# i =1 
# while i<=n:
#     if n%i == 0:
#         print(i)
#     i+=1



# Count the number of factors of a given number: 

# n = int(input("enter number : "))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count+=1

# print(count)       

# i=1
# while i<=n :
#     if n%i == 0:
#         count+=1
#     i+=1
# print (count)


# Check whether a given number is prime: def is_prime(n):

# n = int(input("enter number : "))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")


# Check if a number is perfect: 

# n = int(input("enter number : "))

# sum = 0

# for i in range (1,n):
#     if n%i == 0:
#         sum+=i

# perfect = ("perfect" if n == sum else "not perfect")

# print(perfect)
