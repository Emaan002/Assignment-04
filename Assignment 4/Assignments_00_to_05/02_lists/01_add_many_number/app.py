
"""
Write a function that takes a list of numbers and returns the sum of those numbers.

"""


def add_many_numbers(numers) -> int:
    return sum(numers)


def main():
    numbers: int = [1,2,3,4,5,6,7,15,715,157] #list of numbers

    total: int = add_many_numbers(numbers) #put numbers list in add_many_numbers function and store it's answer in total variable

    print(f"\nThe list of numbers is {numbers}.\nThe sum of numbers is {total}.\n") # Print out the sum above



if __name__ == '__main__':
    main()