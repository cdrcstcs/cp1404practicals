import random
COLUMN_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 45
def main():
    quick_pick = get_valid_quick_pick()
    for pick in range(quick_pick):
        numbers = []
        for i in range(COLUMN_NUMBERS):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in numbers:
                number = random.randint(MINIMUM, MAXIMUM)
            numbers.append(number)
            numbers.sort()
        for number in numbers:
            print(f"{number:2}", end=" ")
        print()
def get_valid_quick_pick():
    quick_pick = int(input("How many quick picks? "))
    while quick_pick < 0:
        print("Invalid number")
        quick_pick = int(input("How many quick picks? "))
    return quick_pick
main()
