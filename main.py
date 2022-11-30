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