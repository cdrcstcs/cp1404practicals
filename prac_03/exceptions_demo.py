
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

# Questions
# When will a ValueError occur?
# It arises when the type of input value differs from the expected type.
# When will a ZeroDivisionError occur?
# It occurs when attempting to divide by zero.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes 
