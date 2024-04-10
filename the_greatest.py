#The Greatest Showdown
#Objective: Harness the power of conditional statements to compare and determine values.

#Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers.
# The program should then identify and print out the largest number among the three.

#Task 2: Identify the Smallest also determine the smallest number among the three and print it out. 
#(For bonus points create a continuous if elif else chain that extends from task 1 and will identify both largest and smallest numbers)

#Expected Outcome: If we provide the numbers 3, 1, and 4, it should print out "The Largest number is 4" "The smallest number is 1".

#Expected Bonus Outcome: "he largest number is 4 and smallest number is 3" (one print statement)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number between", num1, ",", num2, "and", num3, "is", largest)

if (num1 <= num2) and (num1 <= num3):
    smallest = num1
elif (num2 <= num1) and (num2 <= num3):
    smallest = num2
else:
    smallest = num3

print("The smallest number between", num1, ",", num2, "and", num3, "is", smallest)



