import csv

with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\table.csv', 'r') as table:
    reader = list(csv.reader(table))
    reader[0][0] += ';my_col'
    for i in range (1, len(reader)-1):
        reader[i][0] += ';True'
with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\new_col.csv', 'w') as table1:
    writer = csv.writer(table1)
    writer.writerows(reader)