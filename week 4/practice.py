count = 0

with open("c:/PLP software engineering Assignments/Python Programming/week 4/file.txt", 'r') as file:
    data = file.read()
    for line in data.split():
        count += 1
print("Total number of words in the file:", count)

data_upper = data.upper()
with open("c:/PLP software engineering Assignments/Python Programming/week 4/output.txt", 'w') as file:
    file.write(data_upper)
    print("Data written to output.txt in uppercase.")