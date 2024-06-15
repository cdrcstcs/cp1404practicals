FILENAME = "subject_data.txt"
def main():
    data = get_data()
    print(data)
    display_data_detail(data)
def get_data():
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  
        parts = line.split(',')  
        parts[2] = int(parts[2]) 
        datas.append(parts)
    input_file.close()
    return datas
def display_data_detail(datas):
    for data in datas:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[-1]:3} students")
main()
