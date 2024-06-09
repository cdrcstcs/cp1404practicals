
SALES_BONUS_THRESHOLD = 1000
LOW_THRESHOLD_DISCOUNT_RATE = 0.10  # 10%
HIGH_THRESHOLD_DISCOUNT_RATE = 0.15  # 15%
sales = float(input("Enter Sales: $ "))
while sales >= 0:
    if sales < SALES_BONUS_THRESHOLD:

        discount_rate = LOW_THRESHOLD_DISCOUNT_RATE
    else:
        discount_rate = HIGH_THRESHOLD_DISCOUNT_RATE
    bonus = sales * discount_rate
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter Sales: $ "))
