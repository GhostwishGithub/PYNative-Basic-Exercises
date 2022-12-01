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
#Exercise 3
#Print out every even index number from an input stream
#first, get the input
word = input("Enter the word you want counted:")
print("Original word:", word)
#now, get the length of the string
size = len(word)
#Now, count through the word. Remember: Computers start at 0.
for i in range(0, size -1, 2):
    print("index[", i, "]", word[i])