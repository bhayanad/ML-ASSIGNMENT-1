#!/usr/bin/env python
# coding: utf-8

# Q1.Create a program that asks the user to enter name and their age and then print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[1]:


name = input(" Please enter your name: ")
age = int( input("Please enter your age: ") )
fin =  2021 - age + 100
print(f"{name},you will turn 100 years old in the year {fin}.")


# Now do the following:
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# 2. Print out that many copies of the previous message on separate lines. (

# In[2]:


name = input("Enter your name: ")
age = int( input("Enter your age: ") )
i = int(input("How many times do you want the output to be displayed? "))
fin =  2021 - age + 100
for j in range(i):
    print(f" {name}, you will turn 100 years old in the year {fin}.",end='\t')


# In[4]:


name = input("Enter your name: ")
age = int( input("Enter your age: ") )
i = int(input("How many times do you want the output to be displayed? "))
fin =  2021 - age + 100

for j in range(i):
    print(f"{name}, you will turn 100 years old in the year {fin}.")


# 2. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# In[5]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)


# Also do the following:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# In[6]:


# 2.1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []
for i in a:
    if i < 5:
        new.append(i)
print(new)


# In[7]:


# 2.2
print( [x for x in a if x < 5] ) 


# In[8]:


# 2.3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input("Enter number: "))
new = []
for i in a:
    if i < n:
        new.append(i)
print(new)


# 3. Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)

# In[9]:


def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the number of term: "))

print("Sequence is:")
for i in range(n):
   print(fibonacci(i))


# 4. Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extra: Write two different functions to do this - one using a loop and constructing a list, and another using sets.

# In[10]:


def removingDuplicate(l):
    n = []
    
    for i in l:
        if i not in n:
            n.append(i)
    return n

fin = removingDuplicate( [1,1,2,3, 4, 4, 5, 5,5] )
print(fin)


# In[11]:


# 3.1
def removingDuplicates(l):
    return list(set(l))

print( removingDuplicates([1,1,2,3, 4, 4, 5, 5,5]) )


# 
# 5. Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors) Use functions.

# In[12]:


def primeOrNot(n):
    if n <= 1:
        return "Not prime"
    else:
        
        for i in range(2, n):
            if n % i == 0:
                return "Not prime"
        else: 
            return "Prime"
        
n = int( input("Enter a number: ") )
print( primeOrNot(n) )


# In[ ]:




