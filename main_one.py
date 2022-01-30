# Activities & Practices

# 01 "Tenth Power"
# Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

# 1. Define the function header to accept one input parameter called num
# 2. Print out 1 times [num]
# 3. Print out 2 times [num]
# 4. Print out 3 times [num]
# 5. Return the value of 3 times [num]

# Write a function named [first_three_multiples()] that has one parameter named [num].
# This function should print the first three multiples of [num]. Then, it should return the third multiple.
# For example, [first_three_multiples(7)] should print [7], [14], and [21] on three different lines, and return [21].

print("'First Three Multiples' challenge")
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 02 "Tip"
# Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. In order to do this, we will need a few steps:

# 1. Define the function to accept the total cost of the food called [total] and the percentage to tip as [percentage]
# 2. Calculate the tip amount by multiplying the total and percentage and dividing by 100
# 3. Return the tip amount

# Create a function called [tip()] that has two parameters named [total] and [percentage].
# This function should return the amount you should tip given a total and the percentage you want to tip.

print("'Tip' challenge")
def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount

# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 03 "Bond, James Bond"
# It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. To accomplish this, we need to:

# 1. Define the function to accept two parameters, [first_name] and [last_name]
# 2. Concatenate the string [', '] on to the [last_name]
# 3. Concatenate the [first_name] on to the result of the previous step
# 4. Concatenate a space on to the result
# 5. Concatenate the [last_name] again to the result
# 6. Return the final string

# Write a function named [introduction()] that has two parameters named [first_name] and [last_name].
# The function should return the [last_name], followed by a comma, a space, [first_name] another space, and finally [last_name].

print("'Bond, James Bond' challenge")
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 04 "Dog Years"
# Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

# 1. Define the function called [dog_years] to accept two parameters: [name] and [age]
# 2. Calculate the age of the dog in dog years
# 3. Concatenate the string with the dog’s name and age in dog years
# 4. Return the resulting string

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named [dog_years()] that has two parameters named [name] and [age].
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!

print("'Dog Years' challenge")
def dog_years(name, age):
  return (name+", you are "+str(age*7)+" years old in dog years")
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 05 "All Operations"
# For the final code challenge, we are going to perform multiple mathematical operations on multiple inputs to the function. We will begin with adding the first two inputs, then we will subtract the third and fourth inputs. After that, we will multiply the first result and the second result. In the end, we will return the remainder of the previous result divided by the first input. We will also print each of the steps. The steps needed to complete this are:

# 1. Define the function to accept four inputs: [a], [b], [c], and [d]
# 2. Print and store the result of [a] + [b]
# 3. Print and store the result of [c] - [d]
# 4. Print and store the first result times the second result
# 5. Return the previous result modulo [a]

# Create a function named [lots_of_math()]. This function should have four parameters named [a], [b], [c], and [d]. The function should print 3 lines and return 1 value.
# First, print the sum of [a] and [b].
# Second, print [c] minus [d].
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo [a].

print("'All Operations' challenge")
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah




