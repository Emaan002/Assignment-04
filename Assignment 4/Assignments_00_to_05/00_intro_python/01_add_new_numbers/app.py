# Add two numbers

"""
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message.

"""

def main():


    print("This program adds two numbers.")
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: ")) 

    sum_of_two_numbers = number_1 + number_2 
    print(f"Sum of {number_1} + {number_2} = {sum_of_two_numbers}") 


# This line ensures that the main() function runs when the script is executed 
if __name__ == "__main__":
    main()