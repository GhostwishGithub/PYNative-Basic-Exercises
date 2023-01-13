#A simple series of exercises to stay in practice.
#https://pynative.com/python-basic-exercise-for-beginners/

#Exercise 1
#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
def math(num1, num2):
    #multiply the two numbers
    sum = num1 * num2
    #now check to see if it's less than 1000
    if sum <= 1000:
        return sum
    else:
        # if it's over, then add them
        return num1 + num2
#Given 1
number1 = 20
number2 = 30
print("The result of given 1 is:", math(number1, number2))
#Given 2
number3 = 40
number4 = 30
print("The result of given 2 is:", math(number3, number4))

#Exercise 2
#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
#A simple use of the range() function and for loops.
#start with the base value
previous_num = 0
#then the for loop
for i in range(1, 11):
    #a simple incrementor
    next_num = previous_num + i
    #print the results, pretty like
    print("The current number is:", i,"\nThe previous number was:", previous_num, "\nThe sum of the two is:", next_num)
    #now reset the previous number to the current number
    previous_num = i

# #Exercise 3 - commented out for expediency
# #Print out every even index number from an input stream
# #first, get the input
# word = input("Enter the word you want counted:")
# print("Original word:", word)
# #now, get the length of the string
# size = len(word)
# #Now, count through the word. Remember: Computers start at 0.
# for i in range(0, size -1, 2):
#     print("index[", i, "]", word[i])

#Exercise 4
#Write a program to remove characters from a string starting from zero up to 'n' and return a new string
#We'll set up a function to use string slicing
def remove_chars(word, n):
    print("The original word was:", word)
    x = word[n:]
    return x
print(remove_chars("Pynative", 4))
print(remove_chars("Synthwave", 2))

#Exercise 5
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
#Very easy, especially given the fact that python all but manages the list for you
#First, the exercise provides two lists for us
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
#Remember, anything inside square brackets is a list in python
#now, let's get a function going to do the work, yes?
def first_and_last(list):
    print("Using this list:", list)
    #now here's the fun bit. python counts the list items for you, so all you have to do is get the first and last values.
    #Now, how would you know how long the list is without cheating?
    #Easy!
    #you don't. You just throw in -1 to make it loop back to the LAST value. 
    #Clever, huh?
    first_num = list[0]
    last_num = list[-1]
    #boom, magic. Now it's just an if statement to get those true/false values out there
    if first_num == last_num:
        return True
    else:
        return False
    #It's basically done. Just gotta use it.
print("The result is:", first_and_last(numbers_x))
print("The result is:", first_and_last(numbers_y))

#Exercise 6
#Iterate the given list of numbers and print only those numbers which are divisible by 5
#Oh dear. A math problem.
#Well, a little bit of research showed all I need is the % operator. Easy peesy. I love python.
#Given list:
num_list = [10, 20, 33, 46, 55]
#Just to be neat and orderly, we'll print it out
print('Our list of numbers is:', num_list)
#Now a preamble to the for loop we'll use
print("And here's the ones divisible by 5:")
for x in num_list:
    if x % 5 == 0:
        print(x)

#Exercise 7
#Write a program to find how many times substring “Emma” appears in the given string.
#Ah, I already know the answer: it's the count() method!
#Simple. First? A string!
a_string = "Emma likes to play tabletop games. Emma is a nerd. Emma is SUCH a nerd. Nerdy nerd nerd Emma!"
count = a_string.count("Emma")
print("Emma appeared", count, "times!")

#Exercise 8
#Print the following pattern
#So, this just wants us to print a pattern. I actually feel like the actual description is.. missing. I could approach this a hundred different ways, but, I opened the solution and saw what they meant.
#I'll replicate it here.
for x in range(10):
    for y in range(x):
        #I'm interested in this end feature. Hadn't seen it before.
        #Oh neat. It stops the auto newline of print functions!
        print (x, end=" ")
    print("\n")
    #and then we manually put the newline back in

#Exercise 9
#Write a program to check if the given number is a palindrome number. A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
#I appreciate the definition because I had no idea.
#I was a little stumped and had to do some research. Found it after a few googles.
#We'll make a function to swap the number around
def palindrome(number):
    print("The number is:", number)
    original_number = number
#Then we just use a while loop to switch it
    reversed_number = 0
    while number > 0:
        reminder = number % 10
        reversed_number = (reversed_number * 10) + reminder
        number = number // 10
    #Then a simple if statement to check it.
    if original_number == reversed_number:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")
palindrome(121)
palindrome(125)

#Exercise 10
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def merge_list(list1, list2):
    result_list = []

    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))

#Exercise 11
#Write a program to extract each digit from an integer in the reverse order
number = 7536
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")

#exercise 12
#calculate incoming tax for the given income by adhering to the below rules~
#(a table is displayed)
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)