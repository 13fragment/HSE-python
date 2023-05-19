with open("t3.txt", 'r') as file:
    data = file.readlines()
data = [line.strip() for line in data]
sorted_data = sorted(data, key=lambda x: x.split()[1])
for line in sorted_data:
    print(line)