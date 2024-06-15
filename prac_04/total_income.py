def main():
    incomes = []
    numbers_of_month = int(input("How many numbers_of_month? "))

    for month in range(1, numbers_of_month + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        # income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes, numbers_of_month)
def print_report(incomes, numbers_of_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
main()
