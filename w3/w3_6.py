import csv

with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\table.csv', 'r') as table:
    reader = list(csv.reader(table))
    reader2 = reader[len(reader)//2:]
    reader = reader[:len(reader)//2]
    reader.append(['-200;-200;-200;-200'])
with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\middle_row.csv', 'w') as table1:
    writer = csv.writer(table1)
    writer.writerows(reader+reader2)