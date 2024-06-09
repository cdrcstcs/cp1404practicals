
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for number in range(0, 101, 10):
    print(number, end=' ')
print()

for number in range(20, 0, -1):
    print(number, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
star_count = 1
for star in range(1, number_of_stars+1, 1):
    print("*"*star_count)
    star_count += 1
