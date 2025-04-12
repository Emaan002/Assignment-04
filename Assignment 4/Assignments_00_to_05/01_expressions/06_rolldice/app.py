"""
Simulate rolling two dice, and prints results of each roll as well as the total.
"""


import random
def main():
    
    # roll the dice
    die_1: int = random.randint(1,6) 
    die_2: int = random.randint(1,6)

    # sum of dice
    sum_of_dice = die_1 + die_2

    # print sum of dice with die value
    print("\nDice have 6 sides each.")
    print(f"First die {die_1}")
    print(f"Second die {die_2}")
    print(f"\nSum of two dice are {sum_of_dice}\n")  

if __name__ == '__main__':
    main()