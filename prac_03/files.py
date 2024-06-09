IN_FILE = "numbers.txt"
total = 0
with open(IN_FILE) as in_file:
    for i in range(2):
        value = in_file.readline()
        total += int(value)
    print(int(total))
