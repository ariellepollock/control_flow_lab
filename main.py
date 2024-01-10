# control flow in python

######################################
# exercise-01 Vowel or Consonant
######################################
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
letter = input('Please enter aletter from the alphabet (a-z or A-Z): ').lower()
# 2. Write the code that determines whether the letter entered is a vowel
if letter in 'a e i o u':
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
    print(f'The letter {letter} is a vowel')
#      - The letter x is a consonant
else:
    print(f'The letter {letter} is a consonant')
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

######################################
# exercise-02 Length of Phrase
######################################
# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
phrase = ''
while phrase != 'quit':
    phrase = input('Please enter a word or phrase: ')
# 2. Print the following message:
    print(f'What you entered is {len(phrase)} characters long')
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

######################################
# exercise-03 Calculate Dog Years
######################################
# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
years = int(input("Input a dog's age: "))
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
if years < 3:
    dog_years = years * 10
#      - Any remaining years count as 7 years each
else:
    dog_years = ((years - 2) * 7) + 20
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
print(f"The dog's age in dog years is {dog_years}")

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

######################################
# exercise-04 What kind of Triangle?
######################################
# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
print('Enter the lengths of three sides of a triangle:')
a = input('a: ')
b = input('b: ')
c = input('c: ')
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
if a == b and b == c:
    print('A triangle with sides of {a}, {b}, & {c} is an equilateral triangle')
#      scalene - all three sides are unequal in length
elif a != b and b != c:
    print('A triangle with sides of {a}, {b}, & {c} is a scalene triangle')
#      isosceles - exactly two sides are the same length
else:
    print('A triangle with sides of {a}, {b}, & {c} is an isosceles triangle')
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

######################################
# exercise-05 Fibonacci sequence for first 50 terms
######################################
# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
term = 0
a = 0
b = 1
while term <= 50:
    if term < 2:
        print(f'term: {term} / number: {term}')
    else:
        num = a + b
        print(f'term: {term} / number: {num}')
        a = b
        b = num
    term += 1

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

######################################
# exercise-06 What's the Season?
######################################
# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
month = input('Enter the month of the season (Jan - Dec): ')
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
day = int(input('Enter the day of the month: '))
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
if month in ('Dec', 'Jan', 'Feb', 'Mar'):
    season = 'Winter'
#      Mar 20 - Jun 20: Spring
elif month in ('Mar', 'Apr', 'May', 'Jun'):
    season = 'Spring'
#      Jun 21 - Sep 21: Summer
elif month in ('Jun', 'Jul', 'Aug', 'Sep'):
    season = 'Summer'
#      Sep 22 - Dec 20: Fall
else:
    season = 'Fall'
if month == 'Mar' and day > 19:
    season = 'Spring'
elif month == 'Jun' and day > 20:
    season = 'Summer'
elif month == 'Sep' and day > 21:
    season = 'Fall'
elif month == 'Dec' and day > 20:
    season = 'Winter'
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
print(f'{month} {day} is in {season}')

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.